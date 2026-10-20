LATEXMK ?= latexmk

.PHONY: all clean
all:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	$(LATEXMK) -c main.tex
