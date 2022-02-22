TARGETS = main.pdf

all: $(TARGETS)

%.pdf: %.tex %.bib
	pdflatex $*
	bibtex $*
	pdflatex $*
	pdflatex $*
