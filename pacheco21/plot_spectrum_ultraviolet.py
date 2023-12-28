import matplotlib.pyplot as plt

def fig_compareUV(specMod3,specStar3):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, ax1 = plt.subplots(1,1,sharex=True,figsize=(12,6))

    ax1.plot(specMod3['wavelength'], specMod3['flux'], '-',c='#E65D2F', label="Model",linewidth=3)
    ax1.plot(specStar3['wavelength'], specStar3['flux'], '--',c='black', label="HD 4539",linewidth=3)
    ax1.legend(loc="upper right",fontsize=22)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    ax1.set_yticks([0.,0.5e-11,1.0e-11,1.5e-11,2.0e-11,2.5e-11,3.0e-11])
    ax1.set_xlim(1150.,1730.)
    ax1.set_ylabel(r'Flux [erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$]', fontsize=26)
    ax1.set_xlabel(r'Wavelength [$\AA$]', fontsize=26)
    plt.setp(ax1.get_xticklabels(), fontsize=26)
    plt.setp(ax1.get_yticklabels(), fontsize=26)
    ax1.yaxis.label.set_size(26)

    fig.savefig('./fig_spec_ultraviolet.png', dpi=400, bbox_inches = 'tight')
