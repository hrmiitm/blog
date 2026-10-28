---
name: publish-post
description: Validate a Hugo post and publish authorized changes using this repository's GitHub Pages workflow.
---

Read `AGENTS.md` and inspect the working tree before editing. Preserve unrelated changes. Confirm required front matter, intended publication date, source links, and whether the user has authorized publication.

Run:

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_site.py
```

For draft preview use `hugo server --buildDrafts --disableFastRender`. For publishing, set the post's `draft` to `false` and ensure its date is not in the future. Inspect the generated post, home listing, and RSS entry. Check light/dark modes, phone width, navigation, and any new assets.

Commit and push to `main` only when authorized by the current request. Pull requests run the build without deploying; pushes to `main` deploy `public/` through `.github/workflows/deploy.yml`. Never commit generated `public/` files or put credentials in the repository.

Use `gh run list` and `gh run view` to check the workflow result. After successful deployment, verify the live post URL. If GitHub permissions, Pages settings, or environment rules block deployment, report the actual error and preserve the ready source; do not alter unrelated account settings. Stop after one clear failure diagnosis if credentials or user action are required.
