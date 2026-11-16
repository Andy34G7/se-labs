#!/usr/bin/env python3
"""
Generates clean, purely monochrome (all black, no color fills/accents) PDF deliverables
for SE Lab 3, guaranteeing zero table overflows outside margins.
"""

import os
import re
import markdown
import weasyprint

def build_pdf():
    base_dir = '/home/andey/Documents/Sem5/SE/lab3'
    readme_path = os.path.join(base_dir, 'README.md')
    img_path = os.path.join(base_dir, 'component_diagram.png')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc']
    )

    # Use direct file path for local image rendering
    html_body = html_body.replace('src="component_diagram.png"', f'src="{img_path}"')

    # Remove mermaid block from PDF
    html_body = re.sub(
        r'<pre><code class="language-mermaid">.*?</code></pre>',
        '',
        html_body,
        flags=re.DOTALL
    )

    # Pure black and white styling, no colors, no tints, strictly contained tables
    css_content = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

@page {
    size: A4;
    margin: 12mm 12mm 12mm 12mm;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #000000;
    background-color: #ffffff;
    line-height: 1.5;
    font-size: 13px;
    margin: 0;
    padding: 0;
}

h1 {
    font-size: 20px;
    font-weight: 700;
    color: #000000;
    margin-top: 0;
    margin-bottom: 12px;
}

h2 {
    font-size: 16px;
    font-weight: 700;
    color: #000000;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h3 {
    font-size: 14px;
    font-weight: 600;
    color: #000000;
    margin-top: 16px;
    margin-bottom: 6px;
    page-break-after: avoid;
}

h4 {
    font-size: 13px;
    font-weight: 600;
    color: #000000;
    margin-top: 12px;
    margin-bottom: 4px;
    page-break-after: avoid;
}

p {
    margin-top: 4px;
    margin-bottom: 8px;
    color: #000000;
}

ul {
    list-style-type: disc;
    margin-top: 4px;
    margin-bottom: 8px;
    padding-left: 22px;
    color: #000000;
}

ol {
    list-style-type: decimal;
    margin-top: 4px;
    margin-bottom: 8px;
    padding-left: 22px;
    color: #000000;
}

ul ul {
    list-style-type: circle;
    margin-top: 2px;
    margin-bottom: 4px;
    padding-left: 18px;
}

ol ol, ul ol, ol ul {
    margin-top: 2px;
    margin-bottom: 4px;
    padding-left: 18px;
}

li {
    margin-bottom: 3px;
    color: #000000;
    line-height: 1.45;
}

li p {
    margin: 0;
    display: inline;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 11px;
    page-break-inside: auto;
    table-layout: fixed;
    word-break: break-word;
    overflow-wrap: break-word;
}

tr {
    page-break-inside: avoid;
    page-break-after: auto;
}

th {
    background-color: #ffffff;
    color: #000000;
    font-weight: 700;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #000000;
    word-break: break-word;
    overflow-wrap: break-word;
}

td {
    background-color: #ffffff;
    color: #000000;
    padding: 6px 8px;
    border: 1px solid #000000;
    vertical-align: top;
    word-break: break-word;
    overflow-wrap: break-word;
}

tr:nth-child(even) {
    background-color: #ffffff;
}

hr {
    border: none;
    border-top: 1px solid #000000;
    margin: 16px 0;
}

code {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 11px;
    background-color: #ffffff;
    color: #000000;
    padding: 1px 3px;
    border: 1px solid #cccccc;
    border-radius: 2px;
    word-break: break-word;
    overflow-wrap: break-word;
    white-space: normal;
}

pre {
    background-color: #ffffff;
    color: #000000;
    padding: 8px;
    border: 1px solid #000000;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 11px;
    line-height: 1.4;
    page-break-inside: avoid;
    word-break: break-word;
    white-space: pre-wrap;
}

pre code {
    background-color: transparent;
    color: #000000;
    border: none;
    padding: 0;
}

img {
    max-width: 100%;
    height: auto;
    border: 1px solid #000000;
    margin: 10px 0;
    page-break-inside: avoid;
}

blockquote {
    border-left: 3px solid #000000;
    padding-left: 10px;
    margin: 10px 0;
    color: #000000;
    background-color: #ffffff;
}

a {
    color: #000000;
    text-decoration: underline;
}
"""

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Lab 3: Component Modelling & Architectural Pattern Selection</title>
<style>
{css_content}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

    html_out = os.path.join(base_dir, 'README.html')
    with open(html_out, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Written all-black HTML: {html_out}")

    # Generate standard PDFs
    html_obj = weasyprint.HTML(string=full_html, base_url=base_dir)

    targets = [
        os.path.join(base_dir, 'PES2UG24CS061.pdf'),
        os.path.join(base_dir, 'PES2UG24CS061_SE_Lab3.pdf'),
        os.path.join(base_dir, 'README.pdf')
    ]

    for target in targets:
        html_obj.write_pdf(target)
        print(f"Generated all-black PDF: {target}")

if __name__ == '__main__':
    build_pdf()
