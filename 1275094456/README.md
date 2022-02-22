# Processing observation 1275094456 to look for single pulses

This is in response to the referee, who queried whether or not we were possibly getting an inaccurate nulling fraction by not looking for single pulses in 1275094456.

See also the parallel [README for 1275172216](../1275172216/README.md).

* [x] Download data
* [x] Manually recombine
* [x] Get calibration solution (1275085696, according to [Nick's spreadsheet](https://docs.google.com/spreadsheets/d/16bHhlqrGllyq_PD3Fb717MJfGCB1JFrUt2Ra2vPpWQE/edit#gid=0))
* [x] Beamform
* [x] Splice channels
* [ ] Fold (DSPSR)
* [ ] Make pulsestack
* [ ] Look for pulses
* [ ] Remove raw data

## Log

### 2022-02-22

1. Recombine:
```
module use /pawsey/mwa/software/python3/modulefiles
module load vcstools
process_vcs.py -m recombine -o 1275094456 -a
```
2. Beamform
```
process_vcs.py -m beamform -a -o 1275094456 -O 1275085696 -p "00:26:37.30_-19:56:27.63"
```
3. Splice channels
```
cd /astro/mwavcs/vcs/1275094456/pointings/00:26:37.30_-19:56:27.63
splice.sh
> Project ID [G0024]: D0029
> Observation ID: 1275094456
> Pointing [None]: 00:26:37.30_-19:56:27.63
> Number of 200-second chunks [2]: 6
> Lowest coarse channel number [133]: 109
> Highest coarse channel number [156]: 132
```

### 2022-02-23 (planned)

1. Fold (DSPSR)
Copy the par file (`0024.par`, from the root directory of this repo) to Garrawarla, as well as the `dspsr.batch` script in this directory.
Then,
```
sbatch dspsr.batch
```
