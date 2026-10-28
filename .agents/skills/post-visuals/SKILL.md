---
name: post-visuals
description: Create or select supporting diagrams, charts, and illustrations for this blog's posts.
---

Decide what one idea the visual helps the reader understand. Skip decorative images that do not improve the post. Use a simple SVG for small diagrams, a standard plotting tool for data charts, and suitable image tools for raster artwork when available.

Keep published files in `static/images/slug/`. In Markdown use relative image paths that remain under `/blog/`; from `/posts/slug/`, `../../images/slug/file.svg` resolves correctly. Use descriptive alt text and captions containing source or method when needed. Do not assume Mermaid fences render: this site does not load a Mermaid runtime.

For charts, choose the right units and denominator, label axes, show missing data honestly, and avoid misleading scales. Check both themes, grayscale readability, phone width, and label overlap. Make SVG artwork readable without relying only on color.

For interactive explainers, justify why reader interaction improves understanding, retain a useful initial view, support keyboard and touch, and provide a static explanation. Keep scripts local and avoid adding a framework for a single figure.
