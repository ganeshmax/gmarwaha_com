#!/usr/bin/env python3
"""
Convert the "Related Reading" / "Mobile Payments Blog Series" sections
and their following bullet-list into a fully-rendered HTML div (no markdown inside).

This script handles both:
- Previously un-wrapped files (looks for #### heading)
- Already wrapped files that have raw markdown inside the div

The result is a standalone HTML block that Kramdown won't try to parse.
"""

import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')

# Match section headings
HEADING_RE = re.compile(
    r'^####\s+(Related Reading|Mobile Payments Blog Series|Related Posts|Further Reading)[:\s]*$',
    re.IGNORECASE | re.MULTILINE
)

# Already-wrapped but still with markdown inside
WRAPPED_HEADING_RE = re.compile(
    r'<div class="related-reading">\s*\n<p class="related-reading-title">([^<]+)</p>\s*\n(.*?)</div>',
    re.DOTALL
)

# Markdown link: - [text](url)
MD_LINK_RE = re.compile(r'-\s+\[([^\]]+)\]\(([^\)]+)\)')


def md_list_to_html(md_text):
    """Convert markdown list of links to HTML list items."""
    items = []
    for m in MD_LINK_RE.finditer(md_text):
        text = m.group(1).strip()
        url = m.group(2).strip()
        items.append(f'    <li><a href="{url}">{text}</a></li>')
    if not items:
        return ''
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def build_div(title, md_body):
    html_list = md_list_to_html(md_body)
    if not html_list:
        return None
    return (
        f'\n\n<div class="related-reading">\n'
        f'<p class="related-reading-title">{title}</p>\n'
        f'{html_list}\n'
        f'</div>\n'
    )


total = 0

for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Case 1: Already wrapped — fix the markdown inside
    wrapped_match = WRAPPED_HEADING_RE.search(content)
    if wrapped_match:
        title = wrapped_match.group(1).strip()
        md_body = wrapped_match.group(2)
        new_div = build_div(title, md_body)
        if new_div:
            new_content = content[:wrapped_match.start()] + new_div + content[wrapped_match.end():]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Fixed (already wrapped): {fname}")
            total += 1
        continue

    # Case 2: Raw heading not yet wrapped
    heading_match = HEADING_RE.search(content)
    if not heading_match:
        continue

    title = heading_match.group(1).strip()
    heading_start = heading_match.start()
    after_heading = content[heading_match.end():]

    new_div = build_div(title, after_heading)
    if not new_div:
        continue

    before = content[:heading_start].rstrip('\n')
    new_content = before + new_div

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  Wrapped: {fname}")
    total += 1

print(f"\nDone. Processed {total} files.")
