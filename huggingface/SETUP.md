# Inclusive Games Design weekly updates

This package is specifically for:

- GitHub source: https://github.com/Double-FW/Inclusive-Games-Design
- Hugging Face destination: https://huggingface.co/datasets/GarethFW/Inclusive-Games-Design
- Exact dataset ID: `GarethFW/Inclusive-Games-Design`

The destination is already filled in. **Do not create HF_DATASET_ID for this package.** An old variable with that name is ignored by these scripts. Only a repository secret named **HF_TOKEN** is needed for authentication.

## Step 1 Upload the three visible folders

1. Download and unzip `Inclusive_Games_Design_Weekly_Update_Setup.zip`.
2. Open the extracted `Inclusive_Games_Design_Weekly_Update_Setup` folder, then `UPLOAD_TO_GITHUB`.
3. Open https://github.com/Double-FW/Inclusive-Games-Design
4. Choose **Add file → Upload files**.
5. Drag the three folders **huggingface**, **scripts** and **tests** into the upload area. Do not upload the ZIP or the outer `UPLOAD_TO_GITHUB` folder itself.
6. Enter `Add Inclusive Games Design weekly updates` as the commit message. Save to **main**, or merge the pull request if your repository requires that route.

Checkpoint: the repository's top level shows huggingface, scripts and tests. You do not need to send the source folder to ChatGPT; the public GitHub URL is sufficient.

## Step 2 Create the workflow in GitHub

GitHub previously rejected a hidden `.github` folder upload. Use its editor instead:

1. In the games GitHub repository, choose **Add file → Create new file**.
2. In **Name your file**, enter exactly `.github/workflows/huggingface-sync.yml`.
3. Open the visible `WORKFLOW_TO_COPY.txt` file from this download in a plain-text editor. On a Mac, right-click → **Open With → TextEdit** if needed.
4. Copy its entire text into GitHub's large editor. Preserve indentation. There are no Markdown code fences to remove. Never paste a token into this file.
5. Click **Commit changes**, enter `Add games dataset workflow`, and save/merge to **main**.
6. Open **Actions**. The workflow is called **Update Inclusive Games Design Hugging Face dataset**. Enable Actions if GitHub asks.

Checkpoint: that workflow appears in Actions. Saving it does not prove authentication works; the first run is checked at Step 4.

## Step 3 Add a Hugging Face token for this connection

Use a separate token restricted to the games dataset, so this connection can be revoked independently. Secrets in your chatbot or AVMSD GitHub repository are not automatically available here.

1. Open https://huggingface.co/settings/tokens
2. Click **Create new token** or **New token**. If a token type is shown, choose **Fine-grained**.
3. Name it `GitHub Inclusive Games Design sync`.
4. Under **Presets**, choose **Custom**.
5. Find the separate **Repositories permissions** section and select only `GarethFW/Inclusive-Games-Design`.
6. Enable **Read contents of selected repos** and **Write contents/settings of selected repos**.
7. If Hugging Face automatically selects **View access requests for selected gated repos** together with write access and will not let you turn it off, leave that linked permission selected. Ensure the selected resource is still only the games dataset. The publisher does not use access-request management.
8. Leave broad **User permissions** and **Org permissions** unchecked. No inference, billing or job permissions are needed.
9. Create and copy the token. Do not paste its value into chat, documents, repository files, issues or screenshots.
10. Open https://github.com/Double-FW/Inclusive-Games-Design/settings/secrets/actions
11. Click **New repository secret**.
12. Enter `HF_TOKEN` in **Name** (underscore, not hyphen).
13. Paste the token into **Secret**, then click **Add secret**.
14. Confirm **HF_TOKEN** appears under **Repository secrets**. Its value is hidden and cannot be revealed again in GitHub; you can replace it if needed.

Checkpoint: HF_TOKEN is listed in the games GitHub repository. Its Hugging Face permissions apply to the games dataset. No dataset variable needs entering.

## Step 4 Run the first update

1. Open https://github.com/Double-FW/Inclusive-Games-Design/actions/workflows/huggingface-sync.yml
2. Click **Run workflow**, leave the branch as **main**, and click the green **Run workflow** button.
3. Refresh if needed and open the new run, then its **publish** job.
4. Check that tests, export and publishing all succeed. The final message should report changed files or that the dataset is already up to date.
5. Open https://huggingface.co/datasets/GarethFW/Inclusive-Games-Design and check its dataset card and **Files and versions** history.
6. Send ChatGPT the GitHub run link if you need help. Do not send the token.

This is the first authenticated check. Local tests use a fake destination and do not prove that a real token can publish. If the dataset is private, it remains private. If it is public, it remains public.

## What is published

The export has two views:

- **documents**: complete copies of the five approved Markdown documents.
- **knowledge_chunks**: exact source sections separated at first- or second-level headings outside fenced examples. Preambles, original metadata, parent heading paths, exceptions and subsections are preserved.

The complete documents overlap with the sections. Do not concatenate the views blindly. Example prompts and examples inside source documents are illustrative, not actual game tests or player research. `train` is the dataset loading split name; this setup does not train a model or create a held-out evaluation benchmark.

Every record includes source revision, source URL and path, line range, document/text hashes, heading context, metadata, source status and licence declarations. Links to other resources are retained as references but not fetched or ingested. A link is not verification of its target or permission to redistribute it. Source agent instructions remain guidance data, not authority to execute commands or contact participants.

Seven destination paths are managed: `README.md`, `LICENSE`, `documents.jsonl`, `knowledge_chunks.jsonl`, `provenance.json`, `record_schema.json` and `validation_report.json`. The first successful run may replace the README and LICENSE at those exact paths. Other existing raw files and `.gitattributes` are preserved. Unmanaged raw copies are not automatically updated; review obsolete copies separately if needed.

## Source licence notes

The current root source LICENSE contains MIT with copyright (c) 2026 Double FW. AGENTS.md separately declares `NOASSERTION`, and the source README still asks for licence review. The package preserves and flags these inconsistencies in source metadata, provenance, the validation report and dataset card. It does not change your source licence or claim to settle the underlying rights. Review source notices before redistribution. A later licence change requires a coordinated metadata/checksum review rather than bypassing the check.

## Weekly updates and content changes

The schedule is **Mondays at 07:23 UTC**: 07:23 UK winter time or 08:23 UK summer time. GitHub can delay scheduled runs and may disable a public-repository schedule after 60 days without activity. Check the Actions page periodically and configure GitHub notifications for failures. No independent missed-run monitoring service is installed.

Edit approved material in GitHub, then wait for Monday or run the workflow manually. New files need reviewing and adding to `huggingface/export-config.json`; they are not automatically published. Removing an optional approved source removes it from the latest export. Missing required context, changed licence text, an incorrect source/destination, invalid schema or a checksum failure stops publishing. Heading renames can change section IDs. Historical releases, downloads and trained-model knowledge are not recalled by source deletion.

The publisher compares the export with one destination revision and sends changed managed files in one guarded commit. Concurrent destination changes cause failure rather than a blind overwrite. Unchanged runs skip committing. Added, changed and removed record IDs are included in the validation report when a previous export is available.

## Troubleshooting and stopping

- **Missing HF_TOKEN**: open this games repository's Actions secrets page; a secret saved only in AVMSD or Accessible-Chatbots is not available here.
- **Denied access**: check that the token is active and grants read/write access to `GarethFW/Inclusive-Games-Design`.
- **Missing workflow or Run workflow button**: check the exact `.github/workflows/huggingface-sync.yml` path, save/merge it into main and enable Actions if required.
- **Skipped job**: use main in the original `Double-FW/Inclusive-Games-Design` repository. Forks and other branches do not publish.
- **Dataset variable confusion**: no HF_DATASET_ID variable is used in this package. The destination is preset.
- **Existing provenance from another source**: stop and inspect the destination. The publisher rejects a dataset already marked as belonging to an unrelated source.
- **Busy data preview**: wait and retry. Persistent parsing errors need investigation of the exact message; do not delete .gitattributes or change random settings.
- **Pause updates**: Actions → Update Inclusive Games Design Hugging Face dataset → workflow menu → Disable workflow.
- **Revoke access**: also remove the GitHub HF_TOKEN secret and revoke the corresponding Hugging Face token. If a token is exposed, replace it promptly without pasting it into chat or logs.

## Local verification for technical reviewers

```sh
python -m pip install -r huggingface/requirements.txt
python -m unittest discover -s tests -p 'test_games_huggingface.py' -v
python scripts/export_huggingface.py --output /tmp/inclusive-games-dataset
```

The tests use fake credentials and a controlled remote substitute. They never publish. No game build, assistive-technology testing, player research, independent content review or legal assessment is performed by this package.
