import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import gridspec
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns


def plot_color_magnitude_diagram(ms_color, gb_color, rhb_color,\
                              bs_color, bhb_color, ehb_color, \
                              path):
    xmin, xmax, ymax, ymin = (-2.2,3.4,27.4,10.4)

    fig, axt = plt.subplots(sharex=True, figsize=(8,8), tight_layout=True)
    #PLOT 
    plt.minorticks_on()


    plt.scatter(ms_color['F275W_F336W'],  ms_color['F275W'], label='Main Sequence', marker='>', s=2, c='#EE7733')#orange
    plt.scatter(gb_color['F275W_F336W'],  gb_color['F275W'], label='Giant Branches', marker='^', s=2, c='#009988')#teal
    plt.scatter(rhb_color['F275W_F336W'],rhb_color['F275W'], label='Red Horizontal Branch', marker='<', s=2, c='#CC3311')#red
    plt.scatter(bs_color['F275W_F336W'],  bs_color['F275W'], label='Blue Straggler', marker='*', s=2, c='#0077BB')#blue
    plt.scatter(bhb_color['F275W_F336W'],bhb_color['F275W'], label='Blue Horizontal Branch', marker='o', s=2, c='#EE3377')#magenta
    plt.scatter(ehb_color['F275W_F336W'],ehb_color['F275W'], label='Extreme Horizontal Branch', marker='s', s=2, c='#33BBEE')#cyan
    #plt.scatter(cor, mag, marker='o', c='purple')

    axt.legend(fontsize=16)
    axt.set_xlim(xmin, xmax)
    axt.set_ylim(ymax, ymin)
    plt.title("", fontsize=30)
    plt.ylabel('F275W', fontsize=22)
    plt.xlabel('F275W - F336W', fontsize=22)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True)

    #plt.show()
    plt.savefig(path+'CMD1.png', dpi=300, bbox_inches = 'tight')


def plot_color_color_2(ms_color, gb_color, #rhb_color, 
                             bs_color, bhb_color, ehb_color, path):
    fig, (ax1) = plt.plot(figsize=(10,5), tight_layout=True)

    plt.rcParams["font.family"] = "Times New Roman"

    ax1.scatter(ms_color['F336W_F438W'], ms_color['F275W_F336W'], marker='>', s=20, c='#DDAA33',label='MS')
    ax1.scatter(gb_color['F336W_F438W'], gb_color['F275W_F336W'], marker='^', s=20, c='#BB5566',label='GB')
    ax1.scatter(bs_color['F336W_F438W'], bs_color['F275W_F336W'], marker='s', s=20, c='#004488',label='BS')
    ax1.scatter(bhb_color['F336W_F438W'],bhb_color['F275W_F336W'],marker='o', s=20, c='#009988',label='BHB')
    ax1.scatter(ehb_color['F336W_F438W'],ehb_color['F275W_F336W'],marker='*', s=20, c='#EE3377',label='EHB')
    ax1.set_xlim(-2.31,2.31)
    ax1.set_ylim(-1.21,3.21)
    ax1.set_ylabel('F275W - F336W', fontsize=20)
    ax1.set_xlabel('F336W - F438W', fontsize=20)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax1.get_xticklabels(), fontsize=20)
    plt.setp(ax1.get_yticklabels(), fontsize=20)


    plt.savefig(path+'CCD.png', dpi=300, bbox_inches = 'tight')


def plot_color_color_diagram(ms_color, gb_color, #rhb_color, 
                             bs_color, bhb_color, ehb_color, path):
    fig, ((ax1,ax2,ax3),(ax4,ax5,ax7)) = plt.subplots(2,3,sharex=False, figsize=(14,8), 
                                                      tight_layout=True)

    plt.rcParams["font.family"] = "Times New Roman"

    ax1.scatter(ms_color['F336W_F438W'], ms_color['F275W_F336W'], marker='o', s=50, c='#cccc00',label='MS')
    ax1.scatter(gb_color['F336W_F438W'], gb_color['F275W_F336W'], marker='o', s=50, c='#00cccc',label='gb')
    ax1.scatter(bhb_color['F336W_F438W'],bhb_color['F275W_F336W'], marker='o', s=50, c='#800080',label='HB')
    ax1.scatter(ehb_color['F336W_F438W'],ehb_color['F275W_F336W'], marker='o', s=50, c='#ff00ff',label='EHB')
    ax1.scatter(bs_color['F336W_F438W'], bs_color['F275W_F336W'], marker='o', s=50, c='#0000ff',label='bs')
    #ax1.scatter(rhb_color['F336W_F438W'], rhb_color['F275W_F336W'], marker='o', s=50, c='#ff0000',label='RC')
    ax1.set_xlim(-2.2,3.)
    ax1.set_ylim(-.9,3.5)
    ax1.set_ylabel('F275W - F336W', fontsize=20)
    ax1.set_xlabel('F336W - F438W', fontsize=20)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax1.get_xticklabels(), fontsize=20)
    plt.setp(ax1.get_yticklabels(), fontsize=20)

    ax2.scatter(ms_color['F438W_F606W'], ms_color['F275W_F438W'], marker='o', s=50, c='#cccc00',label='MS')
    ax2.scatter(gb_color['F438W_F606W'], gb_color['F275W_F438W'], marker='o', s=50, c='#00cccc',label='gb')
    ax2.scatter(bhb_color['F438W_F606W'],bhb_color['F275W_F438W'], marker='o', s=50, c='#800080',label='HB')
    ax2.scatter(ehb_color['F438W_F606W'],ehb_color['F275W_F438W'], marker='o', s=50, c='#ff00ff',label='EHB')
    ax2.scatter(bs_color['F438W_F606W'], bs_color['F275W_F438W'], marker='o', s=50, c='#0000ff',label='bs')
    #ax2.scatter(rhb_color['F438W_F606W'], rhb_color['F275W_F438W'], marker='o', s=50, c='#ff0000',label='RC')
    ax2.set_xlim(-.8,3.2)
    ax2.set_ylim(-3.1,5.9)
    ax2.set_ylabel('F275W - F438W', fontsize=20)
    ax2.set_xlabel('F438W - F606W', fontsize=20)
    ax2.minorticks_on()
    ax2.tick_params(direction='in', which='major', length=8, width=1.5)
    ax2.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax2.get_xticklabels(), fontsize=20)
    plt.setp(ax2.get_yticklabels(), fontsize=20)

    ax3.scatter(ms_color['F606W_F814W'], ms_color['F275W_F606W'], marker='o', s=50, c='#cccc00',label='MS')
    ax3.scatter(gb_color['F606W_F814W'], gb_color['F275W_F606W'], marker='o', s=50, c='#00cccc',label='gb')
    ax3.scatter(bhb_color['F606W_F814W'],bhb_color['F275W_F606W'], marker='o', s=50, c='#800080',label='HB')
    ax3.scatter(ehb_color['F606W_F814W'],ehb_color['F275W_F606W'], marker='o', s=50, c='#ff00ff',label='EHB')
    ax3.scatter(bs_color['F606W_F814W'], bs_color['F275W_F606W'], marker='o', s=50, c='#0000ff',label='bs')
    #ax3.scatter(rhb_color['F606W_F814W'], rhb_color['F275W_F606W'], marker='o', s=50, c='#ff0000',label='RC')
    ax3.set_xlim(-.6,1.55)
    #ax3.set_ylim(-2.5,2.)
    ax3.set_ylabel('F275W - F606W', fontsize=20)
    ax3.set_xlabel('F606W - F814W', fontsize=20)
    ax3.minorticks_on()
    ax3.tick_params(direction='in', which='major', length=8, width=1.5)
    ax3.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax3.get_xticklabels(), fontsize=20)
    plt.setp(ax3.get_yticklabels(), fontsize=20)

    ax4.scatter(ms_color['F336W_F438W'], ms_color['F275W_F438W'], marker='o', s=50, c='#cccc00',label='MS')
    ax4.scatter(gb_color['F336W_F438W'], gb_color['F275W_F438W'], marker='o', s=50, c='#00cccc',label='gb')
    ax4.scatter(bhb_color['F336W_F438W'],bhb_color['F275W_F438W'], marker='o', s=50, c='#800080',label='HB')
    ax4.scatter(ehb_color['F336W_F438W'],ehb_color['F275W_F438W'], marker='o', s=50, c='#ff00ff',label='EHB')
    ax4.scatter(bs_color['F336W_F438W'], bs_color['F275W_F438W'], marker='o', s=50, c='#0000ff',label='bs')
    #ax4.scatter(rhb_color['F336W_F438W'], rhb_color['F275W_F438W'], marker='o', s=50, c='#ff0000',label='RC')
    ax4.set_xlim(-2.2,2.8)
    ax4.set_ylim(-3.1,5.9)
    ax4.set_ylabel('F275W - F438W', fontsize=20)
    ax4.set_xlabel('F336W - F438W', fontsize=20)
    ax4.minorticks_on()
    ax4.tick_params(direction='in', which='major', length=8, width=1.5)
    ax4.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax4.get_xticklabels(), fontsize=20)
    plt.setp(ax4.get_yticklabels(), fontsize=20)

    ax5.scatter(ms_color['F438W_F606W'], ms_color['F336W_F438W'], marker='o', s=50, c='#cccc00',label='MS')
    ax5.scatter(gb_color['F438W_F606W'], gb_color['F336W_F438W'], marker='o', s=50, c='#00cccc',label='gb')
    ax5.scatter(bhb_color['F438W_F606W'],bhb_color['F336W_F438W'], marker='o', s=50, c='#800080',label='HB')
    ax5.scatter(ehb_color['F438W_F606W'],ehb_color['F336W_F438W'],  marker='o', s=50, c='#ff00ff',label='EHB')
    ax5.scatter(bs_color['F438W_F606W'], bs_color['F336W_F438W'], marker='o', s=50, c='#0000ff',label='bs')
    #ax5.scatter(rhb_color['F438W_F606W'], rhb_color['F336W_F438W'], marker='o', s=50, c='#ff0000',label='RC')
    ax5.set_xlim(-.8,3.2)
    ax5.set_ylim(-2.2,3.)
    ax5.set_ylabel('F336W - F438W', fontsize=20)
    ax5.set_xlabel('F438W - F606W', fontsize=20)
    ax5.minorticks_on()
    ax5.tick_params(direction='in', which='major', length=8, width=1.5)
    ax5.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax5.get_xticklabels(), fontsize=20)
    plt.setp(ax5.get_yticklabels(), fontsize=20)

    ax7.scatter(ms_color['F606W_F814W'], ms_color['F275W_F336W'], marker='o', s=50, c='#cccc00',label='MS')
    ax7.scatter(gb_color['F606W_F814W'], gb_color['F275W_F336W'], marker='o', s=50, c='#00cccc',label='gb')
    ax7.scatter(bhb_color['F606W_F814W'],bhb_color['F275W_F336W'], marker='o', s=50, c='#800080',label='HB')
    ax7.scatter(ehb_color['F606W_F814W'],ehb_color['F275W_F336W'], marker='o', s=50, c='#ff00ff',label='EHB')
    ax7.scatter(bs_color['F606W_F814W'], bs_color['F275W_F336W'], marker='o', s=50, c='#0000ff',label='bs')
    #ax7.scatter(rhb_color['F606W_F814W'], rhb_color['F275W_F336W'], marker='o', s=50, c='#ff0000',label='RC')
    ax7.set_xlim(-.6,1.55)
    ax7.set_ylim(-1.,3.5)
    ax7.set_ylabel('F275W - F336W', fontsize=20)
    ax7.set_xlabel('F606W - F814W', fontsize=20)
    ax7.minorticks_on()
    ax7.tick_params(direction='in', which='major', length=8, width=1.5)
    ax7.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax7.get_xticklabels(), fontsize=20)
    plt.setp(ax7.get_yticklabels(), fontsize=20)

    plt.savefig(path+'CCD.png', dpi=300, bbox_inches = 'tight')
#    plt.show()


def plot_distance_histogram(ms_distance_model, 
                            gb_distance_model, 
                            rc_distance_model, 
                            bs_distance_model, 
                            rhb_distance_model, 
                            bhb_distance_model, 
                            path):
    fig, ax1 = plt.subplots(sharex=False, figsize=(8,8), tight_layout=True)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.grid(axis='y', alpha=0.75)
 
    sns.color_palette("husl", 11)
    kwargs = dict(hist_kws={'alpha':.3}, kde_kws={'linewidth':3}, bins=15)

    sns.distplot(ms_distance_model, label="MS", **kwargs, color='yellow')
    sns.distplot(gb_distance_model, label="GB", **kwargs, color='cyan')
    sns.distplot(rc_distance_model, label="RHB", **kwargs, color='red')
    sns.distplot(bs_distance_model, label="BS", **kwargs, color='blue')
    sns.distplot(rhb_distance_model, label="BHB", **kwargs, color='purple')
    sns.distplot(bhb_distance_model,label="EHB",**kwargs, color='magenta')

    ax1.set_xlim(0,1.5)
    #ax1.set_ylabel('Frequency', fontsize=20)
    ax1.set_xlabel('Distance', fontsize=20)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.axes.yaxis.set_ticklabels([])
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.legend()
    plt.setp(ax1.get_xticklabels(), fontsize=20)
    plt.setp(ax1.get_yticklabels(), fontsize=20)

    plt.savefig(path+'histogram_distances.png', dpi=100, bbox_inches = 'tight')

    plt.show()


def plot_line_profile(total_wavelength, total_flux,
                      base_wavelength,base_flux, 
                      bhb_wavelength, bhb_flux, 
                      bs_wavelength, bs_flux,
                      ehb_wavelength, ehb_flux, 
                      central_line_wavelength,
                      output_file_name):

    figa, (ax1,ax1R) = plt.subplots(2,1,sharex=True,figsize=(10,7), tight_layout=False)
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax1R= plt.subplot(gs[1])

    ax1.plot(total_wavelength, total_flux, label='SSP All', c='black', linestyle='-',  linewidth=3, zorder=10)
    ax1.plot(bhb_wavelength, bhb_flux,  label='Base + BHB', c='#800080', linestyle='--', linewidth=3, zorder=10)
    ax1.plot(base_wavelength,base_flux, label='SSP Base', c='gray', linestyle='-',linewidth=3)
    ax1.plot(bs_wavelength, bs_flux,  label='Base + BS', c='#0000ff', linestyle='-.',  linewidth=3)
    ax1.plot(ehb_wavelength, ehb_flux,  label='Base + EHB', c='#ff00ff', linestyle=':',linewidth=3)
    ax1.axvline(central_line_wavelength, c='black')
    ax1.set_xlim(central_line_wavelength-10,central_line_wavelength+10)
    #ax1.set_ylim(0.5,4.1)
    ax1.set_title(r'(%d \texttt{\AA})' %central_line_wavelength, fontsize=26)
    ax1.legend(handlelength=2., fontsize=12)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2)
    ax1.set_xticklabels([])

    ax1R.set_xlim(central_line_wavelength-10,central_line_wavelength+10)
    ax1R.set_xticklabels([])
    ax1R.set_ylim(-0.01,0.01)
    ax1R.axhline(y=0.0, linestyle='-', c='gray', linewidth=3,zorder=100)
    ax1R.plot(total_wavelength, (total_flux-base_flux), '-',c='black', linewidth=3)
    ax1R.plot(bhb_wavelength,(bhb_flux-base_flux), '--',c='#800080',linewidth=3)
    ax1R.plot(bs_wavelength,  (bs_flux-base_flux), '-.',c='#0000ff',linewidth=3)
    ax1R.plot(ehb_wavelength, (ehb_flux-base_flux), ':',c='#ff00ff',linewidth=3)
    ax1R.set_xlabel(r'Wavelength [\texttt{\AA}]', fontsize=26)
    ax1R.minorticks_on()
    ax1R.tick_params(direction='in', which='major', length=8, width=1.5)
    ax1R.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.setp(ax1R.get_xticklabels(), fontsize=26)
    ax1R.yaxis.label.set_size(26)
    ax1R.xaxis.label.set_size(26)

    plt.savefig('/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/figures/'+output_file_name,
                dpi=100, bbox_inches = 'tight')
    plt.show()


def plot_ssp_compare(wavelength_ssp, base_flux, bs_flux, bhb_flux, ehb_flux, all_flux,
                      output_file_name):

    figa, (ax1,ax1R) = plt.subplots(2,1,sharex=True, figsize=(14,8), tight_layout=True)
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax1R= plt.subplot(gs[1])

    ax1.plot(wavelength_ssp, base_flux/1e-5,label='Base = MS + GB + RHB', c='gray',zorder=1, linestyle='-',linewidth=3)
    ax1.plot(wavelength_ssp, bs_flux/1e-5,  label='Base + BS', c='#0000ff',zorder=10, linestyle='-.',  linewidth=3)
    ax1.plot(wavelength_ssp, bhb_flux/1e-5, label='Base + BHB', c='#800080',zorder=100, linestyle='--', linewidth=3)
    ax1.plot(wavelength_ssp, ehb_flux/1e-5, label='Base + EHB', c='#ff00ff',zorder=100, linestyle=':',linewidth=3)
    ax1.plot(wavelength_ssp, all_flux/1e-5, label='SSP All', c='black',zorder=1, linestyle='-',  linewidth=3)
    ax1.set_ylim(-0.05,1.05)
    ax1.set_xlim(2500,7100)
    ax1.set_ylabel(r'Flux [10$^{-5}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]', fontsize=20)
    ax1.legend(handlelength=2.14, fontsize=14, loc='lower right')
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, labelsize=20,\
                    bottom=True, top=True, left=True, right=True)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, labelsize=20, \
                    bottom=True, top=True, left=True, right=True)
    ax1.set_xticklabels([])

    ax1R.set_xlim(2500,7100)
    ax1R.set_ylim(-0.01,0.21)
    ax1R.axhline(y=0.0, linestyle='-', c='gray', linewidth=3,zorder=100)
    ax1R.plot(wavelength_ssp, (all_flux-base_flux)/1e-5, label='BS+BHB+EHB', linestyle='-',c='black', linewidth=3)
    ax1R.plot(wavelength_ssp, (bhb_flux-base_flux)/1e-5, label='BHB', linestyle='--',c='#800080',linewidth=3)
    ax1R.plot(wavelength_ssp, (ehb_flux-base_flux)/1e-5, label='EHB', linestyle=':',c='#ff00ff',linewidth=3)
    ax1R.plot(wavelength_ssp,  (bs_flux-base_flux)/1e-5, label='BS', linestyle='-.',c='#0000ff',linewidth=3)
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

    plt.savefig(output_file_name+'ssp_comparing_R1000.png',
                dpi=300, bbox_inches = 'tight')
    plt.show()

def plot_spectrum(wavelength, flux,
                  evolutionary_phase):
    fig, ax1 = plt.subplots(sharex=False, figsize=(10,8), tight_layout=True)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.grid(axis='y', alpha=0.75)
   
    ax1.plot(wavelength, flux, label='SSP', c='black', linestyle='-',  linewidth=3, zorder=10)    
    #ax1.set_title(r'(%s )' %evolutionary_phase, fontsize=26)
    ax1.legend(handlelength=2., fontsize=16)
    ax1.minorticks_on()
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True)

    plt.savefig('/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/figures/'+evolutionary_phase + '.png',
                dpi=100, bbox_inches = 'tight')
    #plt.show()


def plot_evolutionary_SSP(wavelength, gb_flux, ms_flux, rhb_flux, bs_flux, bhb_flux, ehb_flux, path):
    fig, axt = plt.subplots(sharex=True, figsize=(14,7), tight_layout=True)
    plt.minorticks_on()

    axt.plot(wavelength, np.log10(gb_flux), c='#009988',label='Giant Branches', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(ms_flux), c='#EE7733',label='Main Sequence', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(rhb_flux), c='#CC3311',label='Red Horizontal Branch', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(bs_flux), c='#0077BB',label='Blue Straggler', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(bhb_flux), c='#EE3377',label='Blue Horizontal Branch', linestyle='-', linewidth=3)
    axt.plot(wavelength, np.log10(ehb_flux), c='#33BBEE',label='Extreme Horizontal Branch', linestyle='-', linewidth=3)

    #plt.legend(handlelength=1.25, fontsize=16, loc='lower left')
    plt.title("", fontsize=30)
    plt.ylabel(r'$\log$ Flux [erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]', fontsize=20)
    plt.xlabel(r'Wavelength [\AA]', fontsize=20)
    axt.set_xlim(2500,7050)
    axt.set_ylim(-8.05,-4.95)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True)

    plt.savefig(path+'evolutionary_phases_R6800.png', dpi=300, bbox_inches = 'tight')
    #plt.show()


def plot_ssp(wavelength, flux, path,\
             ssp_wavelength, ssp_flux):
    fig, ax1 = plt.subplots(sharex=False, figsize=(14,7), tight_layout=True)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.grid(axis='y', alpha=0.75)
   
    ax1.plot(wavelength, flux/integrate.trapz(flux, wavelength), label='Obs', c='black', linestyle='-',  linewidth=3, zorder=10)    
    ax1.plot(ssp_wavelength, ssp_flux/integrate.trapz(ssp_flux, ssp_wavelength), label='Model', c='magenta', linestyle='--',  linewidth=3, zorder=100)    
 
    plt.legend(handlelength=1.25, fontsize=20, loc='lower left')
    plt.title("", fontsize=30)
    plt.ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]', fontsize=30)
    plt.xlabel(r'Wavelength [\AA]', fontsize=30)
    ax1.set_xlim(3200,6500)
    plt.xticks(fontsize=28)
    plt.yticks(fontsize=28)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2)

    plt.savefig(path+'ngc2808_ssp.png', dpi=100, bbox_inches = 'tight')
    #plt.show()