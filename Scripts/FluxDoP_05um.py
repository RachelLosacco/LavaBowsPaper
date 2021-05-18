# Make curves from MIECODE Results
# For various compounds at 0.5um

import numpy as np
import matplotlib.pyplot as plt

complist = ['KCl', 'KF', 'MgO', 'NaCl', 'NaF']  # Compounds
wavelength = ['400', '550', '800']              # Wavelengths in nm
# ALL IN 0.5um

for chem in complist:
    dirname = '../Data/MIECODEResults/'+chem
    flux = []
    dop = []
    for wave in wavelength:
        file = dirname+'/mie.out'+wave
        data = np.genfromtxt(file)
        flux.append(data[:,2])
        dop.append(data[:,-1])
    angle = 180 - data[:,0]

    # Flux vs. angle
    plt.plot(angle, flux[0], 'b-', label='400nm')
    plt.plot(angle, flux[1], 'g-', label='550nm')
    plt.plot(angle, flux[2], 'r-', label='800nm')
    plt.legend(bbox_to_anchor=(1., 1.))
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Flux')
    plt.yscale('log')
    plt.title('Flux for '+chem)
    plt.savefig('../Figures/MIECODEResults/'+chem+'flux.png', bbox_inches='tight')
    plt.show()
    plt.close()
    
    # DoP vs. angle
    plt.plot(angle, dop[0], 'b-', label='400nm')
    plt.plot(angle, dop[1], 'g-', label='550nm')
    plt.plot(angle, dop[2], 'r-', label='800nm')
    plt.legend(bbox_to_anchor=(1., 1.))
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Degree of Polarization')
    plt.title('Degree of Polarization for '+chem)
    plt.savefig('../Figures/MIECODEResults/'+chem+'dop.png', bbox_inches='tight')
    plt.show()
    plt.close()