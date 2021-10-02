OBSIDS = 1226062160 1274143152 1275178816 1283104232
JSON_TARGETS = $(addsuffix .json,$(OBSIDS))

%.json: force
	if [ -f $@ ]; then python ~/src/drift_analysis/drift_analysis.py $@; else python ~/src/drift_analysis/drift_analysis.py ../pdv/$*.pdv I; fi

force:
