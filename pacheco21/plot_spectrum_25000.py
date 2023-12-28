import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import gridspec

def fig_compare25(specMod1,specStar1):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,figsize=(12,10))
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1],hspace=0.01)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])

    Mod1flux = signal.resample(specMod1['flux'],476000)
    Star1flux = signal.resample(specStar1['flux'],476000)
    res_flux = Star1flux - Mod1flux
    res_lambda = signal.resample(specMod1['wavelength'],476000)

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
    plt.setp(ax1.get_xticklabels(), fontsize=26)
    plt.setp(ax1.get_yticklabels(), fontsize=26)

    plt.axhline(y=0.0, color='black', linestyle='-', c='black', linewidth=1,zorder=100)
    ax2.plot(res_lambda, res_flux*1.e13, '-',c='gray', label="Relative flux ",linewidth=3)
    ax2.legend(loc="upper right",fontsize=22)
    ax2.minorticks_on()
    ax2.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax2.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    plt.setp(ax2.get_xticklabels(), fontsize=26)
    plt.setp(ax2.get_yticklabels(), fontsize=26)

    ax2.set_xlim(3700.,9000.)
    ax2.set_ylim(-.75,.75)
    ax2.set_xlabel(r'Wavelength [$\AA$]', fontsize=26)
    ax2.set_ylabel(r'Residuals', fontsize=26)

    fig.savefig('./fig_spec_442708048.png', dpi=400, bbox_inches = 'tight')
