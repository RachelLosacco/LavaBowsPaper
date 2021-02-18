#
# Showing the compound peaks in the 55 Cnc e orbit
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from astropy.io import ascii
import astropy.units as u

comp = pd.read('../Data/compounds.ecsv')

# Read in the data
data = np.genfromtxt('../Data/PeaksInOrbit.dat')
ttot = data[:,0]
Itot = data[:,1]

# Plotting
for row in range(len(comp)):
    plt.plot([comp['Time of Peak'][row].value, comp['Time of Peak'][row].value],
             [min(Itot), max(Itot)], label=comp['Names'][row])
plt.plot(ttot, Itot, 'k-')
plt.xlabel('Time (days)')
plt.ylabel('Flux')
plt.legend()
plt.title('Intensity of 55 Cnc e, with rainbow peaks\n')
plt.savefig('PeaksinOrbit.png')
plt.show()
plt.close()
