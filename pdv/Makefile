OBSIDS = 1226062160 1274143152 1275178816 1283104232
PDV_TARGETS = $(addsuffix .pdv,$(OBSIDS))

all: $(PDV_TARGETS)

%.pdv: ../fits/%.F
	pdv -tK $< > $@
