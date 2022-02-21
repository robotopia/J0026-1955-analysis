# Log

## 2022-02-21

Attempting to figure out why recombine is broken.

```
module use /pawsey/mwa/software/python3/modulefiles
module load vcstools
process_vcs.py -m recombine -o 1275172216 -a
```

Tracing down the error in the log files, it appears that cfitsio was not being found. Sure enough, nothing in the modules that *were* being loaded included cfitsio.
Thus, I added (back?) the line `load("cfitsio/3450")` in the file `/pawsey/mwa/software/python3/modulefiles/mwa-voltage/master.lua`.
I'm re-running now, and it appears to be working.
