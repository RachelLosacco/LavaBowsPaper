#
# Plot semi-major axis vs. mass for exoplanets
#

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('../Data/planets_Mva.csv', delimiter=',')
M = data[:,0]
a = data[:,1]
method = np.loadtxt('../Data/planets_Mva.csv', dtype=str, delimiter=',')[:,2]

# 55 Cnc e
a_55 = 0.01544
M_55 = 0.027383

# Include planets from the solar system
names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
mass = [1.7391e-4, 0.0025644, 0.00314645, 3.3807e-4, 1.0, 0.29942, 0.045734,
        0.053955] # Jupiter mass
orbit = [0.387098, 0.723332, 1.0, 1.523679, 5.2044, 9.5826, 19.2184, 30.11] # AU

a_RV = []
M_RV = []
a_Transit = []
M_Transit = []
a_Timing = []
M_Timing = []
a_Micro = []
M_Micro = []
a_Imag = []
M_Imag = []
a_other = []
M_other = []

for i in range(len(method)):
    if method[i] == 'RV':
        a_RV.append(a[i])
        M_RV.append(M[i])
    elif method[i] == 'Transit':
        a_Transit.append(a[i])
        M_Transit.append(M[i])
    elif method[i] == 'Timing':
        a_Timing.append(a[i])
        M_Timing.append(M[i])
    elif method[i] == 'Microlensing':
        a_Micro.append(a[i])
        M_Micro.append(M[i])
    elif method[i] == 'Imaging':
        a_Imag.append(a[i])
        M_Imag.append(M[i])
    else:
        a_other.append(a[i])
        M_other.append(M[i])
        print(method[i])

plt.scatter(a_RV, M_RV, s=3, c='y', alpha=0.6, label='Radial Velocity')
plt.scatter(a_Transit, M_Transit, s=3, c='r', alpha=0.5, label='Transit')
# plt.scatter(a_Timing, M_Timing, s=3, c='g', label='Transit Timing Variaitons')
plt.scatter(a_Imag, M_Imag, s=3, c='b', alpha=0.6, label='Imaging')
plt.scatter(orbit, mass, marker='+', c='k', label='Solar System')

plt.text(orbit[0]-0.2, mass[0]+0.0001, names[0], color='k', fontsize=13) # Mercury
plt.text(orbit[1]-0.5, mass[1]+0.001, names[1], color='k', fontsize=13)         # Venus
plt.text(orbit[2]+0.1, mass[2]+0.001, names[2], color='k', fontsize=13)   # Earth
plt.text(orbit[3]+0.1, mass[3]+0.0001, names[3], color='k', fontsize=13)  # Mars
plt.text(orbit[4]+0.5, mass[4]+0.4, names[4], color='k', fontsize=13)     # Jupiter
plt.text(orbit[5], mass[5]+0.1, names[5], color='k', fontsize=13)     # Saturn
plt.text(orbit[6]-12, mass[6]-0.02, names[6], color='k', fontsize=13)     # Uranus
plt.text(orbit[7]-13, mass[7]+0.03, names[7], color='k', fontsize=13)     # Neptune

plt.scatter(a_55, M_55, marker='x', c='k')    # 55 Cnc e
plt.text(a_55-0.01, M_55+0.015, '55 Cnc e', fontweight='bold')

plt.scatter(0.0527, 0.47, marker='x', c='k')    # 51 Pegasi b
plt.text(0.0527-0.045, 0.47-0.2, '51 Pegasi b', fontweight='bold')

plt.xlabel('Semi-major axis [AU]')
plt.ylabel('Mass [Jupiter Mass]')
plt.ylim(min(mass), max(M)+3)
plt.xlim(min(a), max(a)-10)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.savefig('../Figures/planets_Mva.png')
plt.show()
plt.close()
