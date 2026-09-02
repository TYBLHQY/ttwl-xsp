#!/usr/bin/env python3
"""Post-process the pandoc-rendered HTML pages for GitHub Pages.

- Repoint pandoc's local KaTeX paths at a CDN so math actually renders on
  GitHub Pages.
- Inject SEO meta tags (description, canonical, Open Graph, Twitter) into
  every page.
- Set the html language to zh-CN.
- Append a footer linking to the raw Markdown source so an LLM / reader can
  grab the text directly.
- Write robots.txt, sitemap.xml and llms.txt for SEO + AI discoverability.
"""

import glob
import html as html_lib
import os
import re

SITE = "https://tyblhqy.github.io/ttwl-xsp"
BOOK = "天体物理概论"
AUTHOR = "向守平"
PUB = "中国科学技术大学出版社"
DESC = f"{BOOK}，{AUTHOR} 编著（彩色版）。{PUB} 2008"

KATEX = "0.16.11"
KATEX_JS = f"https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{KATEX}/katex.min.js"
KATEX_CSS = f"https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{KATEX}/katex.min.css"

META = """<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="author" content="向守平">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{book}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="zh_CN">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">"""

FOOTER = """<footer>
<p><a href="{src}">📄 Markdown 源文件</a>（可直接读取全文）</p>
</footer>
</body>"""

KEYWORDS = "天体物理概论, 向守平, 天体物理, 天文学, 宇宙学, 恒星, 星系, 致密星, 黑洞"


def fix_katex(text: str) -> str:
    text = text.replace("/usr/share/javascript/katex/katex.min.js", KATEX_JS)
    text = text.replace("/usr/share/javascript/katex/katex.min.css", KATEX_CSS)
    # pandoc emits an empty xml:lang with the trailing markup on other lines
    text = re.sub(
        r'<html([^>]*)lang=""([^>]*)xml:lang=""([^>]*)>',
        '<html lang="zh-CN">',
        text,
    )
    return text


def decorate_page(path: str) -> None:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    text = fix_katex(text)

    m = re.search(r"<title>(.*?)</title>", text)
    orig_title = m.group(1).strip() if m else os.path.basename(path)
    title = f"{BOOK} · {orig_title}"
    url = f"{SITE}/{os.path.basename(path)}"
    desc = re.sub(r"[ \n]+", " ", f"{orig_title}——{DESC}。").strip()

    meta = META.format(desc=desc, kw=KEYWORDS, url=url, title=title, book=BOOK)
    # insert right after <head>
    text = re.sub(r"(<head>)", r"\1\n" + meta, text, count=1)

    # title block (keep final), lang, footer
    text = re.sub(r"<title>.*?</title>", f"<title>{html_lib.escape(title)}</title>", text, flags=re.S)
    # replace the pandoc title-block header with our own simple h1? keep as is.

    src = os.path.basename(path).replace(".html", ".md")
    if "</body>" in text:
        text = text.replace("</body>", FOOTER.format(src=src), 1)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def decorate_index() -> None:
    path = "index.html"
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    text = fix_katex(text)

    title = BOOK
    url = f"{SITE}/"
    long_desc = (
        f"{BOOK}（{AUTHOR} 编著，彩色版），{PUB} 2008。全书共 7 章，"
        "涵盖绪论、基本天体物理量、恒星演化、致密星、星际物质、星系与宇宙学简介。"
    )

    # build hasPart from the md files (list of chapter pages)
    parts = sorted(glob.glob("ttwl_ch*.md")) + ["ttwl_front.md", "ttwl_back.md"]
    items = []
    for p in parts:
        with open(p, encoding="utf-8") as fh:
            head = fh.read(4000)
        t = re.search(r'^title:\s*"?(.+?)"?\s*$', head, re.M)
        nm = t.group(1) if t else p
        rel = p.replace(".md", ".html")
        items.append(
            f'{{"@type":"Chapter","name":{json_label(nm)},"url":"{SITE}/{rel}"}}'
        )
    haspart = ",\n    ".join(items)

    head_add = f"""<meta name="description" content="{long_desc}">
<meta name="keywords" content="{KEYWORDS}">
<meta name="author" content="向守平">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#1f3b70">
<meta property="og:type" content="book">
<meta property="og:site_name" content="{BOOK}">
<meta property="og:title" content="{BOOK}">
<meta property="og:description" content="{long_desc}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="zh_CN">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{BOOK}">
<meta name="twitter:description" content="{long_desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🌌</text></svg>">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": "{BOOK}",
  "author": {{"@type": "Person", "name": "向守平"}},
  "inLanguage": "zh-CN",
  "publisher": {{"@type": "Organization", "name": "中国科学技术大学出版社"}},
  "hasPart": [{haspart}]
}}
</script>"""

    text = re.sub(r"(<head>)", r"\1\n" + head_add, text, count=1)
    text = re.sub(r"<title>.*?</title>", f"<title>{html_lib.escape(title)}</title>", text, flags=re.S)
    text = re.sub(r'<html([^>]*)lang=""([^>]*)xml:lang=""([^>]*)>', '<html lang="zh-CN">', text)
    text = text.replace('lang="zh"', 'lang="zh-CN"')

    # AI note block in the body
    note = """
<section>
<h2>AI 阅读入口</h2>
<p>内容以 Markdown 源文件形式保存，可直接加载：<a href="llms.txt">llms.txt</a>，或任选一个 <code>.md</code> 章节。</p>
</section>
"""
    if "AI 阅读入口" not in text:
        text = text.replace("</body>", note + "</body>", 1)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def json_label(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_aux() -> None:
    with open("robots.txt", "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\nSitemap: " + SITE + "/sitemap.xml\n")

    urls = sorted(glob.glob("ttwl_*.html")) + ["index.html"]
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fh.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            loc = SITE + "/" + ("" if u == "index.html" else u)
            fh.write(f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq></url>\n")
        fh.write("</urlset>\n")

    with open("llms.txt", "w", encoding="utf-8") as fh:
        fh.write(f"# {BOOK}\n\n> {AUTHOR}\n")
        fh.write(f"> {BOOK}，中国科学技术大学出版社 2008，全书共 7 章。\n")
        fh.write("\n所有章节均以 Markdown（.md）源文件提供，可直接读取全文：\n\n")
        for p in sorted(glob.glob("ttwl_*.md")):
            t = "阅读全文"
            with open(p, encoding="utf-8") as g:
                m = re.search(r'^title:\s*"?(.+?)"?\s*$', g.read(4000), re.M)
            if m:
                t = m.group(1)
            fh.write(f"- [{t}]({p})\n")


if __name__ == "__main__":
    for page in sorted(glob.glob("ttwl_*.html")):
        decorate_page(page)
    decorate_index()
    write_aux()
    print("done")
