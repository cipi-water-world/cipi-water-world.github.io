"""Build index.html (a full web page for GitHub Pages) from app.html.

app.html is the single source: it is also what gets published as the Claude artifact,
which adds its own <html>/<head>/<body> wrapper. This script adds that wrapper for
normal hosting, plus share-preview tags for WhatsApp and other apps.

Usage:  python3 build.py https://USERNAME.github.io/cipi-water-world/
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
base = (sys.argv[1] if len(sys.argv) > 1 else "").rstrip("/") + "/"

src = (ROOT / "app.html").read_text(encoding="utf-8")
split = src.index("</style>") + len("</style>")
head, body = src[:split], src[split:]

title = "Cipi's Water World"
desc = "Ikuti Cipi si tetes air keliling siklus air, buka peti hadiah, lalu ikut Ujian Cipi. IPAS Kelas 5 SD."
extra = f"""<meta name="description" content="{desc}">
<meta name="theme-color" content="#F7EBDA">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-180.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}og.png">
<meta property="og:url" content="{base}">
<meta name="twitter:card" content="summary_large_image">
"""

page = f'<!doctype html>\n<html lang="id">\n<head>\n{head}\n{extra}</head>\n<body>\n{body.strip()}\n</body>\n</html>\n'
(ROOT / "index.html").write_text(page, encoding="utf-8")
print(f"index.html written ({len(page):,} bytes), base URL: {base}")
