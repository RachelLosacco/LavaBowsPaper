# Plotting 2D faces, output from pixx

import numpy as np
import matplotlib.pyplot as plt

in_dir = '../Data/Plotting2DData/'
out_dir = '../Figures/'
# Plug in whatever compound, wavelength, and angle you want to plot
comp = 'MgO'
wave = 400
angle = 23
pol = ['Q', 'U', 'V']

name = in_dir+comp+'_'+str(wave)+'_0'+str(angle)+'_F.dat'
infile = np.genfromtxt(name)
x = infile[:,0]
y = infile[:,1]
flux = infile[:,2]
plt.scatter(x, y, c=flux)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.text(-1.2, 0.85, 'I', fontsize=20)
plt.axis('equal')
plt.colorbar(label='Intensity', format='%.0e')
plt.savefig(out_dir+comp+'_'+str(wave)+'_0'+str(angle)+'_F.png')
# plt.show()
plt.close()

for i in pol:
    name = in_dir+comp+'_'+str(wave)+'_0'+str(angle)+'_'+i+'.dat'
    infile = np.genfromtxt(name)
    x = infile[:,0]
    y = infile[:,1]
    flux = infile[:,2]

    plt.scatter(x, y, c=abs(flux))
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.text(-1.2, 0.85, i, fontsize=20)
    plt.axis('equal')
    plt.colorbar(label='Intensity', format='%.0e')
    plt.clim(0.00003, 0)
    plt.savefig(out_dir+comp+'_'+str(wave)+'_0'+str(angle)+'_'+i+'.png')
#     plt.show()
    plt.close()