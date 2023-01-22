import os
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

"""
a preprocessor that simply includes other files, even recursively!

usage in markdown:

    ...
    #md filename
    ...


usage in python:
    from includemd import IncludeMD

    ...
    markdown.markdown(text, extensions=[
        ...
        IncludeMD(path=os.path.dirname(infile)),
        ...
    ])
    ...
"""

class IncludeMDPreprocessor(Preprocessor):

    def __init__(self, md, path):
        self.path = path
        super(self.__class__, self).__init__(md)


    def _incl(self, filename):
        new_lines = []

        with open(os.path.join( self.path, filename)) as file:
            for line in file.readlines():
                
                splitted = line.split()
                if len(splitted) > 0 and splitted[0] == '#md':
                    filename = splitted[1]
                    for line in self._incl(filename):
                        new_lines.append(line)
                else:
                    new_lines.append( line.rstrip('\n') )

        return new_lines


    def _process_lines(self, lines):
        new_lines = []

        for line in lines:
            
            splitted = line.split()
            if len(splitted) > 0 and splitted[0] == '#md':
                filename = splitted[1]
                for line in self._incl(filename):
                    new_lines.append(line)

            else:
                new_lines.append(line)
        
        return new_lines


    def run(self, lines):
        return self._process_lines(lines)




class IncludeMD(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'path': [kwargs['path'], ],
        }
        super(self.__class__, self).__init__(**kwargs)


    def extendMarkdown(self, md):
        md.preprocessors.register(IncludeMDPreprocessor(md, self.config['path'][0]), 'include.md', 1)
