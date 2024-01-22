import pandas as pd
import numpy as np 

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from seaborn import jointplot


def plot_density_diagram(ms_color, distance_ms, \
                         gb_color, distance_gb, \
                         rhb_color,distance_rhb,\
                         bs_color, distance_bs, \
                         bhb_color,distance_bhb,\
                         ehb_color,distance_ehb,\
                         coelho_color, \
                         pacheco_color, \
                         path, name):
    xmin, xmax, ymin, ymax = (-4.2, 10.2, -2.2, 3.2)

    fig, axs = plt.subplots(sharex=False, figsize=(10,15), tight_layout=False,\
                                nrows=3, ncols=2)
    sns.kdeplot(data= gb_color, x='F275W_F438W',y='F275W_F336W', color='#009988',fill=True,ax=axs[0,0])
    sns.kdeplot(data= bs_color, x='F275W_F438W',y='F275W_F336W', color='#0077BB',fill=True,ax=axs[0,0])
    sns.kdeplot(data= ms_color, x='F275W_F438W',y='F275W_F336W', color='#EE7733',fill=True,ax=axs[0,0])
    sns.kdeplot(data=rhb_color, x='F275W_F438W',y='F275W_F336W', color='#CC3311',fill=True,ax=axs[0,0])
    sns.kdeplot(data=bhb_color, x='F275W_F438W',y='F275W_F336W', color='#EE3377',fill=True,ax=axs[0,0])
    sns.kdeplot(data=ehb_color, x='F275W_F438W',y='F275W_F336W', color='#33BBEE',fill=True,ax=axs[0,0])
    axs[0,0].scatter( coelho_color['F275W_F438W'], coelho_color['F275W_F336W'], marker='X', s=40, 
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.7)
    axs[0,0].scatter(pacheco_color['F275W_F438W'],pacheco_color['F275W_F336W'], marker='D', s=40, 
                     facecolors='#000000', edgecolors='#BBBBBB', alpha=0.7)
    axs[0,0].set_xlim(-3.1, 4.1)
    axs[0,0].set_ylim(-1.1, 2.9)
    axs[0,0].set_ylabel('F275W - F336W', fontsize=24)
    axs[0,0].set_xlabel('F275W - F438W', fontsize=24)
    axs[0,0].minorticks_on()
    axs[0,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[0,0].get_yticklabels(), fontsize=24)

    sns.kdeplot(data= gb_color, x='F275W_F814W', y='F438W_F814W', color='#009988',fill=True,ax=axs[0,1])
    sns.kdeplot(data= bs_color, x='F275W_F814W', y='F438W_F814W', color='#0077BB',fill=True,ax=axs[0,1])
    sns.kdeplot(data= ms_color, x='F275W_F814W', y='F438W_F814W', color='#EE7733',fill=True,ax=axs[0,1])
    sns.kdeplot(data=rhb_color, x='F275W_F814W', y='F438W_F814W', color='#CC3311',fill=True,ax=axs[0,1])
    sns.kdeplot(data=bhb_color, x='F275W_F814W', y='F438W_F814W', color='#EE3377',fill=True,ax=axs[0,1])
    sns.kdeplot(data=ehb_color, x='F275W_F814W', y='F438W_F814W', color='#33BBEE',fill=True,ax=axs[0,1])
    axs[0,1].scatter( coelho_color['F275W_F814W'], coelho_color['F438W_F814W'], marker='X', s=40, 
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.7)
    axs[0,1].scatter(pacheco_color['F275W_F814W'],pacheco_color['F438W_F814W'],  marker='D', s=40, 
                     facecolors='#000000', edgecolors='#BBBBBB', alpha=0.7)    
    axs[0,1].set_xlim(-4.3, 7.1)
    axs[0,1].set_ylim(-1.1, 2.9)
    axs[0,1].set_ylabel('F438W - F814W', fontsize=24)
    axs[0,1].set_xlabel('F275W - F814W', fontsize=24)
    axs[0,1].minorticks_on()
    axs[0,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[0,1].get_yticklabels(), fontsize=24)

    sns.kdeplot(data= gb_color, x='F336W_F606W',y='F606W_F814W',color='#009988',fill=True,ax=axs[1,0])
    sns.kdeplot(data= bs_color, x='F336W_F606W',y='F606W_F814W',color='#0077BB',fill=True,ax=axs[1,0])
    sns.kdeplot(data= ms_color, x='F336W_F606W',y='F606W_F814W',color='#EE7733',fill=True,ax=axs[1,0])
    sns.kdeplot(data=rhb_color, x='F336W_F606W',y='F606W_F814W',color='#CC3311',fill=True,ax=axs[1,0])
    sns.kdeplot(data=bhb_color, x='F336W_F606W',y='F606W_F814W',color='#EE3377',fill=True,ax=axs[1,0])
    sns.kdeplot(data=ehb_color, x='F336W_F606W',y='F606W_F814W',color='#33BBEE',fill=True,ax=axs[1,0])
    axs[1,0].scatter( coelho_color['F336W_F606W'], coelho_color['F606W_F814W'], marker='X', s=40, 
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.7)
    axs[1,0].scatter(pacheco_color['F336W_F606W'],pacheco_color['F606W_F814W'], marker='D', s=40, 
                     facecolors='#000000', edgecolors='#BBBBBB', alpha=0.7)
    axs[1,0].set_xlim(-3.1, 4.1)
    axs[1,0].set_ylim(-.8, 2.1)
    axs[1,0].set_ylabel('F606W - F814W', fontsize=24)
    axs[1,0].set_xlabel('F275W - F606W', fontsize=24)
    axs[1,0].minorticks_on()
    axs[1,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[1,0].get_yticklabels(), fontsize=24)


    sns.kdeplot(data= gb_color, x='F275W_F606W',y='F438W_F606W',color='#009988',fill=True,ax=axs[1,1])
    sns.kdeplot(data= bs_color, x='F275W_F606W',y='F438W_F606W',color='#0077BB',fill=True,ax=axs[1,1])
    sns.kdeplot(data= ms_color, x='F275W_F606W',y='F438W_F606W',color='#EE7733',fill=True,ax=axs[1,1])
    sns.kdeplot(data=rhb_color, x='F275W_F606W',y='F438W_F606W',color='#CC3311',fill=True,ax=axs[1,1])
    sns.kdeplot(data=bhb_color, x='F275W_F606W',y='F438W_F606W',color='#EE3377',fill=True,ax=axs[1,1])
    sns.kdeplot(data=ehb_color, x='F275W_F606W',y='F438W_F606W',color='#33BBEE',fill=True,ax=axs[1,1])
    axs[1,1].scatter( coelho_color['F275W_F606W'], coelho_color['F438W_F606W'], marker='X', s=40, 
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.7)
    axs[1,1].scatter(pacheco_color['F275W_F606W'],pacheco_color['F438W_F606W'],  marker='D', s=40, 
                     facecolors='#000000', edgecolors='#BBBBBB', alpha=0.7)
    axs[1,1].set_xlim(-4.3, 7.1)
    axs[1,1].set_ylim(-.8, 2.1)
    axs[1,1].set_ylabel('F438W - F606W', fontsize=24)
    axs[1,1].set_xlabel('F336W - F606W', fontsize=24)
    axs[1,1].minorticks_on()
    axs[1,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[1,1].get_yticklabels(), fontsize=24)


    sns.kdeplot(data= gb_color, x='F336W_F814W',y='F336W_F438W', color='#009988',fill=True,ax=axs[2,0])
    sns.kdeplot(data= bs_color, x='F336W_F814W',y='F336W_F438W', color='#0077BB',fill=True,ax=axs[2,0])
    sns.kdeplot(data= ms_color, x='F336W_F814W',y='F336W_F438W', color='#EE7733',fill=True,ax=axs[2,0])
    sns.kdeplot(data=rhb_color, x='F336W_F814W',y='F336W_F438W', color='#CC3311',fill=True,ax=axs[2,0])
    sns.kdeplot(data=bhb_color, x='F336W_F814W',y='F336W_F438W', color='#EE3377',fill=True,ax=axs[2,0])
    sns.kdeplot(data=ehb_color, x='F336W_F814W',y='F336W_F438W', color='#33BBEE',fill=True,ax=axs[2,0])
    axs[2,0].scatter( coelho_color['F336W_F814W'], coelho_color['F336W_F438W'], marker='X', s=40, 
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.7)
    axs[2,0].scatter(pacheco_color['F336W_F814W'],pacheco_color['F336W_F438W'], marker='D', s=40, 
                     facecolors='#000000', edgecolors='#BBBBBB', alpha=0.7)
    axs[2,0].set_xlim(-3.1, 4.1)
    axs[2,0].set_ylim(-2.4, 1.1)
    axs[2,0].set_ylabel('F336W - F438W', fontsize=24)
    axs[2,0].set_xlabel('F336W - F814W', fontsize=24)
    axs[2,0].minorticks_on()
    axs[2,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[2,0].get_yticklabels(), fontsize=24)

  
    sns.histplot(data=distance_ms, x='ms', alpha=0.15, color='#EE7733', ax=axs[2,1], linewidth=3, 
                 kde=False, stat='percent', binwidth=0.1, element = "step", label='MS')
    sns.histplot(data=distance_gb, x='gb', alpha=0.15, color='#009988', ax=axs[2,1], linewidth=3, 
                 kde=False, stat='percent', binwidth=0.1, element = "step", label='GB')
    sns.histplot(data=distance_rhb, x='rhb',alpha=0.15, color='#CC3311', ax=axs[2,1], linewidth=3, 
                 kde=False, stat='percent', binwidth=0.1, element = "step", label='RHB')
    sns.histplot(data=distance_bs, x='bs', alpha=0.15, color='#0077BB', ax=axs[2,1], linewidth=3, 
                 kde=False, stat='percent', binwidth=0.1, element = "step", label='BS')
    sns.histplot(data=distance_bhb, x='bhb',alpha=0.15, color='#33BBEE', ax=axs[2,1], linewidth=3,  
                 kde=False, stat='percent', binwidth=0.1, element = "step", label='BHB')
    sns.histplot(data=distance_ehb, x='ehb',alpha=0.15, color='#EE3377', ax=axs[2,1], linewidth=3, 
                 kde=False, stat='percent', binwidth=0.1, element = "step", label='EHB')
    axs[2,1].set_ylabel('($\%$)', fontsize=24)
    axs[2,1].set_xlabel('Distance [mag]', fontsize=24)
    axs[2,1].set_xlim(0, 1.1)  
    axs[2,1].minorticks_on()
    axs[2,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[2,1].get_yticklabels(), fontsize=24)


    plt.savefig(path+'DensityCCD_'+name+'.png', dpi=300, bbox_inches = 'tight')
