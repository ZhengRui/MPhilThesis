thesis.pdf: main.tex \
				chapter/*.tex \

	xelatex main.tex
	bibtex main
	xelatex main.tex

clean:
	rm *.aux *.bbl *.blg *.toc *.lof *.log *.lot
read:
	foxitreader thesis.pdf
