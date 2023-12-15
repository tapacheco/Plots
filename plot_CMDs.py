import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import gridspec
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns


def plot_color_magnitude_diagram(ms_color, ms_mag, \
                                 gb_color, gb_mag, \
                                 rhb_color,rhb_mag,\
                                 bs_color, bs_mag, \
                                 bhb_color,bhb_mag,\
                                 ehb_color,ehb_mag,\
                                 path, name):
    xmin, xmax, ymax, ymin = (-2.2,3.4,26.2,11.2)

    fig, axt = plt.subplots(sharex=False, figsize=(16,16), tight_layout=True,\
                            nrows=2, ncols=2)

    axt[0,0].scatter( ms_color['F275W_F336W'], ms_mag['F275W'], marker='>', s=5, c='#EE7733')#orange
    axt[0,0].scatter( gb_color['F275W_F336W'], gb_mag['F275W'], marker='^', s=5, c='#009988')#teal
    axt[0,0].scatter(rhb_color['F275W_F336W'],rhb_mag['F275W'], marker='<', s=5, c='#CC3311')#red
    axt[0,0].scatter( bs_color['F275W_F336W'], bs_mag['F275W'], marker='*', s=5, c='#0077BB')#blue
    axt[0,0].scatter(bhb_color['F275W_F336W'],bhb_mag['F275W'], marker='o', s=5, c='#EE3377')#magenta
    axt[0,0].scatter(ehb_color['F275W_F336W'],ehb_mag['F275W'], marker='s', s=5, c='#33BBEE')#cyan
    axt[0,0].set_xlim(xmin, xmax)
    axt[0,0].set_ylim(ymax, ymin)
    axt[0,0].set_ylabel('F275W', fontsize=24)
    axt[0,0].set_xlabel('F275W - F336W', fontsize=24)
    axt[0,0].minorticks_on()
    axt[0,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axt[0,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)



    axt[0,1].scatter( ms_color['F336W_F438W'], ms_mag['F336W'], marker='>', s=5, c='#EE7733')#orange
    axt[0,1].scatter( gb_color['F336W_F438W'], gb_mag['F336W'], marker='^', s=5, c='#009988')#teal
    axt[0,1].scatter(rhb_color['F336W_F438W'],rhb_mag['F336W'], marker='<', s=5, c='#CC3311')#red
    axt[0,1].scatter( bs_color['F336W_F438W'], bs_mag['F336W'], marker='*', s=5, c='#0077BB')#blue
    axt[0,1].scatter(bhb_color['F336W_F438W'],bhb_mag['F336W'], marker='o', s=5, c='#EE3377')#magenta
    axt[0,1].scatter(ehb_color['F336W_F438W'],ehb_mag['F336W'], marker='s', s=5, c='#33BBEE')#cyan
    axt[0,1].set_xlim(xmin, xmax)
    axt[0,1].set_ylim(ymax, ymin)
    axt[0,1].set_ylabel('F336W', fontsize=24)
    axt[0,1].set_xlabel('F336W - F438W', fontsize=24)
    axt[0,1].minorticks_on()
    axt[0,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axt[0,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)



    axt[1,0].scatter( ms_color['F438W_F606W'], ms_mag['F438W'], marker='>', s=5, c='#EE7733')#orange
    axt[1,0].scatter( gb_color['F438W_F606W'], gb_mag['F438W'], marker='^', s=5, c='#009988')#teal
    axt[1,0].scatter(rhb_color['F438W_F606W'],rhb_mag['F438W'], marker='<', s=5, c='#CC3311')#red
    axt[1,0].scatter( bs_color['F438W_F606W'], bs_mag['F438W'], marker='*', s=5, c='#0077BB')#blue
    axt[1,0].scatter(bhb_color['F438W_F606W'],bhb_mag['F438W'], marker='o', s=5, c='#EE3377')#magenta
    axt[1,0].scatter(ehb_color['F438W_F606W'],ehb_mag['F438W'], marker='s', s=5, c='#33BBEE')#cyan
    axt[1,0].set_xlim(xmin, xmax)
    axt[1,0].set_ylim(ymax, ymin)
    axt[1,0].set_ylabel('F438W', fontsize=24)
    axt[1,0].set_xlabel('F438W - F606W', fontsize=24)
    axt[1,0].minorticks_on()
    axt[1,0].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axt[1,0].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)



    axt[1,1].scatter( ms_color['F606W_F814W'], ms_mag['F606W'], marker='>', s=5, c='#EE7733')#orange
    axt[1,1].scatter( gb_color['F606W_F814W'], gb_mag['F606W'], marker='^', s=5, c='#009988')#teal
    axt[1,1].scatter(rhb_color['F606W_F814W'],rhb_mag['F606W'], marker='<', s=5, c='#CC3311')#red
    axt[1,1].scatter( bs_color['F606W_F814W'], bs_mag['F606W'], marker='*', s=5, c='#0077BB')#blue
    axt[1,1].scatter(bhb_color['F606W_F814W'],bhb_mag['F606W'], marker='o', s=5, c='#EE3377')#magenta
    axt[1,1].scatter(ehb_color['F606W_F814W'],ehb_mag['F606W'], marker='s', s=5, c='#33BBEE')#cyan
    axt[1,1].set_xlim(xmin, xmax)
    axt[1,1].set_ylim(ymax, ymin)
    axt[1,1].set_ylabel('F606W', fontsize=24)
    axt[1,1].set_xlabel('F606W - F814W', fontsize=24)
    axt[1,1].minorticks_on()
    axt[1,1].tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)
    axt[1,1].tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True, labelsize=26)


    plt.savefig(path+'CMD_'+name+'.png', dpi=300, bbox_inches = 'tight')
