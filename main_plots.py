
from math import *
import pandas as pd
import numpy as np

import plot_CMDs as cmd
import plot_color_color as ccd
import functions as apply

import sys
sys.path.append('../SSPmodels/codeModule/utilsSpecMod/')
from photoColors import get_reddening
from photoColors import compute_color_extinction 
from photoColors import calculate_colors

nameGC = 'NGC7089'
color_excess_B_V = 0.06
path = '../SSPmodels/subsets_hugs_ngc7089_meth1.txt'
#path = '../SSPmodels/subsets_hugs_ngc2808_meth1.txt'
print("Globular Cluster: %s \n" %nameGC)

photometry_gc = pd.read_csv(path, engine='python', comment='#',
                            skip_blank_lines=True, delim_whitespace=True, 
                            names=['X', 'Y', 
                            'F275W', 'RMSF275W', 'QFITF275W', 'RADXSF275W', 'NfF275W', 'NgF275W', #col 3
                            'F336W', 'RMSF336W', 'QFITF336W', 'RADXSF336W', 'NfF336W', 'NgF336W', #col 9
                            'F438W', 'RMSF438W', 'QFITF438W', 'RADXSF438W', 'NfF438W', 'NgF438W', #col 15
                            'F606W', 'RMSF606W', 'QFITF606W', 'RADXSF606W', 'NfF606W', 'NgF606W', #col 21
                            'F814W', 'RMSF814W', 'QFITF814W', 'RADXSF814W', 'NfF814W', 'NgF814W', #col 27
                            'P', 'RA', 'DEC', 'ID', 'ITER', 'MS','GB','RHB','BS','BHB','EHB']) #col 33


print("\n Computing color excess")
print("E(B-V): %s" %color_excess_B_V)
reddening = get_reddening(color_excess_B_V)
extinction = compute_color_extinction(color_excess_B_V)

print("\n Calculating photometric colors from HST")
color = calculate_colors(photometry_gc)

cutoff = (photometry_gc['P'] > 90) & \
         (photometry_gc['RMSF275W'] < 0.07) & \
         (photometry_gc['RMSF336W'] < 0.05) & \
         (photometry_gc['RMSF438W'] < 0.04) & \
         (photometry_gc['RMSF606W'] < 0.03) & \
         (photometry_gc['RMSF814W'] < 0.03) & \
         (photometry_gc['F438W']!=99.9999)

ms_color, ms_mag = apply.color_magnitude(photometry_gc, 'MS', cutoff,\
                                         color, reddening, extinction)

gb_color, gb_mag = apply.color_magnitude(photometry_gc, 'GB', cutoff,\
                                         color, reddening, extinction)

rhb_color, rhb_mag = apply.color_magnitude(photometry_gc, 'RHB', cutoff,\
                                         color, reddening, extinction)

bs_color, bs_mag = apply.color_magnitude(photometry_gc, 'BS', cutoff,\
                                         color, reddening, extinction)

bhb_color, bhb_mag = apply.color_magnitude(photometry_gc, 'BHB', cutoff,\
                                         color, reddening, extinction)

ehb_color, ehb_mag = apply.color_magnitude(photometry_gc, 'EHB', cutoff,\
                                         color, reddening, extinction)

print("\n Plotting CMD: \n")
cmd.plot_color_magnitude_diagram(ms_color, ms_mag, \
                                 gb_color, gb_mag, \
                                 rhb_color,rhb_mag,\
                                 bs_color, bs_mag, \
                                 bhb_color,bhb_mag,\
                                 ehb_color,ehb_mag,\
                                 './', nameGC)

print("\n Plotting color-color diagram: \n")
ccd.plot_color_color_diagram(ms_color, \
                             gb_color, \
                             rhb_color,\
                             bs_color, \
                             bhb_color,\
                             ehb_color,\
                             './', nameGC)