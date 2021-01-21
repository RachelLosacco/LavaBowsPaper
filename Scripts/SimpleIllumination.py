#
# Two ways to get a simple lightcurve
#
import matplotlib.pyplot as plot
import astropy.units as u
import numpy as np

### METHOD 1 ###
# Bead Illumination
# Equation describing illuminated area of planet as a function of angle/phase

# Functions
def beadil(x):
    '''
    Illumination of planet throughout orbit
    When angle = 0, illumination I = 0
    When angle = pi, illumination I = 1
    Angle x in radians
    '''
    I = np.sin(x/2)**2
    return I

def reflect(A, g, R, a):
    '''
    How much light is reflected towards us? Planet-to-star flux ratio
    A = albedo
    g(theta) = phase angle from beadil
    R = radius
    a = semi-major axis

    '''
    ratio = A*g*(R/a)**2
    return ratio

def lightcurve1(A, t, P, r, a):
    '''
    Putting beadil and reflect together
    t = time in orbit
    P = period of planet
    '''
    orbit = t/P
    theta = (orbit.decompose() * 2*np.pi) * u.rad
    illum = beadil(theta)
    ratio = reflect(A, illum, r, a)
    return ratio

# For calling subroutines into other python scripts, separate the subrountines from
# the rest of the python script by doing the following:
if __name__=="__main__":
    # Now everything below will run if it's called by the terminal,
    # but it will NOT run when imported by an external python file
    # For 55 Cnc e
    A = 0.3
    R = 2.04 * u.R_earth
    a = 0.016 * u.au
    g = 1 #assume full phase
    P = 0.736 * u.day
    t = np.linspace(0, 1)*u.day

    flux_ratio = lightcurve1(A, t, P, R, a).decompose()

    # flux from 55 Cnc (star)
    L = 0.589 * u.L_sun
    d = 41 * u.lyr
    f = L/(4*np.pi*d**2)

    I = f + f*flux_ratio
    plt.plot(t,I)
    plt.xlabel('Time (days)')
    plt.ylabel('Flux')
    plt.title('Lightcurve from 55 Cnc A and e')
    plt.savefig('../Figures/SimpleLightcurve1.png')
    plt.show()


# Functions
def lightcurve2(A, t, P, r, a):
    '''Putting beadil and reflect together
    gives ratio of light added to lightcurve from planet
    A = albedo
    t = time in orbit
    P = period of planet
    r = planet radius
    a = semi-major axis'''
    orbit = t/P
    theta = (orbit.decompose() * 2.*np.pi)*u.rad
    illum = beadil(theta)
    ratio = reflect(A, illum, r, a)
    return ratio

# For 55 Cnc e
A = 0.3
R = 2.04*u.R_earth
a = 0.016*u.au
g = 1 #assume full phase
P = 0.736*u.day
t = np.linspace(0,P.value)*u.day

flux_ratio = lightcurve2(A, t, P, R, a).decompose()

# flux from 55 Cnc (star)
L = 0.589*u.L_sun
d = 41*u.lyr
star_flux = L/(4.*np.pi*d**2.)

# flux from 55 Cnc + 55 Cnc e
system_I = star_flux + star_flux*flux_ratio

# Plotting
plt.plot(t, system_I)
plt.xlabel('Time (days)')
plt.ylabel('Flux')
plt.title('Lightcurve from 55 Cnc A and e\n')
plt.savefig('../Figures/SimpleLightcurve2.png')
# plt.show()
plt.close()
