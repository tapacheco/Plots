
from math import *
import pandas as pd
import numpy as np

import plot_CMDs as cmd
import functions as apply

import sys
sys.path.append('../SSPmodels/codeModule/utilsSpecMod/')
from photoColors import get_reddening
from photoColors import compute_color_extinction 
from photoColors import calculate_colors
from photoColors import apply_evolutionary_phase_mask
from photoColors import apply_reddening

nameGC = 'NGC2808'
color_excess_B_V = 0.22
path = '../SSPmodels/subsets_hugs_ngc2808_meth1.txt'

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

cutoff_ms = np.where(cutoff & photometry_gc['MS'] == True)[0]
color_ms_phase = apply_evolutionary_phase_mask(color, cutoff_ms)
ms_color = apply_reddening(color_ms_phase, extinction)
mag_ms_phase = apply.evolutionary_phase_mask(photometry_gc,cutoff_ms)
ms_mag = apply.reddening(mag_ms_phase,reddening)

cutoff_gb = np.where(cutoff & photometry_gc['GB'] == True)[0]
color_gb_phase = apply_evolutionary_phase_mask(color, cutoff_gb)
gb_color = apply_reddening(color_gb_phase, extinction)
mag_gb_phase = apply.evolutionary_phase_mask(photometry_gc,cutoff_gb)
gb_mag = apply.reddening(mag_gb_phase,reddening)

cutoff_rhb = np.where(cutoff & photometry_gc['RHB'] == True)[0]
color_rhb_phase = apply_evolutionary_phase_mask(color, cutoff_rhb)
rhb_color = apply_reddening(color_rhb_phase, extinction)
mag_rhb_phase = apply.evolutionary_phase_mask(photometry_gc,cutoff_rhb)
rhb_mag = apply.reddening(mag_rhb_phase,reddening)

cutoff_bs = np.where(cutoff & photometry_gc['BS'] == True)[0]
color_bs_phase = apply_evolutionary_phase_mask(color, cutoff_bs)
bs_color = apply_reddening(color_bs_phase, extinction)
mag_bs_phase = apply.evolutionary_phase_mask(photometry_gc,cutoff_bs)
bs_mag = apply.reddening(mag_bs_phase,reddening)

cutoff_bhb = np.where(cutoff & photometry_gc['BHB'] == True)[0]
color_bhb_phase = apply_evolutionary_phase_mask(color, cutoff_bhb)
bhb_color = apply_reddening(color_bhb_phase, extinction)
mag_bhb_phase = apply.evolutionary_phase_mask(photometry_gc,cutoff_bhb)
bhb_mag = apply.reddening(mag_bhb_phase,reddening)

cutoff_ehb = np.where(cutoff & photometry_gc['EHB'] == True)[0]
color_ehb_phase = apply_evolutionary_phase_mask(color, cutoff_ehb)
ehb_color = apply_reddening(color_ehb_phase, extinction)
mag_ehb_phase = apply.evolutionary_phase_mask(photometry_gc,cutoff_ehb)
ehb_mag = apply.reddening(mag_ehb_phase,reddening)


cmd.plot_color_magnitude_diagram(ms_color, ms_mag, \
                                 gb_color, gb_mag, \
                                 rhb_color,rhb_mag,\
                                 bs_color, bs_mag, \
                                 bhb_color,bhb_mag,\
                                 ehb_color,ehb_mag,\
                                 './', nameGC)