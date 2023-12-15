import numpy as np
import pandas as pd
import extinction 


def evolutionary_phase_mask(mag, cutoff):
    
    mag_evolutionary_phase = pd.DataFrame()
    mag_evolutionary_phase['F275W'] = mag['F275W'][cutoff]
    mag_evolutionary_phase['F336W'] = mag['F336W'][cutoff]
    mag_evolutionary_phase['F438W'] = mag['F438W'][cutoff]
    mag_evolutionary_phase['F606W'] = mag['F606W'][cutoff]
    mag_evolutionary_phase['F814W'] = mag['F814W'][cutoff]

    return mag_evolutionary_phase
  

def reddening(mag, reddening):

    obs_mag = pd.DataFrame()
    obs_mag['F275W'] = mag['F275W'] - reddening[0]
    obs_mag['F336W'] = mag['F336W'] - reddening[1]
    obs_mag['F438W'] = mag['F438W'] - reddening[2]
    obs_mag['F606W'] = mag['F606W'] - reddening[3]
    obs_mag['F814W'] = mag['F814W'] - reddening[4]

    return obs_mag