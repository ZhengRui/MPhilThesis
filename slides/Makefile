dissertation.pdf: dissertation.tex \
					section/*.tex \

	xelatex --no-pdf dissertation.tex
	xelatex dissertation.tex

clean:
	rm *.aux *.toc *.log *.out *.nav *.snm
read:
	if [ -e evince.pid ]; then \
		kill -TERM $$(cat evince.pid) || true; \
	fi;
	evince main.pdf & echo $$! > evince.pid
