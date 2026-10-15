"""Dependency-free checks for the buildless Pages artifact."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1] / 'site'
errors = []

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.h1s = 0
        self.title = False
        self.lang = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:
                errors.append(f'Duplicate id: {a["id"]}')
            self.ids.add(a['id'])
        if tag == 'h1': self.h1s += 1
        if tag == 'title': self.title = True
        if tag == 'html': self.lang = a.get('lang') == 'en'
        if tag == 'script': errors.append('Unexpected script')
        if tag == 'form': errors.append('Unexpected form')
        if tag == 'img' and 'alt' not in a: errors.append('Image missing alt')
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])

docs = {}
for path in ROOT.rglob('*.html'):
    doc = Document()
    doc.feed(path.read_text())
    docs[path.resolve()] = doc
    if doc.h1s != 1 or not doc.title or not doc.lang:
        errors.append(f'Heading/title/language problem: {path.relative_to(ROOT)}')
    if 'main' not in doc.ids: errors.append(f'Missing skip target: {path}')
for path, doc in docs.items():
    for link in doc.links:
        url = urlsplit(link)
        if url.scheme:
            if url.scheme != 'https': errors.append(f'Unexpected URL scheme: {link}')
            continue
        if url.netloc or url.path.startswith('/'):
            errors.append(f'Non-relative URL breaks repository subpaths: {link}')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir(): target = target / 'index.html'
        if not target.is_relative_to(ROOT.resolve()):
            errors.append(f'URL escapes public artifact: {link}')
        elif not target.is_file(): errors.append(f'Broken local link in {path.name}: {link}')
        elif url.fragment and (target not in docs or unquote(url.fragment) not in docs[target].ids):
            errors.append(f'Broken anchor: {link}')
for css in ROOT.rglob('*.css'):
    for resource in re.findall(r'url\([\'"]?([^\)\'"]+)', css.read_text()):
        if not (css.parent / resource).is_file(): errors.append(f'Broken CSS asset: {resource}')
if set(p.relative_to(ROOT).as_posix() for p in docs) != {'index.html', 'support/index.html', 'privacy/index.html'}:
    errors.append('Expected exactly the three planned pages')
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix not in {'.html', '.css', '.png', '.jpg'} and path.name != '.nojekyll':
        errors.append(f'Unexpected public artifact: {path.name}')
workflow = (ROOT.parent / '.github/workflows/pages.yml').read_text()
if 'path: site' not in workflow: errors.append('Workflow must upload only site/')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(docs)} pages, local links/anchors, CSS assets, metadata, relative paths and public artifact boundary.')
