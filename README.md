# Drifting analysis on J0024-1956

## Using Drift Analysis software

The software used for this analysis is [DriftAnalysis](https://github.com/robotopia/drift_analysis)

If starting a new analysis, this can be run on a "pdv" file (i.e. a text file containing the output of PSRCHIVE's pdv utility) as follows:

    python drift_analysis.py <pdv_file> <stokes>
    
where "stokes" is one of (I,Q,U,V)

The program uses the JSON format to save out the analyses to file. If such a file has been saved, it can be loaded directly from the command line using

    python drift_analysis.py <json_file>

## Timeline

* 2022-02-14: Started downloading 1275094456 (JobID: 560934)
* 2022-02-14: Started downloading 1275172216 (JobID: 253238)
