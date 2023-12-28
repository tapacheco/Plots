import matplotlib.pyplot as plt
import numpy as np

def fig_coverage(data10B,data10R,
                 data15B,data15R,
                 data20B,data20R,
                 data25B,data25R,
                 data30B,data30R,
                 data35B,data35R,
                 data45B,data45R,
                 data65B,data65R
                 ):

    fig, ax = plt.subplots(sharex=True,figsize=(21,15),tight_layout=True)
    #plt.rcParams['ytick.labelsize']=20

    ax.plot(data10B['wavelength'], np.log10(data10B['flux']), '-',c='#DCE319FF', label="",linewidth=4)
    ax.plot(data10R['wavelength'], np.log10(data10R['flux']), '-',c='#DCE319FF', label="",linewidth=4)

    ax.plot(data15B['wavelength'], np.log10(data15B['flux']*10**2.), '-',c='#B8DE29FF', label="",linewidth=4)
    ax.plot(data15R['wavelength'], np.log10(data15R['flux']*10**2.), '-',c='#B8DE29FF', label="",linewidth=4)

    ax.plot(data20B['wavelength'], np.log10(data20B['flux']*10**4.), '-',c='#95D840FF', label="",linewidth=4)
    ax.plot(data20R['wavelength'], np.log10(data20R['flux']*10**4.), '-',c='#95D840FF', label="",linewidth=4)

    ax.plot(data25B['wavelength'], np.log10(data25B['flux']*10**6.), '-',c='#55C667FF', label="",linewidth=4)
    ax.plot(data25R['wavelength'], np.log10(data25R['flux']*10**6.), '-',c='#55C667FF', label="",linewidth=4)

    ax.plot(data30B['wavelength'], np.log10(data30B['flux']*10**7.5), '-',c='#29AF7FFF', label="",linewidth=4)
    ax.plot(data30R['wavelength'], np.log10(data30R['flux']*10**7.5), '-',c='#29AF7FFF', label="",linewidth=4)

    ax.plot(data35B['wavelength'], np.log10(data35B['flux']*10**8.3), '-',c='#1F968BFF', label="",linewidth=4)
    ax.plot(data35R['wavelength'], np.log10(data35R['flux']*10**8.3), '-',c='#1F968BFF', label="",linewidth=4)

    ax.plot(data45B['wavelength'], np.log10(data45B['flux']*10**9.), '-',c='#39568CFF', label="",linewidth=4)
    ax.plot(data45R['wavelength'], np.log10(data45R['flux']*10**9.), '-',c='#39568CFF', label="",linewidth=4)

    ax.plot(data65B['wavelength'], np.log10(data65B['flux']*10**9.6), '-',c='#440154FF', label="",linewidth=4)
    ax.plot(data65R['wavelength'], np.log10(data65R['flux']*10**9.6), '-',c='#440154FF', label="",linewidth=4)

    ax.minorticks_on()
    ax.tick_params(direction='in', which='major', length=8, width=1.5, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax.tick_params(direction='in', which='minor', length=5, width=1.2, \
                   bottom=True, top=True, left=True, right=True, labelsize=26)
    ax.set_yticks([])
    ax.set_xlim(999.,9001.)
    ax.set_ylim(-1.9,10)
    ax.set_xlabel(r'Wavelength [$\AA$]', fontsize=26)
    ax.set_ylabel('Normalized flux', fontsize=26)
    plt.xticks(fontsize=26)
    plt.yticks(fontsize=26)
    ax.set_xticks([1500,2500,3500,4500,5500,6500,7500,8500])

    fig.text(0.9, 0.185,r'10000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.345,r'15000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.50, r'20000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.652,r'25000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.77, r'30000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.830,r'35000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.883,r'45000 K', fontsize=26, ha='center', va='center', rotation='horizontal')
    fig.text(0.9, 0.932,r'65000 K', fontsize=26, ha='center', va='center', rotation='horizontal')

    fig.savefig('./fig_spectra_cobertura.png', dpi=400, bbox_inches = 'tight')
