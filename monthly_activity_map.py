import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as ticker
import csv

col_names = ['Year', 'Month', 'Count']
activity_data = pd.read_csv('activity_counts.csv', header=None, names=col_names) 

activity_matrix = activity_data.pivot('Month', 'Year', 'Count')
print(activity_matrix)

fig, ax = plt.subplots(figsize=(6, 8))
heatplot = plt.imshow(activity_matrix, cmap='YlOrRd')
xticks = [0, 2016, 2017, 2018, 2019, 2020]
yticks = [i for i in range(0, 13)]
ax.set_xticklabels(xticks)
ax.set_yticklabels(yticks)

ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1))
ax.set_title("Garmin Activity Count - Monthly Variation\n As of June 22nd")
ax.set_xlabel('Year')
ax.set_ylabel('Month')

plt.colorbar()
plt.tight_layout()
plt.savefig('monthly_activity_count.png')
plt.show()