
from math import *
import pandas as pd
import numpy as np
from astropy.io import fits
import extinction 
from extinction import remove

import plot_CMDs as cmd
import plot_color_color as ccd
import plot_density_color_color as den
import plot_spectra as spc
import functions as apply
import degrade_resolvingPower as rsp
import plot_compareSSP as cpr
import plot_SSP_observed as obs

import sys
sys.path.append('../SSPmodels/codeModule/utilsSpecMod/')
from photoColors import get_reddening
from photoColors import compute_color_extinction 
from photoColors import calculate_colors

path = '../SSPmodels/'
nameGC = 'NGC7089'
color_excess_B_V = 0.06
file = 'subsets_hugs_ngc7089_meth1.txt'
#nameGC = 'NGC2808'
#color_excess_B_V = 0.22
#file = 'subsets_hugs_ngc2808_meth1.txt'

synthetic_file_coelho = 'syntheticMAGS_Coelho.txt'
synthetic_file_pacheco = 'syntheticMAGS_EHB_Herich.txt'
synthetic_file_castelli = 'syntheticMAGS_Castelli.txt'

print("Globular Cluster: %s" %nameGC)

photometry_gc = pd.read_csv(path+file, engine='python', comment='#',
                            skip_blank_lines=True, delim_whitespace=True, 
                            names=['X', 'Y', 
                            'F275W', 'RMSF275W', 'QFITF275W', 'RADXSF275W', 'NfF275W', 'NgF275W', #col 3
                            'F336W', 'RMSF336W', 'QFITF336W', 'RADXSF336W', 'NfF336W', 'NgF336W', #col 9
                            'F438W', 'RMSF438W', 'QFITF438W', 'RADXSF438W', 'NfF438W', 'NgF438W', #col 15
                            'F606W', 'RMSF606W', 'QFITF606W', 'RADXSF606W', 'NfF606W', 'NgF606W', #col 21
                            'F814W', 'RMSF814W', 'QFITF814W', 'RADXSF814W', 'NfF814W', 'NgF814W', #col 27
                            'P', 'RA', 'DEC', 'ID', 'ITER', 'MS','GB','RHB','BS','BHB','EHB']) #col 33
synthetic_data_coelho = pd.read_csv(path+synthetic_file_coelho, engine='python', comment='#',
                            skip_blank_lines=True, sep=',',
                            names=['mod', 'TEFF', 'LOGG', 'FEH', 
                                   'F275W', 'F336W', 'F438W', 'F606W', 'F814W', 
                                   'Int_F275W', 'Int_F336W', 'Int_F438W', 'Int_F606W', 'Int_F814W'])
synthetic_data_pacheco = pd.read_csv(path+synthetic_file_pacheco, engine='python', comment='#',
                            skip_blank_lines=True, sep=',',
                            names=['mod', 'TEFF', 'LOGG', 'FEH', 
                                   'F275W', 'F336W', 'F438W', 'F606W', 'F814W', 
                                   'Int_F275W', 'Int_F336W', 'Int_F438W', 'Int_F606W', 'Int_F814W'])
param_ms = pd.read_csv(path+nameGC+'_ms_param.dat', engine='python', comment='#', skip_blank_lines=True, 
                       sep='\t', names=['F275W', 'F336W', 'F438W', 'F606W', 'F814W',
                                       'F275W_F336W', 'F275W_F438W', 'F275W_F606W', 'F275W_F814W', 
                                       'F336W_F438W', 'F336W_F606W', 'F336W_F814W', 'F438W_F606W', 
                                       'F438W_F814W', 'F606W_F814W', 'distance', 'index', 
                                       'TEFF', 'LOG_G'])
distance_ms = param_ms['distance'][1:].astype(float)
param_gb = pd.read_csv(path+nameGC+'_gb_param.dat', engine='python', comment='#', skip_blank_lines=True, 
                       sep='\t', names=['F275W', 'F336W', 'F438W', 'F606W', 'F814W',
                                       'F275W_F336W', 'F275W_F438W', 'F275W_F606W', 'F275W_F814W', 
                                       'F336W_F438W', 'F336W_F606W', 'F336W_F814W', 'F438W_F606W', 
                                       'F438W_F814W', 'F606W_F814W', 'distance', 'index', 
                                       'TEFF', 'LOG_G'])
distance_gb = param_gb['distance'][1:].astype(float)
param_rhb = pd.read_csv(path+nameGC+'_rhb_param.dat', engine='python', comment='#', skip_blank_lines=True, 
                       sep='\t', names=['F275W', 'F336W', 'F438W', 'F606W', 'F814W',
                                       'F275W_F336W', 'F275W_F438W', 'F275W_F606W', 'F275W_F814W', 
                                       'F336W_F438W', 'F336W_F606W', 'F336W_F814W', 'F438W_F606W', 
                                       'F438W_F814W', 'F606W_F814W', 'distance', 'index', 
                                       'TEFF', 'LOG_G'])
distance_rhb = param_rhb['distance'][1:].astype(float)
param_bs = pd.read_csv(path+nameGC+'_bs_param.dat', engine='python', comment='#', skip_blank_lines=True, 
                       sep='\t', names=['F275W', 'F336W', 'F438W', 'F606W', 'F814W',
                                       'F275W_F336W', 'F275W_F438W', 'F275W_F606W', 'F275W_F814W', 
                                       'F336W_F438W', 'F336W_F606W', 'F336W_F814W', 'F438W_F606W', 
                                       'F438W_F814W', 'F606W_F814W', 'distance', 'index', 
                                       'TEFF', 'LOG_G'])
distance_bs = param_bs['distance'][1:].astype(float)
param_bhb = pd.read_csv(path+nameGC+'_bhb_param.dat', engine='python', comment='#', skip_blank_lines=True, 
                       sep='\t', names=['F275W', 'F336W', 'F438W', 'F606W', 'F814W',
                                       'F275W_F336W', 'F275W_F438W', 'F275W_F606W', 'F275W_F814W', 
                                       'F336W_F438W', 'F336W_F606W', 'F336W_F814W', 'F438W_F606W', 
                                       'F438W_F814W', 'F606W_F814W', 'distance', 'index', 
                                       'TEFF', 'LOG_G'])
distance_bhb = param_bhb['distance'][1:].astype(float)
param_ehb = pd.read_csv(path+nameGC+'_ehb_param.dat', engine='python', comment='#', skip_blank_lines=True, 
                       sep='\t', header=1, names=['F275W', 'F336W', 'F438W', 'F606W', 'F814W',
                                       'F275W_F336W', 'F275W_F438W', 'F275W_F606W', 'F275W_F814W', 
                                       'F336W_F438W', 'F336W_F606W', 'F336W_F814W', 'F438W_F606W', 
                                       'F438W_F814W', 'F606W_F814W', 'distance', 'index', 
                                       'TEFF', 'LOG_G'])
distance_ehb = param_ehb['distance'][1:].astype(float)

distance_ms  = pd.DataFrame({'ms': distance_ms})
distance_gb  = pd.DataFrame({'gb': distance_gb}) 
distance_rhb = pd.DataFrame({'rhb':distance_rhb})
distance_bs  = pd.DataFrame({'bs': distance_bs}) 
distance_bhb = pd.DataFrame({'bhb':distance_bhb})
distance_ehb = pd.DataFrame({'ehb':distance_ehb})

print("Computing color excess")
print("E(B-V): %s" %color_excess_B_V)
reddening = get_reddening(color_excess_B_V)
extinction = compute_color_extinction(color_excess_B_V)

print("\n Calculating photometric colors from HST")
color = calculate_colors(photometry_gc)
coelho_color =  calculate_colors(synthetic_data_coelho)
coelho_mag = apply.catch_magnitudes(synthetic_data_coelho)
pacheco_color = calculate_colors(synthetic_data_pacheco)
pacheco_mag = apply.catch_magnitudes(synthetic_data_pacheco)

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

"""
print("Plotting CMD")
cmd.plot_color_magnitude_diagram(ms_color, ms_mag, \
                                gb_color, gb_mag, \
                                rhb_color,rhb_mag,\
                                bs_color, bs_mag, \
                                bhb_color,bhb_mag,\
                                 ehb_color,ehb_mag,\
                                 './', nameGC)

print("Plotting color-color diagram")
ccd.plot_color_color_diagram(ms_color, distance_ms, \
                             gb_color, distance_gb, \
                             rhb_color,distance_rhb,\
                             bs_color, distance_bs, \
                             bhb_color,distance_bhb,\
                             ehb_color,distance_ehb,\
                             coelho_color,  \
                             pacheco_color, \
                             './', nameGC)
"""
print("Plotting other color-color diagram")
den.plot_density_diagram(ms_color, distance_ms, \
                         gb_color, distance_gb, \
                         rhb_color,distance_rhb,\
                         bs_color, distance_bs, \
                         bhb_color,distance_bhb,\
                         ehb_color,distance_ehb,\
                         coelho_color,  \
                         pacheco_color, \
                         './', nameGC)

"""
#ms_spectrum =  rsp.degrade_resolving_power(path+nameGC+'_ms_spectrum.dat', 1000)
#gb_spectrum =  rsp.degrade_resolving_power(path+nameGC+'_gb_spectrum.dat', 1000)
#rhb_spectrum = rsp.degrade_resolving_power(path+nameGC+'_rhb_spectrum.dat',1000)
#bs_spectrum =  rsp.degrade_resolving_power(path+nameGC+'_bs_spectrum.dat', 1000)
#bhb_spectrum = rsp.degrade_resolving_power(path+nameGC+'_bhb_spectrum.dat',1000)
#ehb_spectrum = rsp.degrade_resolving_power(path+nameGC+'_ehb_spectrum.dat',1000)

ms_spectrum = pd.read_csv(path+nameGC+'_ms_spectrum.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
gb_spectrum = pd.read_csv(path+nameGC+'_gb_spectrum.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
rhb_spectrum = pd.read_csv(path+nameGC+'_rhb_spectrum.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
bs_spectrum = pd.read_csv(path+nameGC+'_bs_spectrum.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
bhb_spectrum = pd.read_csv(path+nameGC+'_bhb_spectrum.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
ehb_spectrum = pd.read_csv(path+nameGC+'_ehb_spectrum.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])

spc.plot_evolutionary_SSP(ms_spectrum['wavelength'], 
                          gb_spectrum['flux'], 
                          ms_spectrum['flux'], 
                          rhb_spectrum['flux'], 
                          bs_spectrum['flux'], 
                          bhb_spectrum['flux'], 
                          ehb_spectrum['flux'], './'+nameGC)

#base_ssp =rsp.degrade_resolving_power(path+nameGC+'_base_ssp.dat', 1000)
#bs_ssp   = rsp.degrade_resolving_power(path+nameGC+'_bs_ssp.dat',  1000)
#bhb_ssp  = rsp.degrade_resolving_power(path+nameGC+'_bhb_ssp.dat', 1000)
#ehb_ssp  = rsp.degrade_resolving_power(path+nameGC+'_ehb_ssp.dat', 1000)
#total_ssp=rsp.degrade_resolving_power(path+nameGC+'_total_ssp.dat',1000)
#
#cpr.plot_ssp_compare(base_ssp['wavelength'], base_ssp['flux'], bs_ssp['flux'], 
#                     bhb_ssp['flux'], ehb_ssp['flux'], total_ssp['flux'], './'+nameGC)

base_ssp = pd.read_csv(path+nameGC+'_base_ssp.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
bs_ssp = pd.read_csv(path+nameGC+'_bs_ssp.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
bhb_ssp = pd.read_csv(path+nameGC+'_bhb_ssp.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
ehb_ssp = pd.read_csv(path+nameGC+'_ehb_ssp.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
total_ssp = pd.read_csv(path+nameGC+'_total_ssp.dat', engine='python', comment='#',
                          skip_blank_lines=True, delim_whitespace=True,  header=1,
                          names=['wavelength', 'flux'])
#cpr.plot_ssp_compare(base_ssp['wavelength'], base_ssp['flux'], bs_ssp['flux'], 
#                     bhb_ssp['flux'], ehb_ssp['flux'], total_ssp['flux'], './'+nameGC)

Av = 3.1*color_excess_B_V
print('Av = %f'%Av)
import extinction 
iue1_m2_A = pd.read_csv('/Users/tpacheco/Documents/doutorado/ARI_LJMU/ngc7089_IUE_lr12220',
                        skip_blank_lines=True,header=18,engine='python',delim_whitespace=True, 
                        names=['wavelength','flux','sigma','back','net','quali'])
iue1_f_m2 = np.array(iue1_m2_A['flux'])
iue1_w_m2 = np.array(iue1_m2_A['wavelength'])
iue1_flux_deredden = remove(extinction.fm07(iue1_w_m2, Av), iue1_f_m2)
iue2_m2_A = pd.read_csv('/Users/tpacheco/Documents/doutorado/ARI_LJMU/ngc7089_IUE_sp10171',
                        skip_blank_lines=True,header=18,engine='python',delim_whitespace=True, 
                        names=['wavelength','flux','sigma','back','net','quali'])
iue2_f_m2 = np.array(iue2_m2_A['flux'])
iue2_w_m2 = np.array(iue2_m2_A['wavelength'])
iue2_flux_deredden = remove(extinction.fm07(iue2_w_m2, Av), iue2_f_m2)
iue3_m2_A = pd.read_csv('/Users/tpacheco/Documents/doutorado/ARI_LJMU/ngc7089_IUE_sp15885',
                        skip_blank_lines=True,header=18,engine='python',delim_whitespace=True, 
                        names=['wavelength','flux','sigma','back','net','quali'])
iue3_f_m2 = np.array(iue3_m2_A['flux'])
iue3_w_m2 = np.array(iue3_m2_A['wavelength'])
iue3_flux_deredden = remove(extinction.fm07(iue3_w_m2, Av), iue3_f_m2)

file = '/Users/tpacheco/Documents/doutorado/ARI_LJMU/schiavon05/List/NGC7089_a_1.fits'
hdr = fits.getheader(file)
schi05_f_m2_A = fits.getdata(file) 
nfhr=len(schi05_f_m2_A)
crval, cdelt = (hdr['CRVAL1'], hdr['CD1_1']) 
schi05_w_m2 = crval + (cdelt*np.arange(0,nfhr)) #HR
schi05_flux_deredden = extinction.remove(extinction.fm07(schi05_w_m2, Av), schi05_f_m2_A)

index1 = 149 #np.argmin(np.abs(iue1_w_m2 - 2250))
index2 = 423 #np.argmin(np.abs(iue2_w_m2 - 1860))
index3 = 422 #np.argmin(np.abs(iue3_w_m2 - 1860))
index_S= 3 #np.argmin(np.abs(schi05_w_m2 - 4600))
index_ssp = np.argmin(np.abs(base_ssp['wavelength'] - 1860))

obs.plot_ssp(total_ssp['wavelength'], total_ssp['flux'], index_ssp,\
             schi05_w_m2, schi05_flux_deredden, index_S, \
             iue1_w_m2, iue1_flux_deredden, iue1_m2_A['sigma'], index1, \
             iue2_w_m2, iue2_flux_deredden, iue2_m2_A['sigma'], index2, \
             iue3_w_m2, iue3_flux_deredden, iue3_m2_A['sigma'], index3, \
             './'+nameGC)

#Av = 3.1*color_excess_B_V
#import extinction
#file = '/Users/tpacheco/Documents/doutorado/ARI_LJMU/schiavon05/List/NGC2808_a_1.fits'
#hdr = fits.getheader(file)
#schi05_f_2808_A = fits.getdata(file) 
#nfhr=len(schi05_f_2808_A)
#crval, cdelt = (hdr['CRVAL1'], hdr['CD1_1']) 
#schi05_w_2808 = crval + (cdelt*np.arange(0,nfhr)) #HR
#schi05_flux_deredden = extinction.remove(extinction.fm07(schi05_w_2808, Av), schi05_f_2808_A)
#index_S= np.argmin(np.abs(schi05_w_2808 - 4950))
#index_ssp = np.argmin(np.abs(base_ssp['wavelength'] - 4950))
#obs.plot_ssp(total_ssp['wavelength'], total_ssp['flux'], index_ssp,\
#             schi05_w_2808, schi05_flux_deredden, index_S, \
#             './'+nameGC)
#
"""