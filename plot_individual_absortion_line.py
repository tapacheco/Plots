import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from matplotlib import gridspec

def plot_ssp_lines(base_ssp, bs_ssp, bhb_ssp, ehb_ssp, total_ssp,
                   output_file_name, Ha):

    figa, (ax1,ax1R) = plt.subplots(2,1,sharex=True, figsize=(10,5), tight_layout=True)
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax1R= plt.subplot(gs[1])

    ax1.plot( base_ssp['wavelength'], base_ssp['flux']/1e-5, c='#000000',linestyle='-', linewidth=3)
    ax1.plot(   bs_ssp['wavelength'],   bs_ssp['flux']/1e-5, c='#0077BB',linestyle='-.', linewidth=3)
    ax1.plot(  bhb_ssp['wavelength'],  ehb_ssp['flux']/1e-5, c='#EE3377',linestyle=':', linewidth=3)
    ax1.plot(  ehb_ssp['wavelength'],  bhb_ssp['flux']/1e-5, c='#33BBEE',linestyle='--', linewidth=3)
    ax1.plot(total_ssp['wavelength'],total_ssp['flux']/1e-5, c='#BBBBBB',linestyle='-', linewidth=3)
    ax1.set_xlim(Ha-5, Ha+5)
    ax1.set_ylim(-0.6, -0.05)
    ax1.set_ylabel(r'Flux [10$^{-5}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]', fontsize=16)
    ax1.legend(handlelength=2.14, fontsize=14, loc='lower right')
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=16,\
                    bottom=True, top=True, left=True, right=True)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=16, \
                    bottom=True, top=True, left=True, right=True)
    ax1.set_xticklabels([])

    ax1R.set_xlim(Ha-5, Ha+5)
    ax1R.set_ylim(-0.01,.22)
    ax1R.axhline(y=0.0, linestyle='-', c='#555555', linewidth=3)
    #ax1R.plot(   bs_ssp['wavelength'], (   bs_ssp['flux']-base_ssp['flux'])/1e-5, label='BS',linestyle='-',c='000000', linewidth=3)
    #ax1R.plot(  bhb_ssp['wavelength'], (  bhb_ssp['flux']-base_ssp['flux'])/1e-5, label='BHB',c='#EE3377',linestyle=':', linewidth=3)
    #ax1R.plot(  ehb_ssp['wavelength'], (  ehb_ssp['flux']-base_ssp['flux'])/1e-5, label='EHB',c='#33BBEE',linestyle='--',linewidth=3)
    #ax1R.plot(total_ssp['wavelength'], (total_ssp['flux']-base_ssp['flux'])/1e-5, label='All', c='#BBBBBB',linestyle='-', linewidth=3)
    ax1R.set_xlabel(r'Wavelength [\texttt{\AA}]', fontsize=16)
    ax1R.set_ylabel(r'Residuals', fontsize=16)
    ax1R.legend(handlelength=2.34, fontsize=12, loc='upper right')
    ax1R.minorticks_on()
    ax1R.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=16, \
                    bottom=True, top=True, left=True, right=True)
    ax1R.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=16, \
                    bottom=True, top=True, left=True, right=True)
    ax1R.yaxis.label.set_size(18)
    ax1R.xaxis.label.set_size(18)

    plt.savefig(output_file_name+'ssp_absortion_line.png', dpi=300, bbox_inches = 'tight')
