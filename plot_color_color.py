import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns


def plot_color_color_diagram(ms_color, \
                             gb_color, \
                             rhb_color,\
                             bs_color, \
                             bhb_color,\
                             ehb_color,\
                             path, name):
    xmin, xmax, ymin, ymax = (-5.2, 10.2, -2.5, 3.5)


    fig, axs = plt.subplots(sharex=False, figsize=(16,24), tight_layout=True,\
                            nrows=3, ncols=2)


    axs[0,0].scatter( ms_color['F275W_F438W'], ms_color['F275W_F336W'], marker='o', s=50, c='#cccc00',label='MS')
    axs[0,0].scatter( gb_color['F275W_F438W'], gb_color['F275W_F336W'], marker='o', s=50, c='#00cccc',label='gb')
    axs[0,0].scatter(bhb_color['F275W_F438W'],bhb_color['F275W_F336W'], marker='o', s=50, c='#800080',label='HB')
    axs[0,0].scatter(ehb_color['F275W_F438W'],ehb_color['F275W_F336W'], marker='o', s=50, c='#ff00ff',label='EHB')
    axs[0,0].scatter( bs_color['F275W_F438W'], bs_color['F275W_F336W'], marker='o', s=50, c='#0000ff',label='bs')
    axs[0,0].scatter(rhb_color['F275W_F438W'],rhb_color['F275W_F336W'], marker='o', s=50, c='#ff0000',label='RC')
    axs[0,0].set_xlim(xmin, xmax)
    axs[0,0].set_ylim(ymin, ymax)
    axs[0,0].set_ylabel('F275W - F336W', fontsize=20)
    axs[0,0].set_xlabel('F275W - F438W', fontsize=20)
    axs[0,0].minorticks_on()
    axs[0,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,0].get_xticklabels(), fontsize=20)
    plt.setp(axs[0,0].get_yticklabels(), fontsize=20)

    axs[0,1].scatter( ms_color['F438W_F606W'], ms_color['F438W_F814W'], marker='o', s=50, c='#cccc00',label='MS')
    axs[0,1].scatter( gb_color['F438W_F606W'], gb_color['F438W_F814W'], marker='o', s=50, c='#00cccc',label='gb')
    axs[0,1].scatter(bhb_color['F438W_F606W'],bhb_color['F438W_F814W'], marker='o', s=50, c='#800080',label='HB')
    axs[0,1].scatter(ehb_color['F438W_F606W'],ehb_color['F438W_F814W'], marker='o', s=50, c='#ff00ff',label='EHB')
    axs[0,1].scatter( bs_color['F438W_F606W'], bs_color['F438W_F814W'], marker='o', s=50, c='#0000ff',label='bs')
    axs[0,1].scatter(rhb_color['F438W_F606W'],rhb_color['F438W_F814W'], marker='o', s=50, c='#ff0000',label='RC')
    axs[0,1].set_xlim(xmin, xmax)
    axs[0,1].set_ylim(ymin, ymax)
    axs[0,1].set_ylabel('F438W - F815W', fontsize=20)
    axs[0,1].set_xlabel('F438W - F606W', fontsize=20)
    axs[0,1].minorticks_on()
    axs[0,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[0,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[0,1].get_xticklabels(), fontsize=20)
    plt.setp(axs[0,1].get_yticklabels(), fontsize=20)

    axs[1,0].scatter( ms_color['F438W_F606W'], ms_color['F336W_F606W'], marker='o', s=50, c='#cccc00',label='MS')
    axs[1,0].scatter( gb_color['F438W_F606W'], gb_color['F336W_F606W'], marker='o', s=50, c='#00cccc',label='gb')
    axs[1,0].scatter(bhb_color['F438W_F606W'],bhb_color['F336W_F606W'], marker='o', s=50, c='#800080',label='HB')
    axs[1,0].scatter(ehb_color['F438W_F606W'],ehb_color['F336W_F606W'], marker='o', s=50, c='#ff00ff',label='EHB')
    axs[1,0].scatter( bs_color['F438W_F606W'], bs_color['F336W_F606W'], marker='o', s=50, c='#0000ff',label='bs')
    axs[1,0].scatter(rhb_color['F438W_F606W'],rhb_color['F336W_F606W'], marker='o', s=50, c='#ff0000',label='RC')
    axs[1,0].set_xlim(xmin, xmax)
    axs[1,0].set_ylim(ymin, ymax)
    axs[1,0].set_ylabel('F336W - F606W', fontsize=20)
    axs[1,0].set_xlabel('F438W - F606W', fontsize=20)
    axs[1,0].minorticks_on()
    axs[1,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,0].get_xticklabels(), fontsize=20)
    plt.setp(axs[1,0].get_yticklabels(), fontsize=20)

    axs[1,1].scatter( ms_color['F336W_F438W'], ms_color['F438W_F606W'], marker='o', s=50, c='#cccc00',label='MS')
    axs[1,1].scatter( gb_color['F336W_F438W'], gb_color['F438W_F606W'], marker='o', s=50, c='#00cccc',label='gb')
    axs[1,1].scatter(bhb_color['F336W_F438W'],bhb_color['F438W_F606W'], marker='o', s=50, c='#800080',label='HB')
    axs[1,1].scatter(ehb_color['F336W_F438W'],ehb_color['F438W_F606W'], marker='o', s=50, c='#ff00ff',label='EHB')
    axs[1,1].scatter( bs_color['F336W_F438W'], bs_color['F438W_F606W'], marker='o', s=50, c='#0000ff',label='bs')
    axs[1,1].scatter(rhb_color['F336W_F438W'],rhb_color['F438W_F606W'], marker='o', s=50, c='#ff0000',label='RC')
    axs[1,1].set_xlim(xmin, xmax)
    axs[1,1].set_ylim(ymin, ymax)
    axs[1,1].set_ylabel('F438W - F606W', fontsize=20)
    axs[1,1].set_xlabel('F336W - F438W', fontsize=20)
    axs[1,1].minorticks_on()
    axs[1,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[1,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[1,1].get_xticklabels(), fontsize=20)
    plt.setp(axs[1,1].get_yticklabels(), fontsize=20)

    axs[2,0].scatter( ms_color['F275W_F814W'], ms_color['F275W_F336W'], marker='o', s=50, c='#cccc00',label='MS')
    axs[2,0].scatter( gb_color['F275W_F814W'], gb_color['F275W_F336W'], marker='o', s=50, c='#00cccc',label='gb')
    axs[2,0].scatter(bhb_color['F275W_F814W'],bhb_color['F275W_F336W'], marker='o', s=50, c='#800080',label='HB')
    axs[2,0].scatter(ehb_color['F275W_F814W'],ehb_color['F275W_F336W'],  marker='o', s=50, c='#ff00ff',label='EHB')
    axs[2,0].scatter( bs_color['F275W_F814W'], bs_color['F275W_F336W'], marker='o', s=50, c='#0000ff',label='bs')
    axs[2,0].scatter(rhb_color['F275W_F814W'],rhb_color['F275W_F336W'], marker='o', s=50, c='#ff0000',label='RC')
    axs[2,0].set_xlim(xmin, xmax)
    axs[2,0].set_ylim(ymin, ymax)
    axs[2,0].set_ylabel('F275W - F336W', fontsize=20)
    axs[2,0].set_xlabel('F275W - F814W', fontsize=20)
    axs[2,0].minorticks_on()
    axs[2,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,0].get_xticklabels(), fontsize=20)
    plt.setp(axs[2,0].get_yticklabels(), fontsize=20)

    axs[2,1].scatter(0,0, marker='o', s=50, c='#cccc00',label='MS')
    axs[2,1].scatter(0,0, marker='o', s=50, c='#00cccc',label='gb')
    axs[2,1].scatter(0,0, marker='o', s=50, c='#800080',label='HB')
    axs[2,1].scatter(0,0, marker='o', s=50, c='#ff00ff',label='EHB')
    axs[2,1].scatter(0,0, marker='o', s=50, c='#0000ff',label='bs')
    axs[2,1].scatter(0,0, marker='o', s=50, c='#ff0000',label='RC')
    axs[2,1].set_xlim(xmin, xmax)
    axs[2,1].set_ylim(ymin, ymax)
    axs[2,1].set_ylabel('', fontsize=20)
    axs[2,1].set_xlabel('', fontsize=20)
    axs[2,1].minorticks_on()
    axs[2,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axs[2,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    plt.setp(axs[2,1].get_xticklabels(), fontsize=20)
    plt.setp(axs[2,1].get_yticklabels(), fontsize=20)


    plt.savefig(path+'CCD_'+name+'.png', dpi=300, bbox_inches = 'tight')
