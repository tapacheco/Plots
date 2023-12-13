
from math import *
import pandas as pd
import numpy as np

import plot_CMDs

import sys
sys.path.append('../SSPmodels/codeModule/utilsSpecMod/')
from photoColors import get_reddening
from photoColors import compute_color_extinction 
from photoColors import calculate_colors


nameGC = 'NGC2808'
color_excess_B_V = 0.22
path = '/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/subsets_hugs_ngc2808_meth1.txt'

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
color = calculate_colors(photometry_gc['MS'])
