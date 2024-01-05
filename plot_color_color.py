import pandas as pd
import numpy as np 

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns
from seaborn import jointplot


def plot_color_color_diagram(ms_color, \
                             gb_color, \
                             rhb_color,\
                             bs_color, \
                             bhb_color,\
                             ehb_color,\
                             coelho_color, \
                             pacheco_color, \
                             distance, \
                             path, name):
    xmin, xmax, ymin, ymax = (-4.2, 10.2, -2.2, 3.2)

    fig, axs = plt.subplots(sharex=False, figsize=(16,24), tight_layout=False,\
                                nrows=3, ncols=2)
 
    axs[0,0].scatter( ms_color['F275W_F438W'], ms_color['F275W_F336W'], marker='>', s=40, alpha=0.25,  c='#EE7733',label='MS')
    axs[0,0].scatter( gb_color['F275W_F438W'], gb_color['F275W_F336W'], marker='^', s=40, alpha=0.25,  c='#009988',label='gb')
    axs[0,0].scatter(rhb_color['F275W_F438W'],rhb_color['F275W_F336W'], marker='<', s=40, alpha=0.25,  c='#CC3311',label='RC')
    axs[0,0].scatter( bs_color['F275W_F438W'], bs_color['F275W_F336W'], marker='s', s=40, alpha=0.25,  c='#0077BB',label='bs')
    axs[0,0].scatter(bhb_color['F275W_F438W'],bhb_color['F275W_F336W'], marker='o', s=40, alpha=0.25,  c='#33BBEE',label='HB')
    axs[0,0].scatter(ehb_color['F275W_F438W'],ehb_color['F275W_F336W'], marker='*', s=40, alpha=0.25,  c='#EE3377',label='EHB')
    axs[0,0].scatter( coelho_color['F275W_F438W'], coelho_color['F275W_F336W'], marker='X', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[0,0].scatter(pacheco_color['F275W_F438W'],pacheco_color['F275W_F336W'], marker='D', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[0,0].set_xlim(-3.1, 6.1)
    axs[0,0].set_ylim(-1.1, 4.1)
    axs[0,0].set_ylabel('F275W - F336W', fontsize=24)
    axs[0,0].set_xlabel('F275W - F438W', fontsize=24)
    axs[0,0].minorticks_on()
    axs[0,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[0,0].get_yticklabels(), fontsize=24)

    axs[0,1].scatter( ms_color['F275W_F814W'], ms_color['F438W_F814W'], marker='>', s=40, alpha=0.25,  c='#EE7733',label='MS')
    axs[0,1].scatter( gb_color['F275W_F814W'], gb_color['F438W_F814W'], marker='^', s=40, alpha=0.25,  c='#009988',label='gb')
    axs[0,1].scatter(rhb_color['F275W_F814W'],rhb_color['F438W_F814W'], marker='<', s=40, alpha=0.25,  c='#CC3311',label='RC')
    axs[0,1].scatter( bs_color['F275W_F814W'], bs_color['F438W_F814W'], marker='s', s=40, alpha=0.25,  c='#0077BB',label='bs')
    axs[0,1].scatter(bhb_color['F275W_F814W'],bhb_color['F438W_F814W'], marker='o', s=40, alpha=0.25,  c='#33BBEE',label='HB')
    axs[0,1].scatter(ehb_color['F275W_F814W'],ehb_color['F438W_F814W'], marker='*', s=40, alpha=0.25,  c='#EE3377',label='EHB')
    axs[0,1].scatter( coelho_color['F275W_F814W'], coelho_color['F438W_F814W'], marker='X', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[0,1].scatter(pacheco_color['F275W_F814W'],pacheco_color['F438W_F814W'],  marker='D', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[0,1].set_xlim(-4.3, 9.6)
    axs[0,1].set_ylim(-1.1, 4.1)
    axs[0,1].set_ylabel('F438W - F814W', fontsize=24)
    axs[0,1].set_xlabel('F275W - F814W', fontsize=24)
    axs[0,1].minorticks_on()
    axs[0,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[0,1].get_yticklabels(), fontsize=24)

    axs[1,0].scatter( ms_color['F336W_F606W'], ms_color['F606W_F814W'], marker='>', s=40, alpha=0.25,  c='#EE7733',label='MS')
    axs[1,0].scatter( gb_color['F336W_F606W'], gb_color['F606W_F814W'], marker='^', s=40, alpha=0.25,  c='#009988',label='gb')
    axs[1,0].scatter(rhb_color['F336W_F606W'],rhb_color['F606W_F814W'], marker='<', s=40, alpha=0.25,  c='#CC3311',label='RC')
    axs[1,0].scatter( bs_color['F336W_F606W'], bs_color['F606W_F814W'], marker='s', s=40, alpha=0.25,  c='#0077BB',label='bs')
    axs[1,0].scatter(bhb_color['F336W_F606W'],bhb_color['F606W_F814W'], marker='o', s=40, alpha=0.25,  c='#33BBEE',label='HB')
    axs[1,0].scatter(ehb_color['F336W_F606W'],ehb_color['F606W_F814W'], marker='*', s=40, alpha=0.25,  c='#EE3377',label='EHB')
    axs[1,0].scatter( coelho_color['F336W_F606W'], coelho_color['F606W_F814W'], marker='X', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[1,0].scatter(pacheco_color['F336W_F606W'],pacheco_color['F606W_F814W'], marker='D', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[1,0].set_xlim(-3.1, 6.1)
    axs[1,0].set_ylim(-.8, 3.1)
    axs[1,0].set_ylabel('F606W - F814W', fontsize=24)
    axs[1,0].set_xlabel('F275W - F606W', fontsize=24)
    axs[1,0].minorticks_on()
    axs[1,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[1,0].get_yticklabels(), fontsize=24)

    axs[1,1].scatter( ms_color['F275W_F606W'], ms_color['F438W_F606W'], marker='>', s=40, alpha=0.25,  c='#EE7733',label='MS')
    axs[1,1].scatter( gb_color['F275W_F606W'], gb_color['F438W_F606W'], marker='^', s=40, alpha=0.25,  c='#009988',label='gb')
    axs[1,1].scatter(rhb_color['F275W_F606W'],rhb_color['F438W_F606W'], marker='<', s=40, alpha=0.25,  c='#CC3311',label='RC')
    axs[1,1].scatter( bs_color['F275W_F606W'], bs_color['F438W_F606W'], marker='s', s=40, alpha=0.25,  c='#0077BB',label='bs')
    axs[1,1].scatter(bhb_color['F275W_F606W'],bhb_color['F438W_F606W'], marker='o', s=40, alpha=0.25,  c='#33BBEE',label='HB')
    axs[1,1].scatter(ehb_color['F275W_F606W'],ehb_color['F438W_F606W'], marker='*', s=40, alpha=0.25,  c='#EE3377',label='EHB')
    axs[1,1].scatter( coelho_color['F275W_F606W'], coelho_color['F438W_F606W'], marker='X', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[1,1].scatter(pacheco_color['F275W_F606W'],pacheco_color['F438W_F606W'],  marker='D', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[1,1].set_xlim(-4.3, 9.6)
    axs[1,1].set_ylim(-.8, 3.1)
    axs[1,1].set_ylabel('F438W - F606W', fontsize=24)
    axs[1,1].set_xlabel('F336W - F606W', fontsize=24)
    axs[1,1].minorticks_on()
    axs[1,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[1,1].get_yticklabels(), fontsize=24)

    axs[2,0].scatter( ms_color['F336W_F814W'], ms_color['F336W_F438W'], marker='>', s=40, alpha=0.25,  c='#EE7733',label='MS')
    axs[2,0].scatter( gb_color['F336W_F814W'], gb_color['F336W_F438W'], marker='^', s=40, alpha=0.25,  c='#009988',label='gb')
    axs[2,0].scatter(rhb_color['F336W_F814W'],rhb_color['F336W_F438W'], marker='<', s=40, alpha=0.25,  c='#CC3311',label='RC')
    axs[2,0].scatter( bs_color['F336W_F814W'], bs_color['F336W_F438W'], marker='s', s=40, alpha=0.25,  c='#0077BB',label='bs')
    axs[2,0].scatter(bhb_color['F336W_F814W'],bhb_color['F336W_F438W'], marker='o', s=40, alpha=0.25,  c='#33BBEE',label='HB')
    axs[2,0].scatter(ehb_color['F336W_F814W'],ehb_color['F336W_F438W'], marker='*', s=40, alpha=0.25,  c='#EE3377',label='EHB')
    axs[2,0].scatter( coelho_color['F336W_F814W'], coelho_color['F336W_F438W'], marker='X', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[2,0].scatter(pacheco_color['F336W_F814W'],pacheco_color['F336W_F438W'], marker='D', s=40,  
                     facecolors='#BBBBBB', edgecolors='#000000', alpha=0.25)
    axs[2,0].set_xlim(-3.1, 6.1)
    axs[2,0].set_ylim(-2.2, 2.7)
    axs[2,0].set_ylabel('F336W - F438W', fontsize=24)
    axs[2,0].set_xlabel('F336W - F814W', fontsize=24)
    axs[2,0].minorticks_on()
    axs[2,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,0].get_xticklabels(), fontsize=24)
    plt.setp(axs[2,0].get_yticklabels(), fontsize=24)

 #   sns.histplot(data=distance, x='ms', color='#EE7733', ax=axs[2,1], 
 #                binwidth=0.1, element = "step", label='MS')
#    sns.histplot(data=distance, x='gb', alpha=0.25, color='#009988', ax=axs[2,1], kde=True, 
#                 binwidth=0.1, element = "step", label='GB')
#    sns.histplot(data=distance, x='rhb',alpha=0.25, color='#CC3311', ax=axs[2,1], kde=True, 
#                 binwidth=0.1, element = "step", label='RHB')
#    sns.histplot(data=distance, x='bs', alpha=0.25, color='#0077BB', ax=axs[2,1], kde=True, 
#                 binwidth=0.1, element = "step", label='BS')
#    sns.histplot(data=distance, x='bhb',alpha=0.25, color='#33BBEE', ax=axs[2,1], kde=True, 
#                 binwidth=0.1, element = "step", label='BHB')
    sns.histplot(data=distance, x='ehb',alpha=0.25, color='#EE3377', ax=axs[2,1], kde=True, 
                 binwidth=0.1, element = "step", label='EHB')
    axs[2,1].set_ylabel('', fontsize=24)
    axs[2,1].set_xlabel('', fontsize=24)
    axs[2,1].minorticks_on()
    axs[2,1].set_xlim(0, 5)  
    axs[2,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,1].get_xticklabels(), fontsize=24)
    plt.setp(axs[2,1].get_yticklabels(), fontsize=24)


    plt.savefig(path+'CCD_'+name+'.png', dpi=300, bbox_inches = 'tight')
