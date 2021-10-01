OBSIDS = 1226062160 1274143152 1275178816 1283104232 1287670032 1290341112
FITS = $(addsuffix .fits,$(OBSIDS))

download: $(FITS)

%.fits:
	rsync -aPv hpc-data:/astro/mwavcs/pulsar_search/psr2_J0024-1932/$*/$*_*.fits .

0026.eph:
	rsync -avP hpc-data:/astro/mwavcs/pulsar_search/psr2_timing/psr2_obs_4_5_6.eph $@
