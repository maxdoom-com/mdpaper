from setuptools import setup

setup(
    name='mdpapaer',
    version='0.0.4',
    author='Nico Hoffmann',
    author_email='n-py-mdpaper@maxdoom.com',
    packages=['mdpaper',],
    scripts=['bin/mdpaper'],
    url='https://github.com/maxdoom-com/mdpaper/',
    license='LICENSE.md',
    description='A tiny utility to convert markdown to pdf using python and chrome',
    long_description=open('README.md').read(),
    install_requires=[
        'Jinja2',
        'Markdown',
        'Pygments',
        'pymdown-extensions',
        'xlrd',
    ],
    include_package_data=True,
    package_data={
        '': [
            'templates/doc.html',
        ],
    },
)
