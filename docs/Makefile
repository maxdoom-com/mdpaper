# select markdown files 3 levels deep
MDFILES=test.md

# get the names of the pdf files to be created
PDFFILES=$(patsubst %.md, %.pdf, $(MDFILES))

RM=rm -f


# add some suffix rules for md > html > pdf conversion
.SUFFIXES:

.SUFFIXES:
%.pdf: %.html
	google-chrome --headless --no-margins --print-to-pdf=$@ $< 2> /dev/null
%.html: %.md
	env/bin/mdpaper $< > $@

# `make all` to create missing or changes pdf files
all: $(PDFFILES)

# `make clean` to remove all created pdf files
clean:
	$(RM) $(PDFFILES)

# `make re` to recreate all
re: clean all
