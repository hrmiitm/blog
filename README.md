# hrmiitm / notes

A minimal static blog at **https://hrmiitm.github.io/blog/**, built with Hugo and deployed by GitHub Actions. Light and dark themes, responsive reading layouts, article contents, RSS, sitemap, and a custom 404 page. No theme dependency, JavaScript framework, database, or Node installation required.

## Local preview

Install [Hugo](https://gohugo.io/installation/) **0.162.1** (standard edition is enough), then:

```sh
hugo server --disableFastRender
```

Open the URL printed by Hugo. Add `--buildDrafts` when working on unpublished posts.

## Add a post

Create `content/posts/YYYY/your-post.md`:

```yaml
---
title: "Your post title"
date: 2026-10-28T18:00:00+05:30
slug: "your-post"
description: "A short description for the listing, feed, and search engines."
tags: ["Topic"]
draft: true
---
```

Write Markdown below the front matter. Use H2 headings for main sections; the article contents are generated automatically. Set the date to your intended publication time and `draft: false` when ready. Future-dated posts are not published until a build runs after that date. Workflows run on pushes and manual dispatch, not on a schedule.

Time-sensitive guides can include `verified: "YYYY-MM-DD"`. Short posts can set `toc: false` to hide the table of contents. Put supporting images in `static/images/your-post/`. Templates accept an optional `art: "archive"` for the existing archive illustration; omit it for other subjects. Tags are displayed as labels; no empty tag archives are generated.

Before publishing:

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_site.py
```

Push to `main` to build and deploy. Pull requests build and validate without deploying. Deployment status appears under the repository's **Actions** tab. GitHub Pages must use **GitHub Actions** as its source (already configured for this repository).

## Architecture

```text
content/               Markdown posts and standalone pages
layouts/               Small Hugo templates, partials, and RSS template
static/                CSS, theme toggle, favicon, and future images
.agents/skills/        All seven reusable post-creation skills
scripts/check_site.py  Build checks using only Python's standard library
.github/workflows/     Build, check, and GitHub Pages deployment
hugo.toml              Site identity, URL, and build configuration
```

Hugo creates `public/`; it is ignored by Git and uploaded by the workflow. The `/blog/` base path is configured in `hugo.toml`. Change that value if you later add a custom domain or rename the repository.

## Agent skills

Read `AGENTS.md` for repository conventions. All skills are in one folder, `.agents/skills/`:

| Skill              | Purpose                                           |
| ------------------ | ------------------------------------------------- |
| `post-ideas`       | Choose a question, topic, and useful angle        |
| `research-post`    | Verify claims and keep source provenance          |
| `write-post`       | Draft and edit Markdown with correct front matter |
| `explain-concepts` | Make difficult ideas understandable               |
| `data-story`       | Write from actual datasets or experiments         |
| `post-visuals`     | Make charts, diagrams, or supporting images       |
| `publish-post`     | Check, preview, and publish authorized changes    |

These are original, project-specific instructions, informed by the skill roles discussed in [sanand0's agents](https://github.com/sanand0/scripts/tree/main/agents) and [writing skills](https://github.com/sanand0/blog/tree/main/pages/skills). They do not reproduce another author's personal voice. Agent tools that support repository skills can discover `.agents/skills/`; other tools can read the relevant `SKILL.md` directly.

## Theme behavior

The first visit follows the device color preference. The header button switches between light and dark and remembers the selection locally. If local storage is unavailable, the toggle still works for the current page. With JavaScript disabled, CSS follows the device preference and hides the inactive button.

## First article

[The Web Has a Memory](content/posts/2026/save-a-page-before-it-disappears.md) explains how to find and save pages, with seven archiving options. Sources were reviewed on 28 October 2026; no archive requests were made on the reader's behalf. Service descriptions are documentation-based, not a comparative capture benchmark.
