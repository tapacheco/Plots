import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from matplotlib import gridspec

def plot_ssp_lines(base_ssp, index_ssp_base, 
                   bs_ssp, index_ssp_bs,  
                   bhb_ssp, index_ssp_bhb, 
                   ehb_ssp, index_ssp_ehb,
                   total_ssp,index_ssp_total,
                   output_file_name, Ha):

    figa, (ax1,ax1R) = plt.subplots(2,1,sharex=True, figsize=(10,5), tight_layout=True)
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax1R= plt.subplot(gs[1])

    ax1.plot(total_ssp['wavelength'],total_ssp['flux']/total_ssp['flux'][index_ssp_total], c='black',   label='All', linestyle='-', linewidth=3)
    ax1.plot( base_ssp['wavelength'], base_ssp['flux']/base_ssp['flux'][index_ssp_base] , c='#555555', label='base', linestyle='-', linewidth=3)
    ax1.plot(   bs_ssp['wavelength'],   bs_ssp['flux']/bs_ssp['flux'][index_ssp_bs], c='#0077BB', label='BS', linestyle='-.', linewidth=3)
    ax1.plot(  bhb_ssp['wavelength'],  bhb_ssp['flux']/bhb_ssp['flux'][index_ssp_bhb], c='#33BBEE', label='BHB', linestyle=':', linewidth=3)
    ax1.plot(  ehb_ssp['wavelength'],  ehb_ssp['flux']/ehb_ssp['flux'][index_ssp_ehb], c='#EE3377', label='EHB',  linestyle='--', linewidth=3)
    ax1.set_xlim(Ha-50, Ha+50)
    ax1.set_ylim(0.26, 1.09)
    ax1.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ \texttt{\AA}$^{-1}$]', fontsize=16)
    ax1.legend(fontsize=16, loc='lower right')
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=16,\
                    bottom=True, top=True, left=True, right=True)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=16, \
                    bottom=True, top=True, left=True, right=True)
    ax1.set_xticklabels([])

    ax1R.set_xlim(Ha-50, Ha+50)
    ax1R.set_ylim(-0.03,.14)
    ax1R.axhline(y=0.0, linestyle='-', c='#555555', linewidth=3)
    ax1R.plot(total_ssp['wavelength'], (total_ssp['flux']-base_ssp['flux'])/total_ssp['flux'][index_ssp_base], label='All',c='black', linestyle='-', linewidth=3)
    ax1R.plot(   bs_ssp['wavelength'], (   bs_ssp['flux']-base_ssp['flux'])/bs_ssp['flux'][index_ssp_bs], label='BS', c='#0077BB',linestyle='-',linewidth=3)
    ax1R.plot(  bhb_ssp['wavelength'], (  bhb_ssp['flux']-base_ssp['flux'])/bhb_ssp['flux'][index_ssp_bhb] , label='BHB',c='#33BBEE',linestyle=':', linewidth=3)
    ax1R.plot(  ehb_ssp['wavelength'], (  ehb_ssp['flux']-base_ssp['flux'])/ehb_ssp['flux'][index_ssp_ehb] , label='EHB',c='#EE3377',linestyle='--',linewidth=3)
    ax1R.set_xlabel(r'Wavelength [\texttt{\AA}]', fontsize=16)
    ax1R.set_ylabel(r'Residuals', fontsize=16)
    ax1R.minorticks_on()
    ax1R.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=16, \
                    bottom=True, top=True, left=True, right=True)
    ax1R.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=16, \
                    bottom=True, top=True, left=True, right=True)
    ax1R.yaxis.label.set_size(18)
    ax1R.xaxis.label.set_size(18)

 #   plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(output_file_name+'_ssp_absortion_line_normalized.png', dpi=300)
