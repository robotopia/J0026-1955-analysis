# Processing 1275172216 in response to referee report

This is in response to the referee, who queried whether or not we were possibly getting an inaccurate nulling fraction by not looking for single pulses in 1275172216.

See also the parallel [README for 1275094456](../1275094456/README.md).

## Tasks

* [x] Download data
* [x] Manually recombine
* [x] Get calibration solution (1275172096, according to [Nick's spreadsheet](https://docs.google.com/spreadsheets/d/16bHhlqrGllyq_PD3Fb717MJfGCB1JFrUt2Ra2vPpWQE/edit#gid=0))
* [x] Beamform
* [ ] Fold (DSPSR)
* [ ] Make pulsestack
* [ ] Look for pulses

## Log

### 2022-02-21

Attempting to figure out why recombine is broken.

```
module use /pawsey/mwa/software/python3/modulefiles
module load vcstools
process_vcs.py -m recombine -o 1275172216 -a
```

Tracing down the error in the log files, it appears that cfitsio was not being found. Sure enough, nothing in the modules that *were* being loaded included cfitsio.
Thus, I added (back?) the line `load("cfitsio/3450")` in the file `/pawsey/mwa/software/python3/modulefiles/mwa-voltage/master.lua`.
I'm re-running now, and it appears to be working.

### 2022-02-22

1. Beamform
```
process_vcs.py -m beamform -a -o 1275172216 -O 1275172096 -p "00:26:37.30_-19:56:27.63"
```
2. Splice channels
```
cd /astro/mwavcs/vcs/1275172216/pointings/00:26:37.30_-19:56:27.63
splice.sh
> Project ID [G0024]: D0029
> Observation ID: 1275172216
> Pointing [None]: 00:26:37.30_-19:56:27.63
> Number of 200-second chunks [2]: 6
> Lowest coarse channel number [133]: 109
> Highest coarse channel number [156]: 132
```
