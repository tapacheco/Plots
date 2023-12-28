import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import gridspec

def fig_compare45(specMod2,specStar2):
    plt.rcParams["font.family"] = "Times New Roman"

    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,figsize=(12,10), tight_layout=False)
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])


    Mod2flux = signal.resample(specMod2['flux'],476000)
    Star2flux = signal.resample(specStar2['flux'],476000)
    res2_flux = Star2flux - Mod2flux
    res2_lambda = signal.resample(specMod2['wavelength'],476000)

    ax1.plot(specMod2['wavelength'], specMod2['flux'], '-',c='#61136E', label="Model 45000K",linewidth=3)
    ax1.plot(specStar2['wavelength'], specStar2['flux'], '--',c='black', label="Lamost 183405148",linewidth=3)
    ax1.legend(loc="upper right",fontsize=22)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, \
                        bottom=True, top=True, left=True, right=True, labelsize=20)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, \
                        bottom=True, top=True, left=True, right=True, labelsize=20)
    ax1.tick_params(labelbottom=False)
    ax1.set_xlim(3700.,9000.)
    ax1.set_yticks([0.0,0.5e-13,1.0e-13,1.5e-13,2.0e-13,2.5e-13,3.0e-13])
    ax1.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$]', fontsize=26)
    plt.setp(ax1.get_xticklabels(), fontsize=26)
    plt.setp(ax1.get_yticklabels(), fontsize=26)

    plt.axhline(y=0.0, color='black', linestyle='-', c='black', linewidth=1,zorder=100)
    ax2.plot(res2_lambda, res2_flux*1.e13, '-',c='gray', label="Relative flux ",linewidth=3)
    ax2.legend(loc="upper right",fontsize=22)
    ax2.minorticks_on()
    ax2.tick_params(direction='in', which='major', length=8, width=1.5, \
                        bottom=True, top=True, left=True, right=True, labelsize=20)
    ax2.tick_params(direction='in', which='minor', length=5, width=1.2, \
                        bottom=True, top=True, left=True, right=True, labelsize=20)
    plt.setp(ax2.get_xticklabels(), fontsize=26)
    plt.setp(ax2.get_yticklabels(), fontsize=26)

    ax2.set_ylim(-.75,.75)
    ax2.set_xlim(3700.,9000.)
    ax2.set_xlabel(r'Wavelength [$\AA$]', fontsize=26)
    ax2.set_ylabel(r'Residuals', fontsize=26)

    plt.minorticks_on()
    plt.xticks(fontsize=26)
    plt.yticks(fontsize=26)

    fig.savefig('./fig_spec_183405148.png', dpi=400, bbox_inches = 'tight')