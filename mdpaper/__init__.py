import os
import markdown, jinja2

from .includemd import IncludeMD
from .includexls import IncludeXLS


def render(template_file, **data):
    env = jinja2.Environment( loader = jinja2.PackageLoader('mdpaper', 'templates') )
    env.trim_blocks = True
    # env.lstrip_blocks = True
    tpl = env.get_template(template_file)
    text = tpl.render(**data)

    return text

def mdtohtml(infile):
    with open(infile, 'r') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=[
            'tables',
            'admonition',
            'toc',
            'pymdownx.tilde',
            'pymdownx.magiclink',
            'codehilite',
            'def_list',
            IncludeMD(path=os.path.dirname(infile)),
            IncludeXLS(path=os.path.dirname(infile)),
        ])
        title = infile.split('/')[-1]
        output = render("doc.html", title=title, html=html)
        print(output)

