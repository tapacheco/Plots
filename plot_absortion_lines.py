import pandas as pd
import numpy as np 

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from seaborn import jointplot

def distance_NaN(valores):
    if isinstance(valores, (list, np.ndarray)):
        distancias_ok = [valor for valor in valores if not (isinstance(valor, float) and np.isnan(valor))]
        return distancias_ok

def plot_absortion_lines(ssp_ngc2808_base, index_base ,  
                         ssp_ngc2808_bs,   index_bs   ,
                         ssp_ngc2808_ehb,  index_ehb  ,
                         ssp_ngc2808_bhb,  index_bhb  , 
                         ssp_ngc2808_total,index_total,
                         path, name):
    Ha = 6562.5
    Hb = 4860.74
    Hc = 4340.1 
    Hd = 4101.2
    Ca = 3951.
    fig, axs = plt.subplots(sharex=False, figsize=(10,15), tight_layout=False,\
                                nrows=3, ncols=2)
 
    axs[0,0].plot( ssp_ngc2808_base['wavelength'],np.log10( ssp_ngc2808_base['flux']/ ssp_ngc2808_base['flux'][index_base ]), c='#BBBBBB',)
    axs[0,0].plot(   ssp_ngc2808_bs['wavelength'],np.log10(   ssp_ngc2808_bs['flux']/   ssp_ngc2808_bs['flux'][index_bs   ]), c='#004488',)
    axs[0,0].plot(  ssp_ngc2808_ehb['wavelength'],np.log10(  ssp_ngc2808_ehb['flux']/  ssp_ngc2808_ehb['flux'][index_ehb  ]), c='#994455',)
    axs[0,0].plot(  ssp_ngc2808_bhb['wavelength'],np.log10(  ssp_ngc2808_bhb['flux']/  ssp_ngc2808_bhb['flux'][index_bhb  ]), c='#997700',)
    axs[0,0].plot(ssp_ngc2808_total['wavelength'],np.log10(ssp_ngc2808_total['flux']/ssp_ngc2808_total['flux'][index_total]), c='#000000',)
    axs[0,0].set_xlim(Ha-5, Ha+5)
    axs[0,0].set_ylim(-0.6, -0.)
    axs[0,0].set_xlabel(r'', fontsize=24)
    axs[0,0].set_ylabel(r'$\log$ Flux [$erg s^{-1} cm^{-2} Hz^{-1}$]', fontsize=24)
    axs[0,0].minorticks_on()
    axs[0,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[0,0].get_yticklabels(), fontsize=24)

    axs[0,1].plot( ssp_ngc2808_base['wavelength'],np.log10( ssp_ngc2808_base['flux']/ ssp_ngc2808_base['flux'][index_base ]), c='#BBBBBB',)
    axs[0,1].plot(   ssp_ngc2808_bs['wavelength'],np.log10(   ssp_ngc2808_bs['flux']/   ssp_ngc2808_bs['flux'][index_bs   ]), c='#004488',)
    axs[0,1].plot(  ssp_ngc2808_ehb['wavelength'],np.log10(  ssp_ngc2808_ehb['flux']/  ssp_ngc2808_ehb['flux'][index_ehb  ]), c='#994455',)
    axs[0,1].plot(  ssp_ngc2808_bhb['wavelength'],np.log10(  ssp_ngc2808_bhb['flux']/  ssp_ngc2808_bhb['flux'][index_bhb  ]), c='#997700',)
    axs[0,1].plot(ssp_ngc2808_total['wavelength'],np.log10(ssp_ngc2808_total['flux']/ssp_ngc2808_total['flux'][index_total]), c='#000000',)
    axs[0,1].set_xlim(Hb-5, Hb+5)
    axs[0,1].set_ylim(-0.6, -0.)
    axs[0,1].set_xlabel(r'', fontsize=24)
    axs[0,1].set_ylabel(r'', fontsize=24)
    axs[0,1].minorticks_on()
    axs[0,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[0,1].get_yticklabels(), fontsize=24)

    axs[1,0].plot( ssp_ngc2808_base['wavelength'],np.log10( ssp_ngc2808_base['flux']/ ssp_ngc2808_base['flux'][index_base ]), c='#BBBBBB',)
    axs[1,0].plot(   ssp_ngc2808_bs['wavelength'],np.log10(   ssp_ngc2808_bs['flux']/   ssp_ngc2808_bs['flux'][index_bs   ]), c='#004488',)
    axs[1,0].plot(  ssp_ngc2808_ehb['wavelength'],np.log10(  ssp_ngc2808_ehb['flux']/  ssp_ngc2808_ehb['flux'][index_ehb  ]), c='#994455',)
    axs[1,0].plot(  ssp_ngc2808_bhb['wavelength'],np.log10(  ssp_ngc2808_bhb['flux']/  ssp_ngc2808_bhb['flux'][index_bhb  ]), c='#997700',)
    axs[1,0].plot(ssp_ngc2808_total['wavelength'],np.log10(ssp_ngc2808_total['flux']/ssp_ngc2808_total['flux'][index_total]), c='#000000',)
    axs[1,0].set_xlim(Hc-5, Hc+5)
    axs[1,0].set_ylim(-0.6, -0.)
    axs[1,0].set_xlabel(r'', fontsize=24)
    axs[1,0].set_ylabel(r'$\log$ Flux [$erg s^{-1} cm^{-2} Hz^{-1}$]', fontsize=24)
    axs[1,0].minorticks_on()
    axs[1,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[1,0].get_yticklabels(), fontsize=24)

    axs[1,1].plot( ssp_ngc2808_base['wavelength'],np.log10( ssp_ngc2808_base['flux']/ ssp_ngc2808_base['flux'][index_base ]), c='#BBBBBB',)
    axs[1,1].plot(   ssp_ngc2808_bs['wavelength'],np.log10(   ssp_ngc2808_bs['flux']/   ssp_ngc2808_bs['flux'][index_bs   ]), c='#004488',)
    axs[1,1].plot(  ssp_ngc2808_ehb['wavelength'],np.log10(  ssp_ngc2808_ehb['flux']/  ssp_ngc2808_ehb['flux'][index_ehb  ]), c='#994455',)
    axs[1,1].plot(  ssp_ngc2808_bhb['wavelength'],np.log10(  ssp_ngc2808_bhb['flux']/  ssp_ngc2808_bhb['flux'][index_bhb  ]), c='#997700',)
    axs[1,1].plot(ssp_ngc2808_total['wavelength'],np.log10(ssp_ngc2808_total['flux']/ssp_ngc2808_total['flux'][index_total]), c='#000000',)
    axs[1,1].set_xlim(Hd-5, Hd+5)
    axs[1,1].set_ylim(-0.6, -0.)
    axs[1,1].set_xlabel(r'', fontsize=24)
    axs[1,1].set_ylabel(r'', fontsize=24)
    axs[1,1].minorticks_on()
    axs[1,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[1,1].get_yticklabels(), fontsize=24)

    axs[2,0].plot( ssp_ngc2808_base['wavelength'],np.log10( ssp_ngc2808_base['flux']/ ssp_ngc2808_base['flux'][index_base ]), c='#BBBBBB',)
    axs[2,0].plot(   ssp_ngc2808_bs['wavelength'],np.log10(   ssp_ngc2808_bs['flux']/   ssp_ngc2808_bs['flux'][index_bs   ]), c='#004488',)
    axs[2,0].plot(  ssp_ngc2808_ehb['wavelength'],np.log10(  ssp_ngc2808_ehb['flux']/  ssp_ngc2808_ehb['flux'][index_ehb  ]), c='#994455',)
    axs[2,0].plot(  ssp_ngc2808_bhb['wavelength'],np.log10(  ssp_ngc2808_bhb['flux']/  ssp_ngc2808_bhb['flux'][index_bhb  ]), c='#997700',)
    axs[2,0].plot(ssp_ngc2808_total['wavelength'],np.log10(ssp_ngc2808_total['flux']/ssp_ngc2808_total['flux'][index_total]), c='#000000',)
    axs[2,0].set_xlim(Ca-30, Ca+30)
    axs[2,0].set_ylim(-0.6, -0.)
    axs[2,0].set_xlabel(r'Wavelength [$\AA$]', fontsize=24)
    axs[2,0].set_ylabel(r'$\log$ Flux [$erg s^{-1} cm^{-2} Hz^{-1}$]', fontsize=24)
    axs[2,0].minorticks_on()
    axs[2,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[2,0].get_yticklabels(), fontsize=24)

    axs[2,1].plot( ssp_ngc2808_base['wavelength'],np.log10( ssp_ngc2808_base['flux']/ ssp_ngc2808_base['flux'][index_base ]), c='#BBBBBB',)
    axs[2,1].plot(   ssp_ngc2808_bs['wavelength'],np.log10(   ssp_ngc2808_bs['flux']/   ssp_ngc2808_bs['flux'][index_bs   ]), c='#004488',)
    axs[2,1].plot(  ssp_ngc2808_ehb['wavelength'],np.log10(  ssp_ngc2808_ehb['flux']/  ssp_ngc2808_ehb['flux'][index_ehb  ]), c='#994455',)
    axs[2,1].plot(  ssp_ngc2808_bhb['wavelength'],np.log10(  ssp_ngc2808_bhb['flux']/  ssp_ngc2808_bhb['flux'][index_bhb  ]), c='#997700',)
    axs[2,1].plot(ssp_ngc2808_total['wavelength'],np.log10(ssp_ngc2808_total['flux']/ssp_ngc2808_total['flux'][index_total]), c='#000000',)
    axs[2,1].set_xlim(Ca-50, Ca+50)
    axs[2,1].set_ylim(-0.6, -0.)
    axs[2,1].set_xlabel(r'Wavelength [$\AA$]', fontsize=24)
    axs[2,1].set_ylabel(r'', fontsize=24)
    axs[2,1].minorticks_on()
    axs[2,1].set_xlim(0, 2.55)  
    axs[2,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[2,1].get_yticklabels(), fontsize=24)


    plt.savefig(path+'fig_absortion_lines_'+name+'.png', dpi=300, bbox_inches = 'tight')
