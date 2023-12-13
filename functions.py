import numpy as np
import pandas as pd
import extinction 

def apply_evolutionary_phase_mask(color, cutoff):
    
    color_evolutionary_phase = pd.DataFrame()
    color_evolutionary_phase['F275W_F336W'] = color['F275W_F336W'][cutoff]
    color_evolutionary_phase['F275W_F438W'] = color['F275W_F438W'][cutoff]
    color_evolutionary_phase['F275W_F606W'] = color['F275W_F606W'][cutoff]
    color_evolutionary_phase['F275W_F814W'] = color['F275W_F814W'][cutoff]
    color_evolutionary_phase['F336W_F438W'] = color['F336W_F438W'][cutoff]
  
  def apply_reddening(color, reddening):

    obs_color = pd.DataFrame()
    obs_color['F275W_F336W'] = color['F275W_F336W'] - reddening['F275W_F336W']
    obs_color['F275W_F438W'] = color['F275W_F438W'] - reddening['F275W_F438W']
    obs_color['F275W_F606W'] = color['F275W_F606W'] - reddening['F275W_F606W']
    obs_color['F275W_F814W'] = color['F275W_F814W'] - reddening['F275W_F814W']
    obs_color['F336W_F438W'] = color['F336W_F438W'] - reddening['F336W_F438W']
