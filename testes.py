from math import *
import pandas as pd
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

castelli ='/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/specsCASTELLI/fm15at15000g45k2odfnew.dat'
file_castelli = pd.read_csv(castelli, skip_blank_lines=True, comment='#', delimiter=' ', 
                            engine='python', names=['line', 'wavelength', 'flux'])
wavelength_cas = file_castelli['wavelength']
flux_cas = file_castelli['flux']*4*(3*10**(18))/(wavelength_cas**2)

coelho = '/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/specsCoelho/t15000_g+4.5_m10p00_hr.fits'
hdr = fits.getheader(coelho)
flux_coe = fits.getdata(coelho)
nfhr = len(flux_coe)
wavelength = np.empty(nfhr)
wavelength_coe = hdr['CRVAL1'] + (hdr['CDELT1']*np.arange(0,nfhr)) #HR

pacheco_R250 = '/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/specsEHB_lowZ/Herich_R250/t15000_g45_lowZ_Herich.fits'
with fits.open(pacheco_R250) as hdul:
    data = hdul[1].data
    wavelength_pac_low = data['WAVELENGTH']
    flux_pac_low = data['FLUX']

pacheco = '/Users/tpacheco/Documents/doutorado/code_SSP/SSPmodels/specsEHB_lowZ/Herich_R20000/t15000_g45_lowZ_Herich.fits'
with fits.open(pacheco) as hdul:
    data = hdul[1].data
    wavelength_pac = data['WAVELENGTH']
    flux_pac = data['FLUX']

fig, axt = plt.subplots(sharex=True, figsize=(14,7), tight_layout=True)
plt.minorticks_on()
plt.plot(wavelength_cas, flux_cas, c='#073763', linestyle='-',label='castelli', linewidth=3)
plt.plot(wavelength_coe, flux_coe, c='#e26e12', linestyle='-',label='coelho', linewidth=3)
plt.plot(wavelength_pac, flux_pac, c='#38761d', linestyle='-',label='pacheco', linewidth=3)
plt.plot(wavelength_pac_low, flux_pac_low, c='grey', linestyle='-', label='pacheco2', linewidth=3)
axt.set_xlim(0,10000.)
axt.legend()
plt.show()
