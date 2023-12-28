import matplotlib.pyplot as plt
from matplotlib import gridspec

def fig_compare(specMod1,specStar1,specMod2,specStar2):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,figsize=(12,12))
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])

    ax1.plot(specMod1['wavelength'], specMod1['flux'], '-',c='#E65D2F', label="Model 25000K",linewidth=3)
    ax1.plot(specStar1['wavelength'], specStar1['flux'], '--',c='black', label="Lamost 442708048",linewidth=3)
    ax1.legend(loc="upper right",fontsize=22)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax1.tick_params(labelbottom=False)
    ax1.set_yticks([0.,0.5e-13,1.0e-13,1.5e-13,2.0e-13])
    ax1.set_xlim(3700.,9000.)
    ax1.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$]', fontsize=26)
    ax1.text(8600.,3.5e-14, r'(a)', fontsize=26.)
    plt.setp(ax1.get_xticklabels(), fontsize=26)
    plt.setp(ax1.get_yticklabels(), fontsize=26)


    ax2.plot(specMod2['wavelength'], specMod2['flux'], '-',c='#E65D2F', label="Model 45000K",linewidth=3)
    ax2.plot(specStar2['wavelength'], specStar2['flux'], '--',c='black', label="Lamost 183405148",linewidth=3)
    ax2.legend(loc="upper right",fontsize=22)
    ax2.minorticks_on()
    ax2.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax2.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax2.set_xlim(3700.,9000.)
    ax2.set_yticks([0.0,0.5e-13,1.0e-13,1.5e-13,2.0e-13,2.5e-13])
    ax2.set_xticks([3800,4800,5800,6800,7800,8800])
    ax2.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$]', fontsize=26)
    ax2.text(8600.,4.5e-14, r'(b)', fontsize=26.)
    plt.setp(ax2.get_xticklabels(), fontsize=26)
    plt.setp(ax2.get_yticklabels(), fontsize=26)
    ax2.set_xlim(3700.,9000.)
    ax2.set_xlabel(r'Wavelength [$\AA$]', fontsize=26)
    ax2.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$]', fontsize=26)

    fig.savefig('./fig_spec_optico.png', dpi=400)
