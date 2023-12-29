import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
import seaborn as sns

def fig_corcor(hst,stg):
    plt.rcParams["font.family"] = "Times New Roman"
    fig, (axa,axb,axc) = plt.subplots(1,3,sharex=False, figsize=(14,8), 
                    gridspec_kw={"width_ratios":[1,1,0.07],"wspace":0.0})
    axa = plt.subplot(1,3,1)
    sns.scatterplot(data=hst, x="FQ575N_FQ750N", y="F469N_F673N", hue="Teff", hue_norm=(6000., 66000.), style="Z", 
                    size="logg", sizes=(400, 200), palette="inferno_r", markers=["v","o"], legend=False, 
                    ax=axa)

    axa.text(-.3,-.71, r'(a)', fontsize=28.)
    axa.set_title('HST',fontsize=26)
    axa.set_xlabel('FQ575N - FQ750N', fontsize=26)
    axa.set_ylabel('F469N - F673N', fontsize=26)
    axa.set_xlim(-0.56,-0.21)
    axa.set_ylim(-0.79,1.1)
    axa.minorticks_on()
    axa.yaxis.label.set_size(28)
    axa.tick_params(direction='in', which='major', length=8., width=1., \
                   bottom=True, top=True, left=True, right=True, labelsize=265)
    axa.tick_params(direction='in', which='minor', length=5., width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    axa.set_rasterized(True)
    plt.setp(axa.get_xticklabels(), fontsize=28.)
    plt.setp(axa.get_yticklabels(), fontsize=28.)

    sns.scatterplot(data=stg, x="v_b", y="u_v", hue="Teff", hue_norm=(6000., 66000.), style="Z", 
                    size="logg", sizes=(400, 200), palette="inferno_r", markers=["v","o"], legend=False, 
                    ax=axb)
    axb.text(.32,-.71, r'(b)', fontsize=28.)
    axb.set_title('Stroemgren',fontsize=26)
    axb.set_xlabel('v - b', fontsize=26)
    axb.set_ylabel('u - v', fontsize=26)
    axb.set_ylim(-0.79,1.1)
    axb.set_yticks([])
    axb.minorticks_on()
    axb.yaxis.label.set_size(28)
    axb.tick_params(direction='in', which='major', length=8., width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    axb.tick_params(direction='in', which='minor', length=5., width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    axb.set_rasterized(True)
    plt.setp(axb.get_xticklabels(), fontsize=28.)
    plt.setp(axb.get_yticklabels(), fontsize=28.)

    norm = mpl.colors.Normalize(vmin=6000.,vmax=65000.)
    sm = plt.cm.ScalarMappable(cmap='inferno_r', norm=norm)
    sm.set_array([])
    fig.colorbar(sm, cax=axc,ticks=(10000,15000,20000,25000,30000,35000,45000,65000), 
                boundaries=np.arange(9000,66000,12))
    plt.setp(axc.get_xticklabels(), fontsize=28.)
    plt.setp(axc.get_yticklabels(), fontsize=28.)
    axc.set_title(r'T$_{eff}$ [K]', fontsize=28., loc='left')

    plt.savefig('./fig_colorcolor.png', dpi=400, bbox_inches = 'tight')
