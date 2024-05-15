# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# src/main.py
# This is the main file for MarkdownBlog and is called by `make` to generate the blog

import os
import json

from lib import logger
from lib import formatter

def get_pages():
    os.chdir("content/pages")
    pages = os.listdir()
    os.chdir("../../")
    return pages

def load_page_content(page_path):
    try:
        with open(f"{page_path}/meta.json") as f:
            meta = json.load(f)
        with open(f"{page_path}/page.md") as f:
            page_content = f.read()
        return meta, page_content
    except FileNotFoundError:
        logger.error(f"Page content not found for: {page_path}")
        return None, None

def generate_html(meta, formatted_page_content, base_template):
    base = base_template.replace('<div class="main" id="main">', "<div class='main' id='main'>\n<p class='date'>"+meta["Date"]+"</p>"+formatted_page_content)
    base = base.replace("<title></title>", f"<title>{meta['Title']}</title>")
    base = base.replace('<meta name="description" content="">', f'<meta name="description" content="{meta["Description"]}">')
    base = base.replace('<meta name="keywords" content="">', f'<meta name="keywords" content="{meta["Keywords"]}">')
    base = base.replace('<meta name="author" content="">', f'<meta name="author" content="{meta["Author"]}">')
    base = base.replace('<meta name="og:image" content="">', f'<meta name="og:image" content="{meta["Image"]}">')
    base = base.replace('<meta name="og:title" content="">', f'<meta name="og:title" content="{meta["Title"]}">')
    base = base.replace('<meta name="og:description" content="">', f'<meta name="og:description" content="{meta["Description"]}">')
    base = base.replace('<meta name="og:created_time" content="">', f'<meta name="og:created_time" content="{meta["Date"]}">')
    return base

def main():
    logger.log("Starting MarkdownBlog")
    pages = get_pages()
    logger.debug(f"Found {len(pages)} pages")

    base_template_path = "content/html/base.html"
    try:
        with open(base_template_path) as f:
            base_template = f.read()
    except FileNotFoundError:
        logger.error("Base template file not found.")
        return

    for page in pages:
        page_path = f"content/pages/{page}"
        meta, page_content = load_page_content(page_path)
        if meta is None or page_content is None:
            continue

        formatted_page_content = formatter.format_page_content(page_content)
        html_content = generate_html(meta, formatted_page_content, base_template)

        if page == "home":
            output_path = "www/index.html"
        else:
            output_path = f"www/{page}/index.html"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

        try:
            with open(output_path, "w") as f:
                f.write(html_content)
            logger.log(f"Generated HTML for page: {page}")
        except Exception as e:
            logger.error(f"Error writing HTML content for page {page}: {e}")
    logger.success("Finished generating HTML files.")

if __name__ == "__main__":
    main()
