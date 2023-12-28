import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
import seaborn as sns
from scipy import stats


def fig_inglisTeller(data_IT):
    Teff = data_IT['Teff'] * 1000
    logg = data_IT['gravity'] * 0.1
    logNmax = np.log10(data_IT['Nmax'])

    res = stats.linregress(logNmax, data_IT['eletronic_density'])
    print(f"sdt err: {res.stderr:.6f}")
    print(f"R-squared: {res.rvalue**2:.6f}")

    plt.rcParams["font.family"] = "Times New Roman"
    fig, ax = plt.subplots(sharex=False,figsize=(12,10), gridspec_kw={"wspace":0.0})

    ax = sns.regplot(data=data_IT, x=logNmax, y="eletronic_density", color="gray", scatter_kws={'alpha':0.1})
    sns.scatterplot(data=data_IT, x=logNmax, y="eletronic_density", hue=Teff, hue_norm=(6000., 66000.), 
                size=logg, sizes=(450, 250), palette="inferno_r", marker="v", legend=False, zorder=100)

    plt.title('Inglis-Teller Diagram',fontsize=28)
    ax.set_xlabel(r'$\log$ N$_{max}$', fontsize=26)
    ax.set_ylabel(r'$\log$ [$\eta_{e}(\tau = 0.1)$ [cm$^{-3}$]]', fontsize=26)
    sns.set(font_scale=1.4)
    sns.set_style("whitegrid", {'axes.grid' : False})
    sns.set_style("ticks", {"xtick.major.size": 28, "ytick.major.size": 28})

    norm = mpl.colors.Normalize(vmin=6000,vmax=65000)
    sm = plt.cm.ScalarMappable(cmap='inferno_r', norm=norm)
    sm.set_array([])
    cbar=plt.colorbar(sm, ticks=(10000,15000,25000,35000,45000,65000), 
                      boundaries=np.arange(9000,66000,12))
    cbar.set_label(label=r'$T_{eff}$ [K]', size=26,rotation=0,labelpad=-60,y=1.05)
    cbar.ax.tick_params(labelsize=26) 

    ax.set_xlim(0.75,1.42)
    ax.yaxis.label.set_size(26)
    ax.minorticks_on()
    plt.tight_layout()
    plt.xticks(fontsize=26)
    plt.yticks(fontsize=26)    
    ax.tick_params(direction='in', which='major', length=8., width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax.tick_params(direction='in', which='minor', length=5., width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.text(1.05, 16.51, r'log $\eta_{e}$ = 20.12 - 4.64$\cdot$log N$_{max}$', fontsize=24)
    plt.text(1.15, 16.35, r'R$^2$-value: 0.645566', fontsize=24)

    plt.savefig('./fig_inglisTeller.png', dpi=300, bbox_inches = 'tight')
