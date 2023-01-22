#!/bin/sh

cat \
    doc.html.in1 \
    css/github-markdown.css \
    css/pygments-default.css \
    css/style.css \
    doc.html.in2 \
> doc.html

