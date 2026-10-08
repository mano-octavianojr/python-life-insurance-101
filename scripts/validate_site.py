"""Check lesson coverage, local links, assets, downloads, and solution panels."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup
import nbformat

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'

def main():
    pages = sorted(SITE.glob('*.html'))
    assert len(pages) == 11
    links = 0
    for path in pages:
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        assert soup.html['lang'] == 'en'
        assert soup.find('meta', attrs={'name':'viewport'})
        assert soup.find(id='content') and soup.title
        for node in soup.select('[href], [src]'):
            target = node.get('href', node.get('src'))
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            destination = path.parent / unquote(url.path) if url.path else path
            assert destination.exists(), (path.name, target)
            if url.fragment and destination.suffix == '.html':
                other = BeautifulSoup(destination.read_text(), 'html.parser')
                assert other.find(id=unquote(url.fragment)), (path.name, target)
            links += 1
        if path.name != 'index.html':
            notebook_path = ROOT / 'notebooks' / (path.stem + '.ipynb')
            notebook = nbformat.read(notebook_path, as_version=4)
            assert (SITE / 'notebooks' / notebook_path.name).read_bytes() == notebook_path.read_bytes()
            # Compare full source code to exported code, preserving whitespace.
            exported = [node.get_text() for node in soup.select('.input_area pre')]
            original = [cell.source for cell in notebook.cells if cell.cell_type == 'code']
            assert len(exported) == len(original)
            assert all(a.strip() == b.strip() for a,b in zip(exported, original)), path.name
            for cell in notebook.cells:
                if cell.cell_type == 'markdown' and cell.source.startswith('## '):
                    assert cell.source.splitlines()[0][3:] in soup.get_text(), path.name
            assert soup.select_one('details.solution summary')
            assert soup.select_one('details.solution .input_area pre')
        print('PASS', path.name)
    assert (SITE / 'data/policy_records.csv').read_bytes() == (ROOT / 'data/policy_records.csv').read_bytes()
    print(f'Validated {len(pages)} pages and {links} local links, plus lesson code and downloads.')

if __name__ == '__main__':
    main()
