from astroquery.ned import Ned
import astropy.units as u
result_table = Ned.query_region("Abell 399", radius=180 * u.arcmin)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = result_table.to_pandas()

df

df2=df.dropna()
df2

#%matplotlib notebook
#plt.plot(df2['RA(deg)'], df2['DEC(deg)'], 'bo')
#plt.show()


#%matplotlib notebook
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df2['RA(deg)'], df2['Redshift'],df2['DEC(deg)'], marker='.')
ax.set_xlabel('RA')
ax.set_ylabel('Z')
ax.set_zlabel('DEC')
ax.set_xlim([43, 46])
ax.set_ylim([0.05, 0.1])
ax.set_zlim([12, 15])


plt.show()
