import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import gridspec
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns


def plot_color_magnitude_diagram(ms_color, gb_color, rhb_color,\
                              bs_color, bhb_color, ehb_color, \
                              path):
    xmin, xmax, ymax, ymin = (-2.2,3.4,27.4,10.4)

    fig, axt = plt.subplots(sharex=True, figsize=(8,8), tight_layout=True)
    #PLOT 
    plt.minorticks_on()


    plt.scatter(ms_color['F275W_F336W'],  ms_color['F275W'], label='Main Sequence', marker='>', s=2, c='#EE7733')#orange
    plt.scatter(gb_color['F275W_F336W'],  gb_color['F275W'], label='Giant Branches', marker='^', s=2, c='#009988')#teal
    plt.scatter(rhb_color['F275W_F336W'],rhb_color['F275W'], label='Red Horizontal Branch', marker='<', s=2, c='#CC3311')#red
    plt.scatter(bs_color['F275W_F336W'],  bs_color['F275W'], label='Blue Straggler', marker='*', s=2, c='#0077BB')#blue
    plt.scatter(bhb_color['F275W_F336W'],bhb_color['F275W'], label='Blue Horizontal Branch', marker='o', s=2, c='#EE3377')#magenta
    plt.scatter(ehb_color['F275W_F336W'],ehb_color['F275W'], label='Extreme Horizontal Branch', marker='s', s=2, c='#33BBEE')#cyan
    #plt.scatter(cor, mag, marker='o', c='purple')

    axt.legend(fontsize=16)
    axt.set_xlim(xmin, xmax)
    axt.set_ylim(ymax, ymin)
    plt.title("", fontsize=30)
    plt.ylabel('F275W', fontsize=22)
    plt.xlabel('F275W - F336W', fontsize=22)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.tick_params(direction='in', which='major', length=8, width=1.5, \
                    bottom=True, top=True, left=True, right=True)
    plt.tick_params(direction='in', which='minor', length=5, width=1.2, \
                    bottom=True, top=True, left=True, right=True)

    #plt.show()
    plt.savefig(path+'CMD1.png', dpi=300, bbox_inches = 'tight')
