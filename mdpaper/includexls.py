import os, xlrd
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

"""
A markdown extension to include xls files from markdown files (pagewise).

usage in markdown:

    ...
    #xls filename pagenumber
    ...


usage in python:
    from includexls import IncludeXLS

    ...
    markdown.markdown(text, extensions=[
        ...
        IncludeXLS(path=os.path.dirname(infile)),
        ...
    ])
    ...
"""

class IncludeXLSPreprocessor(Preprocessor):

    def __init__(self, md, path):
        self.path = path
        super(self.__class__, self).__init__(md)


    def _incl(self, filename, pagenumber=0):
        book = xlrd.open_workbook( os.path.join(self.path, filename))
        sheet = book.sheet_by_index(pagenumber)

        lines = []

        for y in range(sheet.nrows):
            if y == 0: # headers...
                lines.append( '| ' + ' | '.join([ sheet.cell_value(y, x) for x in range(sheet.ncols) ]) + ' |' )
                lines.append( '| ' + ' | '.join([ '---' ]*sheet.ncols) + ' |' )
            else: # content...
                lines.append( '| ' + ' | '.join([ sheet.cell_value(y, x) for x in range(sheet.ncols) ]) + ' |' )

        return lines


    def _process_lines(self, lines):
        new_lines = []

        for line in lines:
            
            splitted = line.split()
            if len(splitted) > 0 and splitted[0] == '#xls':
                filename = splitted[1]
                pagenumber = int(splitted[2])
                for line in self._incl(filename, pagenumber):
                    new_lines.append(line)

            else:
                new_lines.append(line)
        
        return new_lines


    def run(self, lines):
        return self._process_lines(lines)




class IncludeXLS(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'path': [kwargs['path'], ],
        }
        super(self.__class__, self).__init__(**kwargs)


    def extendMarkdown(self, md):
        md.preprocessors.register(IncludeXLSPreprocessor(md, self.config['path'][0]), 'include.xls', 1)
