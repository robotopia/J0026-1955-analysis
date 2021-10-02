OBSIDS = 1226062160 1274143152 1275178816 1283104232
DSPSR_TARGETS = $(addprefix dspsr_,$(OBSIDS))
ARCHIVES = $(addsuffix .F,$(OBSIDS))
PDV_TARGETS = $(addsuffix .pdv,$(OBSIDS))

dspsr: $(DSPSR_TARGETS)

dspsr_%:
	# OBSID $*: On Garrawarla:
	@echo "mkdir -p /astro/mwavcs/pulsar_search/psr2_J0024-1932/$*/single"
	@echo "cd /astro/mwavcs/pulsar_search/psr2_J0024-1932/$*/single"
	@echo "module load singularity"
	@echo "/pawsey/mwa/singularity/dspsr/dspsr.sif dspsr -b 1024 -E 0026_simple.eph -s -j 'F' -U 600 ../$*_*_ch109-132_0001.fits"
	@echo "singularity run -B ~/.Xauthority /pawsey/mwa/singularity/psrchive_tempo2/psrchive_tempo2.sif psradd -o $*.F \$$(cat ordered.txt)"
	@echo "singularity run -B ~/.Xauthority /pawsey/mwa/singularity/psrchive_tempo2/psrchive_tempo2.sif pav -g $*_pulsestack.png/png -YFpC -b 2 -z 0.35,0.65 $*.F"

download: $(ARCHIVES)

%.F:
	rsync -aPv hpc-data:/astro/mwavcs/pulsar_search/psr2_J0024-1932/$*/single/$*.F .

%.pdv: %.F
	pdv -tK $< > $@

0026.eph:
	rsync -avP hpc-data:/astro/mwavcs/pulsar_search/psr2_timing/psr2_obs_4_5_6.eph $@
