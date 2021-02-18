# Make curves from MIECODE Results
# For various compounds at various wavelengths

import numpy as np
import matplotlib.pyplot as plt

complist = ['KCl', 'KF', 'MgO', 'NaCl', 'NaF']  # Compounds
wavelength = ['400', '550', '800']              # Wavelengths in nm
dropsize = ['02', '10', '50']                   # Droplet sizes in um

for chem in complist:
    dirname = '../Data/MIECODEResults/'+chem
    flux = []
    dop = []
    for wave in wavelength:
        for r in dropsize:
            file = dirname+'/mie.out'+wave+'nm'+r+'um'
            data = np.genfromtxt(file)
            flux.append(data[:,2])
            dop.append(data[:,-1])
    angle = data[:,0]

    # Plot flux vs. angle
    plt.plot(angle, flux[0], 'b:', alpha=0.4, label='400nm, 2$\mu$m')
    plt.plot(angle, flux[1], 'b--', alpha=0.4, label='400nm, 10$\mu$m')
    plt.plot(angle, flux[2], 'b-', label='400nm, 50$\mu$m')
    plt.plot(angle, flux[3], 'g:', alpha=0.4, label='550nm, 2$\mu$m')
    plt.plot(angle, flux[4], 'g--', alpha=0.4, label='550nm, 10$\mu$m')
    plt.plot(angle, flux[5], 'g-', label='550nm, 50$\mu$m')
    plt.plot(angle, flux[6], 'r:', alpha=0.4, label='800nm, 2$\mu$m')
    plt.plot(angle, flux[7], 'r--', alpha=0.4, label='800nm, 10$\mu$m')
    plt.plot(angle, flux[8], 'r-', label='800nm, 50$\mu$m')
    plt.legend(bbox_to_anchor=(1., 1.))
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Flux')
    plt.yscale('log')
    plt.title('Flux for '+chem)
    plt.savefig('../Figures/MIECODEResults/'+chem+'flux.png', bbox_inches='tight')
    plt.close()

    # Plot DoP vs. angle
    plt.plot(angle, dop[0], 'b:', alpha=0.4, label='400nm, 2$\mu$m')
    plt.plot(angle, dop[1], 'b--', alpha=0.4, label='400nm, 10$\mu$m')
    plt.plot(angle, dop[2], 'b-', label='400nm, 50$\mu$m')
    plt.plot(angle, dop[3], 'g:', alpha=0.4, label='550nm, 2$\mu$m')
    plt.plot(angle, dop[4], 'g--', alpha=0.4, label='550nm, 10$\mu$m')
    plt.plot(angle, dop[5], 'g-', label='550nm, 50$\mu$m')
    plt.plot(angle, dop[6], 'r:', alpha=0.4, label='800nm, 2$\mu$m')
    plt.plot(angle, dop[7], 'r--', alpha=0.4, label='800nm, 10$\mu$m')
    plt.plot(angle, dop[8], 'r-', label='800nm, 50$\mu$m')
    plt.legend(bbox_to_anchor=(1., 1.))
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Degree of Polarization')
    plt.title('Degree of Polarization for '+chem)
    plt.savefig('../Figures/MIECODEResults/'+chem+'dop.png', bbox_inches='tight')
    plt.close()
