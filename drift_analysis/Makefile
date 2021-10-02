OBSIDS = 1226062160 1274143152 1275178816 1283104232
JSON_TARGETS = $(addsuffix .json,$(OBSIDS))
MAXIMA_FILES = $(addsuffix .maxima,$(JSON_TARGETS))

%.json: force
	if [ -f $@ ]; then python ~/src/drift_analysis/drift_analysis.py $@; else python ~/src/drift_analysis/drift_analysis.py ../pdv/$*.pdv I; fi

maxima_plot.png: plot_maxima.gpi $(MAXIMA_FILES)
	gnuplot -e "set terminal pngcairo enhanced size 1500,500; set output '$@'" $<

force:
