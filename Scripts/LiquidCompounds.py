#
# Temperature of compounds when they are liquid
# Including refractive index as y-axis
#
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import pandas as pd

# Functions
def phase(n):
    '''Scattering angle from Bailey(2007)
    Phase angle, complimentary to rainbow angle
    Dependent on refractive index n (unitless)'''
    # Rainbow angle
    x = np.sqrt((4-n**2)/3)
    theta = np.pi + (2*np.arcsin(x)) - (4*np.arcsin(x/n))
    # Phase angle
    phi = np.pi - theta
    return phi

def df_phase(row):
    '''Phase from refractive index
    For dataframe'''
    return phase(row['Refractive Index'])

# Temperatures [K] for 55 Cnc e
equ_temp = 1517  # equilibrium
day_temp = 2697  # day side
night_temp = 1376 # night side

# Table of rock-forming compounds
info = {'Names':['KCl', 'KF', 'KOH', 'MgO', 'NaCl', 'NaF', 'NaOH', 'SiO', 'SiO2']}
comp = pd.DataFrame(data=info)
comp['Refractive Index'] = [1.4927, 1.3632, 1.4090, 1.7405, 1.5469, 1.3261, 1.3576, 1.7369, 1.5384]
comp['Melting'] = [770.0, 858.0, 360.0, 2825.0, 800.7, 993.0, 318.0, 1702.0, 1713.0]*u.C
comp['Boiling'] = [1420.0, 1502.0, 1327.0, 3600.0, 1465.0, 1704.0, 1388.0, 1880.0, 2950.0] * u.C
comp['Phase angle'] = comp.apply(df_phase, axis=1)
comp['Chromatic Dispersion'] = [-0.056254, -0.018988, np.nan, -0.071378, -0.064713, -0.018955, np.nan, 6.8718, -1.0916] * u.micron

n_min = min(comp['Refractive Index'])
n_max = max(comp['Refractive Index'])

# Plotting
# Horizontal compound lines
plt.hlines(comp['Refractive Index'], comp['Melting'], comp['Boiling'])
for row in range(len(comp)):
    plt.text(comp['Melting'][row], comp['Refractive Index'][row]+0.01, comp['Names'][row])

# 55 Cnc
plt.plot([equ_temp, equ_temp], [n_min-0.1, n_max+0.1], 'b--', zorder=1, alpha=0.7, label='Equil. Temp.')
plt.fill_betweenx([n_min-0.1, n_max+0.1], night_temp, day_temp, color='b', alpha=0.4)

#Extra
plt.xlabel('Temperature (K)')
plt.ylabel('Refractive Index $n$')
plt.ylim(n_min-0.1, n_max+0.1)
plt.title('Temperature with Liquid Compounds')
plt.legend(loc='upper left')
plt.savefig('../Figures/TempofPlanetsandComp.png')
# plt.show()
plt.close()
