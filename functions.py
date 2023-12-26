import numpy as np
import pandas as pd

import sys
sys.path.append('../SSPmodels/codeModule/utilsSpecMod/')
from photoColors import apply_evolutionary_phase_mask
from photoColors import apply_reddening


def evolutionary_phase_mask(mag, cutoff):
    
    mag_evolutionary_phase = pd.DataFrame()
    mag_evolutionary_phase['F275W'] = mag['F275W'][cutoff]
    mag_evolutionary_phase['F336W'] = mag['F336W'][cutoff]
    mag_evolutionary_phase['F438W'] = mag['F438W'][cutoff]
    mag_evolutionary_phase['F606W'] = mag['F606W'][cutoff]
    mag_evolutionary_phase['F814W'] = mag['F814W'][cutoff]

    return mag_evolutionary_phase
  

def catch_magnitudes(input):
    
    mags = pd.DataFrame()
    mags['F275W'] = input['F275W']
    mags['F336W'] = input['F336W']
    mags['F438W'] = input['F438W']
    mags['F606W'] = input['F606W']
    mags['F814W'] = input['F814W']
    return mags


def dereddening(mag, reddening):

    obs_mag = pd.DataFrame()
    obs_mag['F275W'] = mag['F275W'] - reddening[0]
    obs_mag['F336W'] = mag['F336W'] - reddening[1]
    obs_mag['F438W'] = mag['F438W'] - reddening[2]
    obs_mag['F606W'] = mag['F606W'] - reddening[3]
    obs_mag['F814W'] = mag['F814W'] - reddening[4]

    return obs_mag



def color_magnitude(photometry_gc, phase, cutoff,\
                    color_input, reddening, extinction):

    cutoff_phase = np.where(cutoff & photometry_gc[phase] == True)[0]
    color_phase = apply_evolutionary_phase_mask(color_input, cutoff_phase)
    color = apply_reddening(color_phase, extinction)
    mag_phase = evolutionary_phase_mask(photometry_gc, cutoff_phase)
    mag = dereddening(mag_phase,reddening)

    return color, mag