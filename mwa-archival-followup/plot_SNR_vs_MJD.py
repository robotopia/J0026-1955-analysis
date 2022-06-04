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
uplim = 3.0 # Upper limit for non-detection
data = {
         "MJDs_since_58500": np.array([(int(string_data[i][0]) - GPSref)/86400 for i in range(len(string_data))]),
         "durations_secs":   np.array([int(string_data[i][1]) for i in range(len(string_data))]),
         "freq_ctr_MHz":     np.array([float(string_data[i][2]) for i in range(len(string_data))]),
         "sigmas":           np.array([float(string_data[i][3]) if string_data[i][3] != '' else np.nan for i in range(len(string_data))]),
         "notes":            np.array([string_data[i][4] for i in range(len(string_data))])
       }

# Make a plot!
# Split the plot into three segments, with broken x axis
fig, axs = plt.subplots(1, 3, sharey=True)
fig.subplots_adjust(wspace=0.05)

freq_colors = { 97.92: "r", 139.52: "y", 154.24: "g", 184.96: "b" }
facecolors = [freq_colors[freq_MHz] for freq_MHz in data["freq_ctr_MHz"]]
for ax in axs:
    ax.scatter( data["MJDs_since_58500"], data["sigmas"], s=data["durations_secs"]/30, facecolors=facecolors, edgecolors='k', zorder=2 )

print(data["freq_ctr_MHz"], data["sigmas"], data["MJDs_since_58500"])

# Plot the upper limits for the non-detections
nondetection_sigmas = np.array([uplim if note == 'No detection' else np.nan for note in data["notes"]])
for ax in axs:
    ax.errorbar( data["MJDs_since_58500"], nondetection_sigmas, yerr=0.5, uplims=1, fmt=".", zorder=1 )

axs[1].set_xlabel("MJD - 58500") # The middle x-axis
axs[0].set_ylabel("PRESTO detection significance, $\\sigma$") # The left y-axis

axs[0].set_xlim([-600,0])
axs[1].set_xlim([480,550])
axs[2].set_xlim([580,730])

axs[0].spines.right.set_visible(False)
axs[1].spines.left.set_visible(False)
axs[1].spines.right.set_visible(False)
axs[2].spines.left.set_visible(False)

axs[1].tick_params(left=False)
axs[2].yaxis.tick_right()

d = 2  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
axs[0].plot([1, 0], [1, 1], transform=axs[0].transAxes, **kwargs)
axs[1].plot([0, 0], [0, 1], transform=axs[1].transAxes, **kwargs)

plt.show()
