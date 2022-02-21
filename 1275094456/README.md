# Processing observation 1275094456 to look for single pulses

This is in response to the referee, who queried whether or not we were possibly getting an inaccurate nulling fraction by not looking for single pulses in 1275094456.

See also the parallel [README for 1275172216](../1275172216/README.md).

* [x] Download data
* [ ] Manually recombine
* [ ] Beamform

## Log

### 2022-02-22

* Recombined:
```
module use /pawsey/mwa/software/python3/modulefiles
module load vcstools
process_vcs.py -m recombine -o 1275094456 -a
```
