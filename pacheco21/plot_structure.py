import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def fig_structure(lte_t10000K, nlte_t10000K, lte_t15000K, nlte_t15000K, lte_t25000K, nlte_t25000K, 
                  lte_t35000K, nlte_t35000K, lte_t45000K, nlte_t45000K, lte_t65000K , nlte_t65000K,
                  abundance):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, (axa,axc) = plt.subplots(1,2,sharex=False, figsize=(14,7), 
                    gridspec_kw={"width_ratios":[1, 0.05],"wspace":0.0})

    axa.plot( np.log10(lte_t10000K['deepPoints']), np.log10(lte_t10000K['atmpars']), '.',c='#FAC13B', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t10000K['deepPoints']),np.log10(nlte_t10000K['atmpars']), '--',c='#FAC13B', label="",linewidth=3.)
    axa.plot( np.log10(lte_t15000K['deepPoints']), np.log10(lte_t15000K['atmpars']), '.',c='#F57D15', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t15000K['deepPoints']),np.log10(nlte_t15000K['atmpars']), '--',c='#F57D15', label="",linewidth=3.)
    axa.plot( np.log10(lte_t25000K['deepPoints']), np.log10(lte_t25000K['atmpars']), '.',c='#D44842', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t25000K['deepPoints']),np.log10(nlte_t25000K['atmpars']), '--', c='#D44842', label="",linewidth=3.)
    axa.plot( np.log10(lte_t35000K['deepPoints']), np.log10(lte_t35000K['atmpars']), '.',c='#9F2A63', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t35000K['deepPoints']),np.log10(nlte_t35000K['atmpars']), '--', c='#9F2A63', label="",linewidth=3.)
    axa.plot( np.log10(lte_t45000K['deepPoints']), np.log10(lte_t45000K['atmpars']), '.',c='#65156E', label="",linewidth=3.)
    axa.plot(np.log10(nlte_t45000K['deepPoints']),np.log10(nlte_t45000K['atmpars']), '--', c='#65156E', label="",linewidth=3.)
    axa.plot( np.log10(lte_t65000K['deepPoints']), np.log10(lte_t65000K['atmpars']), '.',c='#000004', label="LTE",linewidth=3.)
    axa.plot(np.log10(nlte_t65000K['deepPoints']),np.log10(nlte_t65000K['atmpars']), '--', c='#000004', label="NLTE",linewidth=3.)
 
    axa.set_xlim(-7.0,3.0)
    axa.set_ylim(3.6,5.51)
    axa.legend(handlelength=1.25, fontsize=20.)
    axa.set_title("", fontsize=22.)
    axa.set_ylabel(r'$\log$ (Temperature)', fontsize=20.)
    axa.set_xlabel(r'$\log$ [Depth (mass)]', fontsize=20.)
    axa.minorticks_on()
    axa.tick_params(direction='in', which='major', length=8., width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    axa.tick_params(direction='in', which='minor', length=5., width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=20)
    axa.set_rasterized(True)
    plt.setp(axa.get_xticklabels(), fontsize=20.)
    plt.setp(axa.get_yticklabels(), fontsize=20.)

    #BARRA DE CORES
    norm = mpl.colors.Normalize(vmin=6000.,vmax=65000.)
    sm = plt.cm.ScalarMappable(cmap='inferno_r', norm=norm)
    sm.set_array([])
    fig.colorbar(sm, cax=axc,ticks=(10000,15000,25000,35000,45000,65000), 
                boundaries=np.arange(9000,66000,12))
    plt.setp(axc.get_xticklabels(), fontsize=20.)
    plt.setp(axc.get_yticklabels(), fontsize=20.)
    axc.set_title(r'$T_{eff}$ [K]', fontsize=22., loc='left')

    plt.savefig('./fig_structure'+abundance+'.png', dpi=300, bbox_inches = 'tight')
