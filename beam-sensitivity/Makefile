EPHEMERIS = psr2_obs_4_5_6.eph
RA  = $(shell awk '/^RAJ/ {print $$2}' < $(EPHEMERIS))
DEC = $(shell awk '/^DECJ/ {print $$2}' < $(EPHEMERIS))

OBSIDS = $(shell cat obsids.txt)
TARGETS = $(patsubst %,%_beam.txt,$(OBSIDS))

.SECONDARY:

all: $(TARGETS)

%_beam.txt: %.fits
	mwa_track_primary_beam_response -m $< -r $(RA) -d $(DEC) -o $@

%.fits:
	wget -O $@ http://ws.mwatelescope.org/metadata/fits?obs_id=$*
