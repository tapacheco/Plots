import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def fig_density(nlte_t10000K_g45, nlte_t10000K_g55, nlte_t10000K_g65, \
                nlte_t65000K_g45, nlte_t65000K_g55, nlte_t65000K_g65):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex=False, figsize=(14,14), 
                gridspec_kw={"wspace":0.0,"hspace":0.03})

    ax1.plot(np.log10(nlte_t10000K_g45['deepPoints']), np.log10(nlte_t10000K_g45['eletronic_density']), '.', c='#F5DB4C', label=r"",linewidth=3)
    ax1.plot(np.log10(nlte_t10000K_g55['deepPoints']), np.log10(nlte_t10000K_g55['eletronic_density']), '-.',c='#F5DB4C', label=r"",linewidth=3)
    ax1.plot(np.log10(nlte_t10000K_g65['deepPoints']), np.log10(nlte_t10000K_g65['eletronic_density']), '--',c='#F5DB4C', label=r"",linewidth=3)
    ax1.text(1.5,9., r'(a)', fontsize=26.)
    ax1.set_ylabel(r'$\log$ ($\eta_{e}$ [cm$^{-3}$])', fontsize=26)
    ax1.set_xlim(-7.0,3.0)
    ax1.set_ylim(8,19)
    ax1.minorticks_on()
    ax1.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax1.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax1.tick_params(labelbottom=False)
    plt.setp(ax1.get_xticklabels(), fontsize=26)
    plt.setp(ax1.get_yticklabels(), fontsize=26)

    ax3.plot(np.log10(nlte_t10000K_g45['deepPoints']), np.log10(nlte_t10000K_g45['mass_density']), '.', c='#F5DB4C', label=r"",linewidth=3)
    ax3.plot(np.log10(nlte_t10000K_g55['deepPoints']), np.log10(nlte_t10000K_g55['mass_density']), '-.',c='#F5DB4C', label="",linewidth=3)
    ax3.plot(np.log10(nlte_t10000K_g65['deepPoints']), np.log10(nlte_t10000K_g65['mass_density']), '--',c='#F5DB4C', label="",linewidth=3)
    ax3.text(1.5,-14., r'(b)', fontsize=26.)
    ax3.set_ylabel(r'$\log$ ($\rho$ [g cm$^{-3}$])', fontsize=26)
    ax3.set_xlabel(r'$\log$ [Depth (mass)]', fontsize=26)
    ax3.set_xlim(-7.0,3.0)
    ax3.set_ylim(-15,-4.5)
    ax3.minorticks_on()
    ax3.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax3.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    plt.setp(ax3.get_xticklabels(), fontsize=26)
    plt.setp(ax3.get_yticklabels(), fontsize=26)

    ax2.plot(np.log10(nlte_t65000K_g45['deepPoints']), np.log10(nlte_t65000K_g45['eletronic_density']), '.', c='#140B34', label=r"log $g$ = 4.5",linewidth=3)
    ax2.plot(np.log10(nlte_t65000K_g55['deepPoints']), np.log10(nlte_t65000K_g55['eletronic_density']), '-.',c='#140B34', label=r"log $g$ = 5.5",linewidth=3)
    ax2.plot(np.log10(nlte_t65000K_g65['deepPoints']), np.log10(nlte_t65000K_g65['eletronic_density']), '--',c='#140B34', label=r"log $g$ = 6.5",linewidth=3)
    ax2.text(1.5,9., r'(c)', fontsize=26.)
    ax2.minorticks_on()
    ax2.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax2.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax2.tick_params(labelleft=False,labelbottom=False)
    ax2.legend(handlelength=1.1, fontsize=24,loc="upper left")
    ax2.set_xlim(-7.0,3.0)
    ax2.set_ylim(8,19)
    plt.setp(ax2.get_xticklabels(), fontsize=26)
    plt.setp(ax2.get_yticklabels(), fontsize=26)

    ax4.plot(np.log10(nlte_t65000K_g45['deepPoints']), np.log10(nlte_t65000K_g45['mass_density']), '.', c='#140B34', label=r"",linewidth=3)
    ax4.plot(np.log10(nlte_t65000K_g55['deepPoints']), np.log10(nlte_t65000K_g55['mass_density']), '-.',c='#140B34', label="",linewidth=3)
    ax4.plot(np.log10(nlte_t65000K_g65['deepPoints']), np.log10(nlte_t65000K_g65['mass_density']), '--',c='#140B34', label="",linewidth=3)
    ax4.text(1.5,-14., r'(d)', fontsize=26.)
    ax4.set_xlabel(r'$\log$ [Depth (mass)]', fontsize=26)
    ax4.minorticks_on()
    ax4.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax4.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=24)
    ax4.tick_params(labelleft=False)
    ax4.set_xlim(-7.0,3.0)
    ax4.set_ylim(-15,-4.5)
    plt.setp(ax4.get_xticklabels(), fontsize=26)
    plt.setp(ax4.get_yticklabels(), fontsize=26)

    plt.savefig('./fig_dens_haloHerich.png', dpi=400, bbox_inches = 'tight')
