---
name: write-post
description: Create or revise Markdown blog posts in this repository, including front matter, clear titles, evidence links, and concise editing.
---

Read `AGENTS.md`, the user's source material, and relevant existing posts. Follow the user's voice if supplied. Otherwise use plain, concrete language and focus on one main reader benefit. Do not imitate another author's personal identity.

Create `content/posts/YYYY/slug.md` with YAML front matter:

```yaml
---
title: "A clear, specific title"
date: 2026-10-28T18:00:00+05:30
slug: "a-clear-specific-title"
description: "One concise sentence explaining what the reader gets."
tags: ["Topic"]
draft: true
---
```

Replace the example date with the actual intended publication time in the author's timezone. Keep `draft: true` until publication is authorized. Use `verified: "YYYY-MM-DD"` for researched guides. The optional `art: "archive"` selects the existing archive illustration; omit it for unrelated posts.

Start with a concrete question, discovery, or useful claim. Use H2 for main sections so the table of contents works; use H3 for subdivisions. Do not put an H1 in the body. Link sources beside claims. Tables suit comparisons; lists suit steps or genuinely parallel choices.

The author prefers minimal, engaging notes. Organize practical posts around what the reader wants to do, rather than giving each tool an identical section. A service name and one useful distinction may be enough. Do not repeat a comparison table in prose. Keep caveats where they change the reader's action; avoid repeating generic warnings after every recommendation. For short posts, set `toc: false` so navigation does not overwhelm the writing.

Before finishing, read the draft as a reader: does the opening give a reason to continue, does each paragraph add something, and can the reader act on the advice? Cut repetition and reference-manual scaffolding before adding polish. Keep a memorable user-suggested title when it fits the article.

First-person statements must come from provided experience or work actually performed. Remove invented anecdotes, unsupported superlatives, repeated takeaways, promotional phrases, and filler. Write a descriptive title and summary that match the final content. Use `explain-concepts` for difficult teaching passages and `research-post` when verification is needed.

Preview the post on phone and desktop widths. Follow `publish-post` for build checks and authorized publication.
