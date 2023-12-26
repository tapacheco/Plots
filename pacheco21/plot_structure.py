import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, LogLocator, NullFormatter)
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import gridspec
from matplotlib import rc
import numpy as np

def fig_structure(lte_t10000K, nlte_t10000K, lte_t15000K, nlte_t15000K, lte_t25000K, nlte_t25000K, 
                  lte_t35000K, nlte_t35000K, lte_t45000K, nlte_t45000K, lte_t65000K , nlte_t65000K):
    fig, (axa,axb,axc) = plt.subplots(1,3,sharex=False, figsize=(21,7), 
                    gridspec_kw={"width_ratios":[1,1, 0.05],"wspace":0.0})

    plt.rcParams["font.family"] = "Times New Roman"

    #PARTE A
    axa.plot(np.log10(lte_t10000K[deepPoints]), np.log10(lte_t10000K[atmpars]), '.',c='#DCE319FF', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t10000K[deepPoints]),np.log10(nlte_t10000K[atmpars]), '--',c='#DCE319FF', label="",linewidth=3.)
    axa.plot(np.log10(lte_t15000K[deepPoints]), np.log10(lte_t15000K[atmpars]), '.',c='#B8DE29FF', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t15000K[deepPoints]),np.log10(nlte_t15000K[atmpars]), '--',c='#B8DE29FF', label="",linewidth=3.)
    axa.plot(np.log10(lte_t25000K[deepPoints]), np.log10(lte_t25000K[atmpars]), '.',c='#55C667FF', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t25000K[deepPoints]),np.log10(nlte_t25000K[atmpars]), '--', c='#55C667FF', label="",linewidth=3.)
    axa.plot(np.log10(lte_t35000K[deepPoints]), np.log10(lte_t35000K[atmpars]), '.',c='#1F968BFF', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t35000K[deepPoints]),np.log10(nlte_t35000K[atmpars]), '--', c='#1F968BFF', label="",linewidth=3.)
    axa.plot(np.log10(lte_t45000K[deepPoints]), np.log10(lte_t45000K[atmpars]), '.',c='#39568CFF', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t45000K[deepPoints]),np.log10(nlte_t45000K[atmpars]), '--', c='#39568CFF', label="",linewidth=3.)
    axa.plot(np.log10(lte_t65000K[deepPoints]), np.log10(lte_t65000K[atmpars]), '.',c='#440154FF', label="LTE",linewidth=3.)
    axa.plot(np.log10(nlte_t65000K[deepPoints]),np.log10(nlte_t65000K[atmpars]), '--', c='#440154FF', label="NLTE",linewidth=3.)

    axa.text(2.,3.8, r'(a)', fontsize=20.)
    axa.set_xlim(-7.0,3.0)
    axa.set_ylim(3.6,5.51)
    axa.legend(handlelength=1.25, fontsize=20.)
    axa.set_title("Solar + He rich abundance", fontsize=22.)
    axa.set_ylabel(r'$\log$ (Temperature [K])', fontsize=20.)
    axa.set_xlabel(r'$\log$ [Depth (mass)]', fontsize=20.)
    axa.minorticks_on()
    axa.tick_params(direction='in', which='major', length=8., width=1.5)
    axa.tick_params(direction='in', which='minor', length=5., width=1.2)
    axa.set_rasterized(True)
    plt.setp(axa.get_xticklabels(), fontsize=20.)
    plt.setp(axa.get_yticklabels(), fontsize=20.)

    #PARTE B
    axb.plot(np.log10(lt10_deepPointsb), np.log10(lt10_atmparsb[0]), '.',c='#DCE319FF', label="",linewidth=3.)
    axb.plot(np.log10(nl10_deepPointsb), np.log10(nl10_atmparsb[0]), '--',c='#DCE319FF', label="",linewidth=3.)
    axb.plot(np.log10(lt15_deepPointsb), np.log10(lt15_atmparsb[0]), '.',c='#B8DE29FF', label="",linewidth=3.)
    axb.plot(np.log10(nl15_deepPointsb), np.log10(nl15_atmparsb[0]), '--',c='#B8DE29FF', label="",linewidth=3.)
    axb.plot(np.log10(lt25_deepPointsb), np.log10(lt25_atmparsb[0]), '.',c='#55C667FF', label="",linewidth=3.)
    axb.plot(np.log10(nl25_deepPointsb), np.log10(nl25_atmparsb[0]), '--', c='#55C667FF', label="",linewidth=3.)
    axb.plot(np.log10(lt35_deepPointsb), np.log10(lt35_atmparsb[0]), '.',c='#1F968BFF', label="",linewidth=3.)
    axb.plot(np.log10(nl35_deepPointsb), np.log10(nl35_atmparsb[0]), '--', c='#1F968BFF', label="",linewidth=3.)
    axb.plot(np.log10(lt45_deepPointsb), np.log10(lt45_atmparsb[0]), '.',c='#39568CFF', label="",linewidth=3.)
    axb.plot(np.log10(nl45_deepPointsb), np.log10(nl45_atmparsb[0]), '--', c='#39568CFF', label="",linewidth=3.)
    axb.plot(np.log10(lt65_deepPointsb), np.log10(lt65_atmparsb[0]), '.',c='#440154FF', label="LTE",linewidth=3.)
    axb.plot(np.log10(nl65_deepPointsb), np.log10(nl65_atmparsb[0]), '--', c='#440154FF', label="NLTE",linewidth=3.)

    axb.text(2.,3.8, r'(b)', fontsize=20.)
    axb.set_xlim(-7.0,3.0)
    axb.set_ylim(3.6,5.51)
    axb.legend(handlelength=1.25, fontsize=20.)
    axb.set_title("Halo + He rich abundance", fontsize=22.)
    axb.set_xlabel(r'$\log$ [Depth (mass)]', fontsize=20.)
    axb.minorticks_on()
    axb.tick_params(direction='in', which='major', length=8., width=1.5)
    axb.tick_params(direction='in', which='minor', length=5., width=1.2)
    axb.tick_params(labelleft=False)
    axb.set_rasterized(True)
    plt.setp(axb.get_xticklabels(), fontsize=20.)
    plt.setp(axb.get_yticklabels(), fontsize=20.)

    #BARRA DE CORES
    norm = mpl.colors.Normalize(vmin=6000.,vmax=65000.)
    sm = plt.cm.ScalarMappable(cmap='viridis_r', norm=norm)
    sm.set_array([])
    fig.colorbar(sm, cax=axc,ticks=(10000,15000,25000,35000,45000,65000), 
                boundaries=np.arange(9000,66000,12))
    plt.setp(axc.get_xticklabels(), fontsize=20.)
    plt.setp(axc.get_yticklabels(), fontsize=20.)
    axc.set_title(r'T\textsubscript{eff} [K]', fontsize=22., loc='left')

    #SALVAR
    plt.savefig('../ApJS_Pacheco2020/figures/fig_struc_lte_nlte.pdf', dpi=400, bbox_inches = 'tight')
