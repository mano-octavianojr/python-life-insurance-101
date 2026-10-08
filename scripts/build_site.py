"""Build a portable training website directly from the source notebooks."""
from pathlib import Path
import html
import shutil
from urllib.parse import unquote
import nbformat
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'

def build():
    SITE.mkdir(exist_ok=True)
    (SITE / 'notebooks').mkdir(exist_ok=True)
    shutil.copytree(ROOT / 'data', SITE / 'data', dirs_exist_ok=True)
    exporter = HTMLExporter(template_name='basic')
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    lessons = []
    for path in sorted((ROOT / 'notebooks').glob('*.ipynb')):
        notebook = nbformat.read(path, as_version=4)
        title = notebook.cells[0].source.splitlines()[0].removeprefix('# ')
        goals = next(cell.source.split('\n\n', 1)[1] for cell in notebook.cells if cell.cell_type == 'markdown' and cell.source.startswith('## Learning goals'))
        lessons.append((path, notebook, title, goals))
    def page(title, body):
        return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} · Python Life Insurance 101</title><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#content">Skip to content</a><header><a class="brand" href="index.html">Python Life Insurance 101</a><a href="https://github.com/mano-octavianojr/python-life-insurance-101">GitHub ↗</a></header>{body}<footer>Fictional examples for learning. Real insurance depends on policy terms and applicable law.</footer></body></html>'''
    cards = []
    for index, (path, notebook, title, goals) in enumerate(lessons):
        filename = path.stem + '.html'
        nav = '<nav class="lesson-nav" aria-label="Lesson navigation"><a href="index.html">← All lessons</a>'
        if index:
            nav += f'<a href="{lessons[index-1][0].stem}.html">Previous lesson</a>'
        if index + 1 < len(lessons):
            nav += f'<a href="{lessons[index+1][0].stem}.html">Next lesson →</a>'
        nav += '</nav>'
        # Collapsed solutions let readers try the exercise before seeing an answer.
        body, _ = exporter.from_notebook_node(notebook)
        # Group the solution explanation and its code in a native disclosure panel.
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(body, 'html.parser')
        for element in soup.select('[id]'):
            element['id'] = unquote(element['id'])
        heading = soup.find('h2', id='Sample-solution')
        if heading:
            wrapper = heading.find_parent('div', class_='cell')
            following = wrapper.find_next_sibling('div', class_='cell')
            if wrapper and following:
                details = soup.new_tag('details', attrs={'class':'solution'})
                summary = soup.new_tag('summary')
                summary.string = 'Reveal sample solution'
                details.append(summary)
                wrapper.insert_before(details)
                details.append(wrapper.extract())
                details.append(following.extract())
        tools = f'<aside class="reader-note">Read the lesson here. To run or edit Python, <a href="notebooks/{path.name}" download>download this notebook</a> and use Jupyter. Lesson 08 also uses <a href="data/policy_records.csv" download>the sample CSV</a>; keep it in a data folder beside notebooks. <a href="index.html#setup">Setup instructions</a>.</aside>'
        (SITE / filename).write_text(page(title, f'{nav}<main id="content" class="lesson">{tools}{soup}</main>{nav}'))
        shutil.copy2(path, SITE / 'notebooks' / path.name)
        cards.append(f'<a class="card" href="{filename}"><span class="number">LESSON {index+1:02}</span><h3>{html.escape(title[4:])}</h3><p>{html.escape(goals)}</p><span class="read">Read lesson →</span></a>')
    body = '''<main id="content"><section class="hero"><p class="eyebrow">A free course for high school students</p><h1>Learn Python.<br>Make sense of life insurance.</h1><p class="intro">Join Maya and Leo for ten stories that turn everyday questions into code. Start with your first message and finish with your own policy explorer.</p><a class="button" href="01_first_program.html">Start learning →</a><div class="facts"><span>10 guided lessons</span><span>No coding experience needed</span><span>45–60 minutes each</span></div></section><section class="overview"><h2>Your learning journey</h2><p>Each lesson includes a story, simple explanations, code demos, a challenge, hints, and a sample solution. Work in order and predict what the code will do before running it.</p></section><section class="grid" aria-label="Training lessons">'''+''.join(cards)+'''</section><section id="setup" class="setup"><h2>Ready to try the code?</h2><p>This website is a reading companion. Run the notebooks in JupyterLab on your computer with Python 3.10 or newer. Download the repository to keep notebooks and sample data together.</p><ol><li>Clone or download <a href="https://github.com/mano-octavianojr/python-life-insurance-101">the GitHub repository</a>.</li><li>Open a terminal in the project folder and run the commands below.</li><li>In JupyterLab, open notebooks/01_first_program.ipynb. Press Shift+Enter to run a cell.</li></ol><pre><code>python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab</code></pre><p>Windows activation: <code>.venv\\Scripts\\activate</code>. Try the student workspace before revealing the solution. Restart the kernel and run all cells to reset a lesson.</p></section><section class="scope"><h2>Made for learning</h2><p>All people, policies, prices, and records are fictional. Examples use Philippine pesos and teach concepts in everyday words. They are not real quotations or financial advice. Never share personal financial or health information.</p><p>Teachers: see the <a href="https://github.com/mano-octavianojr/python-life-insurance-101/blob/main/TEACHER_GUIDE.md">teacher guide</a> for expected answers and discussion points.</p></section></main>'''
    (SITE / 'index.html').write_text(page('Learn Python through stories', body))
    (SITE / '.nojekyll').touch()
    print(f'Built {len(lessons)} lessons and homepage in {SITE}')

if __name__ == '__main__':
    build()
