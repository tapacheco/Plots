import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import rc
import numpy as np
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from matplotlib import gridspec

def plot_ssp(wavelength_ssp, flux_ssp, index_ssp,\
             schi05_w_m2, schi05_flux, index_S, \
             iue1_w_m2, iue1_flux, iue1_sigma, index1, \
             iue2_w_m2, iue2_flux, iue2_sigma, index2, \
             iue3_w_m2, iue3_flux, iue3_sigma, index3, \
             path):
    fig, axt = plt.subplots(sharex=True, figsize=(10,5), tight_layout=True)
    plt.minorticks_on()
    flux_1 = (iue1_flux/iue1_flux[index1])
    flux_3 = (iue3_flux/iue3_flux[index3])
    flux_2 = (iue2_flux/iue2_flux[index2])
    sig1 = np.array(iue1_sigma/iue1_flux[index1])
    sig3 = np.array(iue3_sigma/iue3_flux[index3])
    sig2 = np.array(iue2_sigma/iue2_flux[index2])
#    
    plt.plot(iue1_w_m2, np.log10(flux_1), label='IUE lr12220',  c='#DDAA33', linestyle='-', linewidth=3, alpha=.9)
    plt.plot(iue3_w_m2, np.log10(flux_3), label='IUE sp15885',  c='#004488', linestyle='-', linewidth=3, alpha=.9)
    plt.plot(iue2_w_m2, np.log10(flux_2), label='IUE sp10171',  c='#BB5566', linestyle='-', linewidth=3, alpha=.9)
    plt.plot(schi05_w_m2, np.log10(schi05_flux/schi05_flux[index_S]), label='Schiavon+04',  c='grey', alpha=.9, linestyle='-', linewidth=3)
    axt.plot(wavelength_ssp, np.log10(flux_ssp/flux_ssp[index_ssp]), label='Modeled SSP', c='#ff00ff', linestyle='--', linewidth=3)

    axt.fill_between(iue1_w_m2, np.log10(flux_1-sig1), np.log10(flux_1+sig1), color='#DDAA33', alpha=.35)
    axt.fill_between(iue3_w_m2, np.log10(flux_3-sig3), np.log10(flux_3+sig3), color='#004488', alpha=.35)
    axt.fill_between(iue2_w_m2, np.log10(flux_2-sig2), np.log10(flux_2+sig2), color='#BB5566', alpha=.35)
    axt.set_xlim(min(iue2_w_m2)-10,max(schi05_w_m2+10))
    axt.set_ylim(-1.16,1.16)
    plt.legend(handlelength=1.5, fontsize=16, loc='best')
    plt.ylabel(r'$\log$ Flux [erg cm$^{-2}$ s$^{-1}$ \AA $^{-1}$]', fontsize=16)
    plt.xlabel(r'Wavelength [\AA]', fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True)
    plt.savefig(path+'_iue+ssp.png', dpi=300, bbox_inches = 'tight')
