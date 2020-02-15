# https://scitools.org.uk/cartopy/docs/latest/
# https://blog.algorexhealth.com/2017/09/10-heatmaps-10-python-libraries/
# https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#cartopy-projections
# Cartopy - OSGB, EuroPP

import cartopy.crs as crs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.OSGB())
ax.coastlines()

plt.savefig('gb_coastlines.png')

plt.show()