# Make curves from MIECODE Results
# For various compounds at various wavelengths
# JUST MgO 50 um

import numpy as np
import matplotlib.pyplot as plt

dirname = '../Data/MIECODEResults/MgO'
r = '50'

wavelength = ['400', '550', '800']              # Wavelengths in nm
flux = []
dop = []
for wave in wavelength:
    file = dirname+'/mie.out'+wave+'nm'+r+'um'
    data = np.genfromtxt(file)
    flux.append(data[:,2])
    dop.append(data[:,-1])

# Plot flux vs. angle
plt.plot(angle, flux[0], 'b-', label='400nm')
plt.plot(angle, flux[1], 'g-', label='550nm')
plt.plot(angle, flux[2], 'r-', label='800nm')
plt.axvline(x=30, ymin=min(flux[0]), ymax=max(flux[0]), color='k', linestyle='--', alpha=0.5)
plt.axvline(x=70, ymin=min(flux[0]), ymax=max(flux[0]), color='k', linestyle='--', alpha=0.5)
plt.legend(bbox_to_anchor=(0.9, 1.))
plt.xlabel('Angle (degrees)')
plt.ylabel('Flux')
plt.yscale('log')
plt.title('Flux for MgO')
plt.savefig('../Figures/MIECODEResults/MgO'+r+'flux2.png', bbox_inches='tight')
plt.close()

# Plot DoP vs. angle
plt.plot(angle, dop[0], 'b-', label='400nm')
plt.plot(angle, dop[1], 'g-', label='550nm')
plt.plot(angle, dop[2], 'r-', label='800nm')
plt.axvline(x=30, ymin=min(flux[0]), ymax=max(flux[0]), color='k', linestyle='--', alpha=0.5)
plt.axvline(x=70, ymin=min(flux[0]), ymax=max(flux[0]), color='k', linestyle='--', alpha=0.5)
plt.legend(bbox_to_anchor=(1., 1.))
plt.xlabel('Angle (degrees)')
plt.ylabel('Degree of Polarization')
plt.title('Degree fo Polarization for MgO')
plt.savefig('../Figures/MIECODEResults/MgO'+r+'dop2.png', bbox_inches='tight')
plt.close()

# Zoom in of flux between 20 adn 40 degrees
plt.plot(angle, flux[0], 'b-', label='400nm')
plt.plot(angle, flux[1], 'g-', label='550nm')
plt.plot(angle, flux[2], 'r-', label='800nm')
plt.axvline(x=32, ymin=10e-3, ymax=10, color='r', linestyle='--', alpha=0.5)
plt.axvline(x=30, ymin=10e-3, ymax=10, color='g', linestyle='--', alpha=0.5)
plt.axvline(x=29, ymin=10e-3, ymax=10, color='b', linestyle='--', alpha=0.5)
plt.xlim(20,40)
plt.ylim(10e-3, 10)
plt.legend(bbox_to_anchor=(1., 1.))
plt.xlabel('Angle (degrees)')
plt.ylabel('Flux')
plt.yscale('log')
plt.title('Flux for '+chem)
plt.savefig('../Figures/MIECODEResults/MgO'+r+'dop3.png', bbox_inches='tight')
plt.close()
