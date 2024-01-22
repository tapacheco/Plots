import matplotlib.pyplot as plt
import numpy as np

def fig_UV(data10B, data15B, data20B, data25B, data30B, data35B, data45B, data65B ):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, (ax1,ax2,ax3,ax7,ax4,ax8,ax5,ax6) = plt.subplots(8,1,sharex=True,figsize=(12,20))
 
    plt.minorticks_on()
    plt.xticks(fontsize=26)
    plt.yticks(fontsize=26)

    ax1.plot(data65B['wavelength'], data65B['flux'], '-',c='#140B34', label="65000 K",linewidth=3)
    ax1.legend(loc="upper right",fontsize=22)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax1.yaxis.label.set_size(26)

    ax2.plot(data45B['wavelength'], data45B['flux'], '-',c='#61136E', label="45000 K",linewidth=3)
    ax2.legend(loc="upper right",fontsize=22)
    ax2.minorticks_on()
    ax2.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax2.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax2.yaxis.label.set_size(26)

    ax3.plot(data35B['wavelength'], data35B['flux'], '-',c='#A92E5E', label="35000 K",linewidth=3)
    ax3.legend(loc="upper right",fontsize=22)
    ax3.minorticks_on()
    ax3.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax3.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax3.yaxis.label.set_size(26)

    ax7.plot(data30B['wavelength'], data30B['flux'], '-',c='#CB4149', label="30000 K",linewidth=3)
    ax7.legend(loc="upper right",fontsize=22)
    ax7.minorticks_on()
    ax7.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax7.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax7.yaxis.label.set_size(26)

    ax4.plot(data25B['wavelength'], data25B['flux'], '-',c='#E65D2F', label="25000 K",linewidth=3)
    ax4.legend(loc="upper right",fontsize=22)
    ax4.minorticks_on()
    ax4.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax4.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax4.yaxis.label.set_size(26)

    ax8.plot(data20B['wavelength'], data20B['flux'], '-',c='#F78212', label="20000 K",linewidth=3)
    ax8.legend(loc="upper right",fontsize=22)
    ax8.minorticks_on()
    ax8.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax8.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax8.yaxis.label.set_size(26)

    ax5.plot(data15B['wavelength'], data15B['flux'], '-',c='#FCAE12', label="15000 K",linewidth=3)
    ax5.legend(loc="upper right",fontsize=22)
    ax5.minorticks_on()
    ax5.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax5.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax5.yaxis.label.set_size(26)

    ax6.plot(data10B['wavelength'], data10B['flux'], '-',c='#F5DB4C', label="10000 K",linewidth=3)
    ax6.legend(loc="lower right",fontsize=22)
    ax6.minorticks_on()
    ax6.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax6.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax6.yaxis.label.set_size(26)
    #ax6.set_ylim(0,1.7e7)

    ax1.set_xlim(1000.,2000.)
    ax6.set_xlabel(r'Wavelength [$\AA$]', fontsize=26)
    ax6.set_xticks([1100,1300,1500,1700,1900])

    plt.subplots_adjust(left=0.08, bottom=0.06, right=0.96, top=0.96, wspace=0.0, hspace=0.18)
    fig.text(0.04, 0.5, r'Flux [erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$]', fontsize=26, 
            ha='center', va='center', rotation='vertical')


    plt.savefig('./fig_spec_UV_fwhm5.png', dpi=400, bbox_inches = 'tight')
