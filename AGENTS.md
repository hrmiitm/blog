# Working on this blog

This is a small Hugo site for https://hrmiitm.github.io/blog/. Keep it static and preserve the minimal design, accessibility, and both color themes.

- Posts: `content/posts/YYYY/slug.md`. These are the source of truth; edit them directly.
- Standalone pages: `content/`. Templates: `layouts/`. CSS/JS/images: `static/`.
- All reusable agent skills live together in `.agents/skills/`. Read the relevant `SKILL.md` before that task:
  - `post-ideas`: choose topics and angles.
  - `research-post`: research sources and check claims.
  - `write-post`: draft and edit Markdown posts in the author's voice.
  - `explain-concepts`: make difficult ideas understandable.
  - `data-story`: turn actual analysis into a post.
  - `post-visuals`: create charts, diagrams, or other supporting visuals.
  - `publish-post`: validate a post and use the GitHub Pages pipeline.
- Build with Hugo 0.162.1: `hugo --gc --minify --panicOnWarning`.
- Run `python3 scripts/check_site.py` after a build. Preview with `hugo server --disableFastRender`.
- Do not hand-edit `public/` or commit generated output. Do not introduce a package manager, database, or theme dependency without a concrete need.
- Keep `/blog/` in production links. Use Hugo's `relURL` or `.RelPermalink` in templates.
- Do not fabricate first-person experiences, quotes, benchmarks, or capture results. Cite factual service claims near the claim and date time-sensitive checks.
- Creating drafts and running local checks is allowed. Commit, push, and publish only when the current user request authorizes those actions. A prior request to publish one post does not authorize future unrelated publications.
