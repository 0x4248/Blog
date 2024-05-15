# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# src/lib/formatter.py
# formats the markdown and html files when building
# the blog.

import markdown

def format_markdown(content):
    formatted = ""
    incode = False
    for line in content.split("\n"):
        if line.startswith("```") and not incode:
            incode = True
            formatted += "<pre>\n"
            continue
        elif line.startswith("```") and incode:
            incode = False
            formatted += "</pre>\n"
            continue
        else:
            formatted += line + "\n"
    return formatted

def format_page_content(page_content):
    page_content = format_markdown(page_content)
    page_content = markdown.markdown(page_content)
    formatted_page_content = ""
    incode = False
    for line in page_content.split("\n"):
        if line.startswith("<pre>") and not incode:
            incode = True
            formatted_page_content += "\t\t\t"+line+"\n"
            continue
        if line.startswith("</pre>") and incode:
            incode = False
            formatted_page_content += "\t\t\t"+line+"\n"
            continue
        if incode:
            formatted_page_content += line+"\n"
        else:
            formatted_page_content += "\t\t\t"+line+"\n"
    return formatted_page_content