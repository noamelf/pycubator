#! /usr/bin/python3

from pathlib import Path
import sys
import os

from jinja2 import Environment, FileSystemLoader
from nbconvert.exporters import HTMLExporter
from nbconvert.preprocessors import ClearOutputPreprocessor
templates = None
DOCS_DIR = 'docs'

def get_tmpl(name):
    global templates
    if not templates:
        templates = Environment(loader=FileSystemLoader('templates/'))
    return templates.get_template(name)


def extract_slide_title(md_file):
    with md_file.open() as f:
        for l in f:
            if '#' in l:
                return l.strip('# \n')


def get_md_files():
    p = Path('content', 'slides')
    for md_file in sorted(p.iterdir()):
        if md_file.suffix == '.md':
            yield str(md_file), md_file.with_suffix('.html').name, extract_slide_title(md_file)


def pre_clean():
    p = Path('.')
    for i in p.glob(DOCS_DIR + '/*.html'):
        i.unlink()


def generate_slides(md_files):
    slide_tmpl = get_tmpl('slide.j2')
    if not os.path.exists(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    for md_file, html_file, title in md_files:
        rendered_template = slide_tmpl.render(mdfile=md_file, title=title)

        filepath = os.path.join(DOCS_DIR, html_file)
        with open(filepath, 'w') as f:
            f.write(rendered_template)


def generate_index(md_files):
    index_tmpl = get_tmpl('index.j2')
    filepath = os.path.join(DOCS_DIR, 'index.html')
    with open(filepath, 'w') as f:
        f.write(index_tmpl.render(slides=md_files))


def generate_exercises():
    p = Path('content', 'exercises')
    exporter = HTMLExporter()
    exporter.register_preprocessor(ClearOutputPreprocessor(), enabled=True)

    for exercise in p.iterdir():
        if exercise.suffix == '.ipynb':
            html, _ = exporter.from_file(exercise.open())
            with open(exercise.with_suffix('.html').name, 'w') as f:
                f.write(html)


def main():
    pre_clean()

    md_files = list(get_md_files())

    generate_slides(md_files)
    generate_index(md_files)
    generate_exercises()


if __name__ == '__main__':
    sys.exit(main())
