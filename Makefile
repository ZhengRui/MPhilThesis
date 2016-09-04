main.pdf: main.tex \
				chapter/*.tex \

	xelatex --no-pdf main.tex
	biber main
	xelatex --no-pdf main.tex
	xelatex main.tex

clean:
	rm *.aux *.bbl *.blg *.toc *.lof *.log *.lot *.bcf *.xml *.xdv *.out
read:
	if [ -e evince.pid ]; then \
		kill -TERM $$(cat evince.pid) || true; \
	fi;
	evince main.pdf & echo $$! > evince.pid
