mdpaper
========================================================================

A tiny utility to convert markdown to html.


Requirements
------------------------------------------------------------------------

These python libraries are required:

- markdown


Installation
------------------------------------------------------------------------

In a virtual environment (i.e. `./env/`) you can install it this way:

    :::sh
    pip install git+https://github.com/maxdoom-com/mdpaper.git


Usage
------------------------------------------------------------------------

    ::sh
    env/bin/mdpaper path/to/your/markdown.md


Conversion to PDF
------------------------------------------------------------------------

See the Makefile in the docs.


Supported markdown syntax
------------------------------------------------------------------------

Basically it supports everythin that ist supported by:

- (markdown) tables
- (markdown) admonition',
- (markdown) toc',
- (pymdownx) tilde',
- (pymdownx) pymdownx.magiclink',
- (pymdownx) pymdownx.tasklist',
- (pymdownx) pymdownx.mark',
- (markdown) codehilite',
- (markdown) def_list',
- (extension) IncludeMD
- (extension) IncludeXLS




Example
------------------------------------------------------------------------

    :::text
    Test (MD)
    ========================================================================

    [TOC]

    ---

    Admonitions
    ========================================================================

    !!! danger "Danger!"
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    !!! warning "Warning!"
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    !!! okay "Okay!"
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    ---

    Page breaks
    ========================================================================

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    ---

    Page 2
    ------------------------------------------------------------------------

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    ---

    Page 3
    ------------------------------------------------------------------------

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


    ---

    Task List (pymarkdownx)
    ------------------------------------------------------------------------

    - [X] item 1
        * [x] item A
        * [ ] item B
            more text
            + [x] item a
            + [ ] item b
            + [x] item c
        * [X] item C
    - [ ] item 2
    - [ ] item 3


    ---

    Include Test
    ========================================================================

    > This is an extension!

    #md include-test.md

    ---

    XLS Import
    ========================================================================

    > This is an extension!

    #xls Test1.xls 0

    ---

    ... and a lot more!


