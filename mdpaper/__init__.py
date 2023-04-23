import os
import markdown, jinja2

from .includemd import IncludeMD
from .includexls import IncludeXLS


def render(template_file, **data):
    env = jinja2.Environment( loader = jinja2.PackageLoader('mdpaper', 'templates') )
    env.trim_blocks = True
    # env.lstrip_blocks = True
    tpl = env.get_template(template_file)
    return tpl.render(**data)


# def render_text(text, path):
#     env = jinja2.Environment(
#         loader                  = jinja2.FileSystemLoader(path),
#         block_start_string      = '{{%',
#         block_end_string        = '%}}',
#         variable_start_string   = '{{{',
#         variable_end_string     = '}}}',
#     )
#     env.trim_blocks = True
#     # env.lstrip_blocks = True
#     tpl = env.from_string(text)
#     return tpl.render()



def mdtohtml(infile):
    with open(infile, 'r') as f:
        text = f.read()

        # # use jinja on the markdown text before interpreting it as markdown
        # text = render_text(text, os.path.dirname(infile))

        # compile html out of the markdown code
        html = markdown.markdown(text, extensions=[
            'tables',
            'admonition',
            'toc',
            'pymdownx.tilde',
            'pymdownx.magiclink',
            'pymdownx.tasklist',
            'pymdownx.mark',
            'codehilite',
            'def_list',
            'markdown_inline_graphviz',
            IncludeMD(path=os.path.dirname(infile)),
            IncludeXLS(path=os.path.dirname(infile)),
        ])
        title = infile.split('/')[-1]

        # write the output as html file
        output = render("doc.html", title=title, html=html)
        print(output)

