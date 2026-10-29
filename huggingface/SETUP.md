# Weekly Accessible Chatbots dataset updates

GitHub remains the authoring source. The workflow exports only the approved public root documents listed in `export-config.json` to the existing `GarethFW/accessible-chatbots` dataset. It never changes dataset visibility or `.gitattributes` and never uses an LLM or OpenAI API.

## Enable the connection

1. Create a **fine-grained** Hugging Face access token at https://huggingface.co/settings/tokens named `GitHub accessible-chatbots sync`. Grant read and write access only to `GarethFW/accessible-chatbots`. Keep unrelated repository, account and inference permissions off. Never paste the token in a chat, file, commit or issue.
2. In GitHub, open Accessible-Chatbots → Settings → Secrets and variables → Actions → New repository secret. Name it `HF_TOKEN`; paste the token into the Secret field and save.
3. Merge the pull request containing this workflow into the default branch after reviewing the change. These files configure the update but cannot prove the first authenticated publish has succeeded.
4. Open Actions → Update Hugging Face dataset → Run workflow. Choose the default branch and run it once. If GitHub asks you to enable Actions, enable it for this repository.
5. Open the run. A green check and the final step summary confirm publishing or that the dataset was already up to date. Check the dataset's Files and versions commit history and its Dataset card. The first automated export changes its version to 0.2.0.

## Schedule and visibility

Runs are scheduled for Mondays at **07:23 UTC**, meaning 07:23 UK winter time or 08:23 UK summer time. GitHub may delay schedules, and may disable public-repository schedules after 60 days without repository activity. Check Actions periodically and configure your GitHub notifications for failed workflow runs. No independent missed-run monitoring service is installed.

The Hugging Face dataset can remain private for testing. The publisher uses its existing privacy setting. Changing it to public is a separate deliberate step in Hugging Face Settings after review.

## What changes automatically

The export uses committed files from the workflow's source revision. Updated text and deleted optional documents are reflected in the generated snapshots. New files need an explicit addition to the approved file list. Missing required sources, changed licence text, missing or duplicated C00–C23 identifiers, unresolved dependencies or validation failures stop the update. Adding new chunk identifiers requires a reviewed converter change. Only the seven managed destination files are replaced; other destination files are preserved.

Each row records its GitHub revision and content hash. Export dates come from the source commit so repeated runs of the same revision produce identical bytes. A run compares all managed files with one Hugging Face revision and commits updates together, rejecting concurrent destination changes rather than overwriting them blindly. Source changes can remove records from the latest snapshot but do not erase historical releases, downloaded copies or trained model knowledge.

## Troubleshooting and stopping

- Missing token or denied access: check the `HF_TOKEN` secret, token expiry and dataset-specific read/write permissions. Do not print the token into logs.
- Source check failure: confirm the GitHub repository is public. Private GitHub content must not pass this publisher.
- Export validation failure: inspect the Build and validate dataset step; restore valid IDs/dependencies or arrange a reviewed converter/configuration update.
- Concurrent edit: inspect the destination changes, then run the workflow again when ready.
- To pause: Actions → Update Hugging Face dataset → workflow menu → Disable workflow. To revoke access, also delete the GitHub secret and revoke the Hugging Face token.

Local verification uses `python -m unittest discover -s tests -p 'test_huggingface_sync.py' -v` after installing `huggingface/requirements.txt`. Live authenticated publication and Hugging Face viewer behaviour require the first real workflow run; tests do not claim either has happened.

## Maintainer notes

Only run the workflow on the original repository's default branch. It has no pull-request trigger. The token is available only to the publishing step. Action revisions and direct Python dependencies are pinned; maintainers should review dependency updates. Exported source text remains unchanged, including declared review status and known stale references; extraction validation is not a subject-matter approval.
