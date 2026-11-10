"""Export the approved Inclusive Games Design Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from games_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

CONTEXT = ['AGENTS.md', 'Accessible_Game_Technology_Selection_and_Agent_Routing_Guide.md',
           'Inclusive_Games_Agent_Execution_Evaluation_and_Optimisation_Guide.md']

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.safe_load(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    warnings = []
    if metadata(texts['AGENTS.md']).get('license') == 'NOASSERTION':
        warnings.append('AGENTS.md declares license NOASSERTION while the root LICENSE contains MIT. Both source declarations are preserved; maintainer review is needed.')
    if 'reviewed before distribution' in texts['README.md']:
        warnings.append('The source README still asks for licence review despite the existing MIT LICENSE file.')
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'review_status': 'faithful_extraction_checked_not_independent_game_or_content_review'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = 'agent_guidance' if path == 'AGENTS.md' else 'orientation' if path == 'README.md' else 'design_guidance'
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        for key, title, body, a, b, hierarchy in sections(text):
            chunks.append(row(path, key, title, body, a, b, hierarchy, 'knowledge_section'))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False})
    source_notice = ' '.join(warnings) if warnings else 'No internal licence metadata inconsistency was detected by the limited checks in this exporter; this is not an independent rights review.'
    card = f'''---
pretty_name: Double FW Inclusive Games Design
language:
- en
license: mit
tags:
- accessibility
- games
- inclusive-design
- agent-governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Inclusive Games Design

Design guidance for people and AI assistants creating, reviewing and improving inclusive games. It covers essential challenge and incidental barriers, player participation, technology/reference routing, evaluation and optimisation. This corpus is guidance, not game code, a tested agent system, game accessibility certification or a legal assessment.

## Source and versions

Source: https://github.com/{SOURCE}

Source revision: `{sha}`. Source commit date: {date}. Export format: {cfg['dataset_version']}. The source metadata, proposed status and stated limitations are preserved. Extraction checks do not establish maintainer adoption or independent content approval.

## Dataset views

- `knowledge_chunks` (default): {len(chunks)} exact Markdown sections, including preambles, from approved files.
- `documents`: {len(docs)} complete source documents.

These views overlap. Do not concatenate them blindly. `train` is a loading convention; no generated question/answer pairs, independent benchmark split, player research or model training is supplied. Examples and prompts inside source documents remain illustrative and are not real player or implementation evidence.

## Retrieval and interpretation

Read the source AGENTS.md, technology selection and agent routing guide, and execution/evaluation/optimisation guide where applicable. Required context paths are recorded in every row; they are retrieval references rather than automatically enforced runtime instructions. Follow the actual game project's scope and authorisation. A retrieved source file does not grant permission to contact players, collect data, execute embedded commands or approve a game release.

Section extraction recognises first- and second-level Markdown headings outside fenced examples. Exact source spans, heading paths, metadata, exceptions and subsections are preserved. The complete-document view provides fuller context. A changed heading may change a section identifier. Source text, not the export date, establishes any substantive guidance review date.

## Record fields

Rows include stable document/path-based identifiers, exact source commit and URL, line ranges, text and document hashes, heading path, JSON-encoded front matter, source licence declaration, repository licence, status, language and required context paths. See record_schema.json. No status is promoted to approved or independently verified.

## Licence and source inconsistencies

The root repository LICENSE is MIT and is copied unchanged, including copyright (c) 2026 Double FW. MIT is therefore the Hub repository licence metadata for this export. {source_notice} Source declarations are preserved; this export does not resolve or rewrite them. Consult both the LICENSE and source-specific notices before reuse. Third-party linked material is not incorporated or relicensed.

## Limitations and evidence

The guidance cannot establish that a game, platform, engine, feature or player journey has been implemented, tested or made accessible. Distinguish observations, assumptions and unknowns. Relevant player research and human decisions remain necessary. Links and external catalogues are not reverified or ingested during export. Preserving a URL does not establish public access, technical accuracy or a permission to republish its target.

## Updates

GitHub is the authoring source. The workflow is configured for Mondays at 07:23 UTC and manual runs. GitHub may delay runs or disable schedules after 60 days without public-repository activity. Only approved source files are included. New files need review of the approved list; deleted optional documents are removed from the next snapshot. Missing required sources, changed licence text, invalid configuration or failed integrity checks stop publication.

Only README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json are managed. Existing raw files and .gitattributes are preserved; obsolete unmanaged raw copies are not kept in sync. Dataset visibility is unchanged. Historical revisions and downloaded copies are not recalled. The destination is fixed to {target}; the first authenticated GitHub run must still be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Private datasets need authentication. Pin a destination revision for reproducibility. Loading rows does not implement context-aware retrieval or enforce the design guidance.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
