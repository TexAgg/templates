TEXFILE = main

.PHONY: all
all: $(TEXFILE).pdf

\BLOCK{if args["bib"]}
$(TEXFILE).pdf: $(TEXFILE).tex sources.bib
	pdflatex $(TEXFILE)
	pdflatex $(TEXFILE)
	bibtex $(TEXFILE)
	pdflatex $(TEXFILE)
	pdflatex $(TEXFILE)

.PHONY: clean
clean:
	rm -rf *.aux *.log *.out *.blg *.bbl *.run.xml *.toc

\BLOCK{else}

$(TEXFILE).pdf: $(TEXFILE).tex
	pdflatex $(TEXFILE).tex
	pdflatex $(TEXFILE).tex

.PHONY: clean
clean:
	rm -rf *.aux *.log *.out *.toc

\BLOCK{endif}

.PHONY: view
view: $(TEXFILE).pdf
	evince $(TEXFILE).pdf &
