import html
import re

def sanitize_text(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return re.sub(r"[^\x09\x0A\x0D\x20-\x7E]", "", text)

def format_html_preview(text: str) -> str:
    safe = html.escape(text)
    safe = safe.replace("\n\n", "<br><br>").replace("\n", "<br>")
    return (
        '<div style="padding:22px;border-radius:12px;border:1px solid #444;'
        'background:#181818;color:#f4f4f4;line-height:1.65;">'
        f"{safe}</div>"
    )
