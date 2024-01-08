import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from matplotlib import gridspec

def plot_ssp_compare(wavelength_ssp, base_flux, bs_flux, bhb_flux, ehb_flux, all_flux,
                      output_file_name):

    figa, (ax1,ax1R) = plt.subplots(2,1,sharex=True, figsize=(14,8), tight_layout=True)
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax1R= plt.subplot(gs[1])

    ax1.plot(wavelength_ssp,base_flux/1e-5,label='Base = MS + GB + RHB', c='#555555',zorder=1, linestyle='-',linewidth=3)
    ax1.plot(wavelength_ssp,  bs_flux/1e-5,  label='Base + BS', c='#0077BB',zorder=10, linestyle='-.',  linewidth=3)
    ax1.plot(wavelength_ssp, ehb_flux/1e-5, label='Base + EHB', c='#EE3377',zorder=100, linestyle=':',linewidth=3)
    ax1.plot(wavelength_ssp, bhb_flux/1e-5, label='Base + BHB', c='#33BBEE',zorder=100, linestyle='--', linewidth=3)
    ax1.plot(wavelength_ssp, all_flux/1e-5, label='SSP All', c='black',zorder=1, linestyle='-',  linewidth=3)
    ax1.set_ylim(-0.02,.61)
    ax1.set_xlim(1050,9000)
    ax1.set_ylabel(r'Flux [10$^{-5}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]', fontsize=20)
    ax1.legend(handlelength=2.14, fontsize=14, loc='lower right')
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=20,\
                    bottom=True, top=True, left=True, right=True)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=20, \
                    bottom=True, top=True, left=True, right=True)
    ax1.set_xticklabels([])

    ax1R.set_xlim(1050,9000)
    ax1R.set_ylim(-0.01,.22)
    ax1R.axhline(y=0.0, linestyle='-', c='#555555', linewidth=3)
    ax1R.plot(wavelength_ssp, (all_flux-base_flux)/1e-5, label='BS+BHB+EHB',linestyle='-',c='black', linewidth=3)
    ax1R.plot(wavelength_ssp, (bhb_flux-base_flux)/1e-5, label='BHB', linestyle='--',c='#33BBEE',linewidth=3)
    ax1R.plot(wavelength_ssp, (ehb_flux-base_flux)/1e-5, label='EHB', linestyle=':',c='#EE3377',linewidth=3)
    ax1R.plot(wavelength_ssp,  (bs_flux-base_flux)/1e-5, label='BS', linestyle='-.',c='#0077BB',linewidth=3)
    ax1R.set_xlabel(r'Wavelength [\texttt{\AA}]', fontsize=20)
    ax1R.set_ylabel(r'Residuals', fontsize=20)
    ax1R.legend(handlelength=2.34, fontsize=13, loc='upper right')
    ax1R.minorticks_on()
    ax1R.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=20, \
                    bottom=True, top=True, left=True, right=True)
    ax1R.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=20, \
                    bottom=True, top=True, left=True, right=True)
    ax1R.yaxis.label.set_size(18)
    ax1R.xaxis.label.set_size(18)

    plt.savefig(output_file_name+'ssp_comparing_R250.png',
                dpi=300, bbox_inches = 'tight')
