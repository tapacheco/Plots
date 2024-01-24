import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import spectres 
from astropy.io import fits
from astropy.convolution import convolve_fft
from astropy.convolution import Gaussian1DKernel

w_min, w_max = (1100.1, 8999.9)

def degrade_resolving_power(file, resolution):
    data = pd.read_csv(file, engine='python', comment='#', skip_blank_lines=True, header=1,
                       delim_whitespace=True, names=['wavelength', 'flux'])
    wavelength = data['wavelength']
    flux = data['flux'] #erg/cm2/s/A

    wavelength_ln = np.linspace(np.log(min(wavelength)), np.log(max(wavelength-0.1)), num=len(wavelength))
    flux_equispaced = spectres.spectres(wavelength_ln, np.array(np.log(wavelength)), np.array(np.log10(flux)))
    
    delta_lambda = wavelength_ln[1] - wavelength_ln[0]
    sigma_convolution = 1/(np.sqrt(8*np.log(2)) * resolution * delta_lambda)
    #print(delta_lambda, sigma_convolution)
    gaussian_kernel = Gaussian1DKernel(sigma_convolution)
    convolved_flux = convolve_fft(flux_equispaced, gaussian_kernel)
    num_points = int(2*(w_max - w_min)/(5000/resolution))
    wavelength_output = np.linspace(w_min+.1, w_max-.1, num=num_points)
    flux_resample = spectres.spectres(wavelength_output, np.exp(wavelength_ln), convolved_flux)
    flux_output = 10**(flux_resample)
    spectrum = pd.DataFrame({'wavelength': wavelength_output[5:-5], 'flux': flux_output[5:-5]})
    return (spectrum)
