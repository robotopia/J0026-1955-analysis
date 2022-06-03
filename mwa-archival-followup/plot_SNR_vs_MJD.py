import numpy as np
import matplotlib.pyplot as plt
import csv

# Read in the necessary fields
with open('follow-up.csv', newline='') as csvfile:
    try:
        rows = csv.reader(csvfile)
    except IOError:
        print("Couldn't read file as CSV")

    # Line 0 is just column headers, and line 38 is the last actual data line
    string_data = [[row[0], row[4],   row[7], row[9], row[11]]  for row in rows][1:38]
    #               ^       ^         ^       ^       ^
    #               obsids  durations freqs   snrs    notes

# Convert the relevant values to a dictionary of numpy arrays
GPSref = 1231718418 # MDJ 58500
data = {
         "MJDs_since_58500": np.array([(int(string_data[i][0]) - GPSref)/86400 for i in range(len(string_data))]),
         "durations_secs":   np.array([int(string_data[i][1]) for i in range(len(string_data))]),
         "freq_ctr_MHz":     np.array([float(string_data[i][2]) for i in range(len(string_data))]),
         "SNRs":             np.array([float(string_data[i][3]) if string_data[i][3] != '' else None for i in range(len(string_data))]),
         "notes":            np.array([string_data[i][4] for i in range(len(string_data))])
       }

# Make a plot!
plt.plot( data["MJDs_since_58500"], data["SNRs"], 'o' )

# Add the upper limits for the non-detections
nondetection_SNR = np.array([3.0 if note == 'No detection' else np.nan for note in data["notes"]])
plt.errorbar( data["MJDs_since_58500"], nondetection_SNR, yerr=0.5, uplims=1, fmt="." )

plt.xlabel("MJD - 58500")
plt.ylabel("S/N of detection")
plt.show()
