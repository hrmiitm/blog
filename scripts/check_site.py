#!/usr/bin/env python3
"""Check the built site's links, fragments, metadata, and RSS; stdlib only."""

from html.parser import HTMLParser
from pathlib import Path
import sys
import tomllib
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
CONFIG = tomllib.loads((ROOT / "hugo.toml").read_text())
BASE = CONFIG["baseURL"]
BASE_PARTS = urlsplit(BASE)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1s = 0
        self.description = False
        self.canonical = False
        self.lang = False
        self.main = False
        self.problems = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.problems.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1s += 1
        if tag == "html":
            self.lang = bool(attrs.get("lang"))
        if tag == "main":
            self.main = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = bool(attrs.get("content"))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = bool(attrs.get("href"))
        if tag == "img" and not attrs.get("alt"):
            self.problems.append("image is missing descriptive alt text")
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def check():
    pages = {}
    errors = []
    for path in sorted(PUBLIC.rglob("*.html")):
        page = Page()
        page.feed(path.read_text())
        pages[path] = page
        for label, passed in (
            ("exactly one h1", page.h1s == 1),
            ("description", page.description),
            ("canonical URL", page.canonical),
            ("language", page.lang),
            ("main landmark", page.main),
        ):
            if not passed:
                errors.append(f"{path.relative_to(PUBLIC)}: missing/invalid {label}")
        errors.extend(f"{path.relative_to(PUBLIC)}: {p}" for p in page.problems)

    if not pages:
        errors.append("No HTML files. Run Hugo first.")

    for path, page in pages.items():
        relative = path.relative_to(PUBLIC).as_posix()
        page_url = urljoin(BASE, relative.removesuffix("index.html"))
        for link in page.links:
            resolved = urlsplit(urljoin(page_url, link))
            if resolved.scheme not in {"http", "https"} or resolved.netloc != BASE_PARTS.netloc:
                continue
            if not resolved.path.startswith(BASE_PARTS.path):
                errors.append(f"{relative}: link escapes /blog/: {link}")
                continue
            target_name = unquote(resolved.path[len(BASE_PARTS.path):])
            target = PUBLIC / target_name
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{relative}: broken local link: {link}")
            elif resolved.fragment and target in pages and unquote(resolved.fragment) not in pages[target].ids:
                errors.append(f"{relative}: missing fragment: {link}")

    for required in ("index.html", "posts/index.html", "about/index.html", "404.html", "index.xml", "sitemap.xml", "robots.txt"):
        if not (PUBLIC / required).is_file():
            errors.append(f"Missing output: {required}")
    try:
        rss = ET.parse(PUBLIC / "index.xml")
        for item in rss.findall("./channel/item"):
            link = item.findtext("link", "")
            if not link.startswith(urljoin(BASE, "posts/")):
                errors.append(f"RSS includes a non-post URL: {link}")
    except (ET.ParseError, FileNotFoundError) as exc:
        errors.append(f"Invalid RSS: {exc}")

    if errors:
        print("Site check failed:\n" + "\n".join(f"- {e}" for e in errors))
        return 1
    print(f"Checked {len(pages)} HTML pages, local links, fragments, metadata, and RSS.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
