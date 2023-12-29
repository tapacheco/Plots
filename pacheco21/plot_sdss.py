import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
import seaborn as sns
import pandas as pd

def funcVoid(string): return float(string) if string.strip() else float(100.)

def function_data(geier):
    umag = []
    for i in geier['umagSDSS']:
        pd.to_numeric(umag.append(funcVoid(i)), downcast='float')
    u = np.asarray(umag)
    gmag = []
    for j in geier['gmagSDSS']:
        pd.to_numeric(gmag.append(funcVoid(j)), downcast='float')
    g = np.asarray(gmag)
    rmag = []
    for k in geier['rmagSDSS']:
        pd.to_numeric(rmag.append(funcVoid(k)), downcast='float')
    r = np.asarray(rmag)
    temp = []
    for l in geier['Teff']:
        pd.to_numeric(temp.append(funcVoid(l)), downcast='float')
    tef = np.asarray(temp)
    mask_mag = np.where((u!=100.) | (g!=100.) | (r!=100.))[0]
    u_g = u[mask_mag] - g[mask_mag]
    g_r = g[mask_mag] - r[mask_mag]
    tef = tef[mask_mag]
    return u_g, g_r, tef

def fig_sdss(geier, sdss21, sdss23):
    u_g, g_r, tef = function_data(geier)
    mask_tef = np.where((tef >= 6000.) & (tef <=66000.) & (tef!=7180))[0]
    tef_corte, ug_corte, gr_corte = tef[mask_tef], u_g[mask_tef], g_r[mask_tef]

    plt.rcParams["font.family"] = "Times New Roman"
    fig, ax = plt.subplots(sharex=True,figsize=(12,8), gridspec_kw={"wspace":0.0})
    plt.scatter(u_g, g_r, c='grey', marker='+')           
    plt.scatter(ug_corte, gr_corte, c=tef_corte, cmap='inferno_r', alpha=0.35)
    sns.scatterplot(data=sdss21, x="tu_g", y="tg_r", hue="Teff", hue_norm=(6000., 66000.), style="Z", 
                    size="logg", sizes=(400, 200), palette="inferno_r", markers=["v","o"], 
                    legend=False, ax=ax)
    sns.scatterplot(data=sdss23, x="tu_g", y="tg_r", hue="Teff", hue_norm=(6000., 66000.), style="Z", 
                    size="logg", sizes=(400, 200), palette="inferno_r", markers=["v","o"], 
                    legend=False, ax=ax)
    plt.title('SDSS',fontsize=26)
    ax.set_xlabel('u - g', fontsize=26)
    ax.set_ylabel('g - r', fontsize=26)
    sns.set(font_scale=1.4)
    sns.set_style("whitegrid", {'axes.grid' : False})
    sns.set_style("ticks", {"xtick.major.size": 28, "ytick.major.size": 28})
    plt.rcParams["font.family"] = "Times New Roman"
    norm = mpl.colors.Normalize(vmin=6000,vmax=65000)
    sm = plt.cm.ScalarMappable(cmap='inferno_r', norm=norm)
    sm.set_array([])
    cbar=plt.colorbar(sm, ticks=(10000,15000,20000,25000,30000,35000,45000,65000), 
                boundaries=np.arange(9000,66000,12))
    cbar.set_label(label=r'T$_{eff}$ [K]', size=26,rotation=0,labelpad=-60,y=1.06)
    cbar.ax.tick_params(labelsize=26) 
    ax.yaxis.label.set_size(28)
    ax.minorticks_on()
    ax.set_ylim(-.65,.15)
    ax.set_xlim(-.75,1.55)
    plt.tight_layout()
    plt.xticks(fontsize=26)
    plt.yticks(fontsize=26)
    plt.tick_params(direction='in', which='major', length=8, width=1.5)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2)
    plt.savefig('./fig_color_sdss.png', dpi=400, bbox_inches = 'tight')
 