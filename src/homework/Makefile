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
	rm -rf $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).out *.blg *.bbl *.run.xml $(TEXFILE).toc *-blx.bib $(TEXFILE).lol $(TEXFILE).loa

\BLOCK{else}

$(TEXFILE).pdf: $(TEXFILE).tex
	pdflatex $(TEXFILE).tex
	pdflatex $(TEXFILE).tex

.PHONY: clean
clean:
	rm -rf $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).out $(TEXFILE).toc $(TEXFILE).lol $(TEXFILE).loa

\BLOCK{endif}

.PHONY: view
view: $(TEXFILE).pdf
	evince $(TEXFILE).pdf &
