import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


filter = ["j378", "j395", "j410", "j430", "g","j515","r","j660","i","j861","z"]
error_filter = ["ej378", "ej395", "ej410", "ej430", "eg","ej515","er","ej660","ei","ej861","ez"]
wavelength = [.378237,.393937,.410812,.430329,.478987,.514089,.625663,.660391,.765620,.861049,.896470]
filter_jplus = ["J0378", "J0395", "J0410", "J0430", "gSDSS","J0515","rSDSS","J0660","iSDSS","J0861","zSDSS"]
error_jplus = ["ej378", "ej395", "ej410", "ej430", "eg","ej515","er","ej660","ei","ej861","ez"]
wavelength_jplus = [.378237,.393937,.410812,.430329,.478987,.514089,.625663,.660391,.765620,.861049,.896470]
colors = plt.cm.rainbow(np.linspace(0, 1, len(wavelength)))


def plot_SED_residual(mags_obj, error_obj, title):
    median_mags = mags_obj.median()
    median_deviation = stats.median_abs_deviation(mags_obj)
    plt.figure(figsize=(8, 5))
    plt.axhline(y=0, color='black', linestyle='-', label='')
    for i in range(len(mags_obj)):
        plt.errorbar(wavelength,mags_obj.iloc[i, :]-median_mags,yerr=error_obj.iloc[i, :], fmt='o', label='', color='grey', elinewidth=1, capsize=3)
    for i in range(len(median_mags)):
        plt.errorbar(wavelength[i], median_mags[i]-median_mags[i], yerr=median_deviation[i], color=colors[i], fmt='*', ecolor=colors[i], markersize=8, label='', elinewidth=2, capsize=4, zorder=10)
    plt.scatter([], [], color='purple', marker='*', label='Median+Absolute Deviation')  
    plt.xlabel(r'Wavelength ($\mu$m)')
    plt.gca().invert_yaxis()
    plt.ylabel('Magnitude')
    plt.title(title)
    plt.grid(False)
    plt.legend()
    plt.savefig('SED'+title+'_median_residuals.png')
    return (median_mags, median_deviation)


path_stars = '/home/thayse/Documents/analysis_NGC2403/NGC2403_GCcandidates_visualInspection_matching_stars_NicsTable.csv'
stars = pd.read_csv(path_stars)
mags_stars =stars[filter]
error_stars = stars[error_filter]
(median_mags_stars, median_deviation_stars)=plot_SED_residual(mags_stars,error_stars,'Stars')

path_galaxies = '/home/thayse/Documents/analysis_NGC2403/NGC2403_GCcandidates_visualInspection_matching_galaxies_NicsTable.csv'
galaxies = pd.read_csv(path_galaxies)
mags_gal = galaxies[filter]
error_gal = galaxies[error_filter]
(median_mags_gal, median_deviation_gal)=plot_SED_residual(mags_gal, error_gal, 'Galaxies')

path_GCs = '/home/thayse/Documents/analysis_NGC2403/NGC2403_GCcandidates_visualInspection_matching_GCs_NicsTable.csv'
GCs = pd.read_csv(path_GCs)
mags_gcs = GCs[filter]
error_gcs = GCs[error_filter]
(median_mags_gcs, median_deviation_gcs)=plot_SED_residual(mags_gcs, error_gcs, 'GCs')

path_other = '/home/thayse/Documents/analysis_NGC2403/NGC2403_GCcandidates_visualInspection_matching_other_NicsTable.csv'
other = pd.read_csv(path_other)
mags_other = other[filter]
error_other = other[error_filter]
(median_mags_other, median_deviation_other)=plot_SED_residual(mags_other, error_other, 'Other')

confirmed_ngc2403 = pd.read_csv('/home/thayse/Documents/analysis_NGC2403/NGC2403_GCs_confirmed.csv', sep=',')
mags_conf = confirmed_ngc2403[filter]
error_conf = confirmed_ngc2403[error_filter]
(median_mags_conf, median_deviation_conf)=plot_SED_residual(mags_conf, error_conf, 'Confirmed')



def plot_SED_models_residual(mags_obj, title):
    median_mags = mags_obj.median()
    median_deviation = stats.median_abs_deviation(mags_obj)
    plt.figure(figsize=(8, 5))
    plt.axhline(y=0, color='black', linestyle='-', label='')
    for i in range(len(mags_obj)):
        plt.scatter(wavelength_jplus,mags_obj.iloc[i, :]-median_mags, marker='o', label='', color='grey')
    for i in range(len(median_mags)):
        plt.errorbar(wavelength_jplus[i], median_mags[i]-median_mags[i], yerr=median_deviation[i], color=colors[i], fmt='*', ecolor=colors[i], markersize=8, label='', elinewidth=2, capsize=4, zorder=10)
    plt.scatter([], [], color='purple', marker='*', label='Median+Absolute Deviation')  
    plt.xlabel(r'Wavelength ($\mu$m)')
    plt.gca().invert_yaxis()
    plt.ylabel('Magnitude')
    plt.title(title)
    plt.grid(False)
    plt.legend()
    plt.savefig('SED'+title+'_median_residuals.png')
    return (median_mags, median_deviation)

kstars_models = pd.read_csv('/home/thayse/Documents/syntheticMagnitudes/magnitudesStellarModels/synmags_wide_jplus_solar_radius.csv')
mags_kstars = kstars_models[filter_jplus]
(median_mags_kstars, median_deviation_kstars) = plot_SED_models_residual(mags_kstars, 'K Stars models')

xsl_models = pd.read_csv('/home/thayse/Documents/syntheticMagnitudes/magnitudesSSP_XSL/magnitudes_XSL_SSP_JPLUS.csv')
mags_xsl = xsl_models[filter_jplus]
(median_mags_xsl, median_deviation_xsl) = plot_SED_models_residual(mags_xsl, 'XSL models')
