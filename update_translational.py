from pathlib import Path
import re

root = Path(__file__).resolve().parent
index = Path.cwd() / 'index.md'
if not index.is_file():
    raise SystemExit('index.md not found in current directory. Run this from the Jekyll repository root.')
source = index.read_text(encoding='utf-8')
replacement = (root / 'translational-section.html').read_text(encoding='utf-8').strip('\n')

# Locate complete section tags by ID, regardless of attribute order or line breaks.
open_sections = list(re.finditer(r'<section\b[^>]*>', source, re.I | re.S))
sections = []
for m in open_sections:
    id_match = re.search(r'\bid\s*=\s*(["\'])(.*?)\1', m.group(), re.I | re.S)
    if id_match:
        sections.append((id_match.group(2).strip(), m))
consulting = [m for name, m in sections if name == 'consulting']
if len(consulting) != 1:
    print('Section IDs detected:', [name for name, _ in sections])
    raise SystemExit('Cannot uniquely find <section id="consulting">. Please share the current index.md section; no changes made.')
start = consulting[0].start()
# Find the first closing section tag after the consulting section opening.
close = re.search(r'</section\s*>', source[consulting[0].end():], re.I)
if not close:
    raise SystemExit('Consulting section closing tag not found; no changes made.')
end = consulting[0].end() + close.end()
# Guard against unexpected nested sections or replacing beyond the institutional block.
if re.search(r'<section\b', source[consulting[0].end():end - len(close.group())], re.I):
    raise SystemExit('Nested section detected; no changes made.')
if not re.search(r'Bioinformatics|Translational Research|Research Team Training', source[start:end], re.I):
    raise SystemExit('Unexpected consulting section content; no changes made.')
new = source[:start] + replacement.lstrip() + source[end:]
if new == source:
    print('Already up to date.')
else:
    index.write_text(new, encoding='utf-8')
    print('Updated only the consulting section in index.md.')
