import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns


def plot_evolutionary_SSP(wavelength, gb_flux, ms_flux, rhb_flux, bs_flux, bhb_flux, ehb_flux, path):
    fig, axt = plt.subplots(sharex=True, figsize=(10,5), tight_layout=True)
 
    axt.plot(wavelength, np.log10(gb_flux), c='#009988',label='Giant Branches', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(ms_flux), c='#EE7733',label='Main Sequence', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(rhb_flux), c='#CC3311',label='Red Horizontal Branch', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(bs_flux), c='#0077BB',label='Blue Straggler', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(bhb_flux), c='#33BBEE',label='Blue Horizontal Branch', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(ehb_flux), c='#EE3377',label='Extreme Horizontal Branch', linestyle='-', linewidth=3)
    #plt.legend(handlelength=1.25, fontsize=16, loc='lower left')
    plt.title("", fontsize=30)
    plt.ylabel(r'$\log$ Flux [erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]', fontsize=20)
    plt.xlabel(r'Wavelength [\AA]', fontsize=20)
    axt.set_xlim(1050,9050)
    axt.set_ylim(-9.05,-5.25)   
    plt.minorticks_on()
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True)
    plt.savefig(path+'evolutionary_phases.png', dpi=300, bbox_inches = 'tight')
