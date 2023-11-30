import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import gridspec
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import seaborn as sns


info_F275 = pd.Series([2710.00, 2725.12, 2720.87, 2286.17, 3120.27, 425.05, 923.66, 3.74e-9]) #WFC3/UVIS
info_F336 = pd.Series([3354.72, 3365.99, 3359.43, 3014.02, 3706.78, 512.30, 1227.35, 3.26e-9]) #WFC3/UVIS
info_F438 = pd.Series([4326.14, 4339.54, 4323.73, 3894.93, 4710.01, 589.48, 4198.05, 6.73e-9]) #WFC3/UVIS
info_F606 = pd.Series([5921.94, 6035.81, 5810.77, 4626.09, 7179.31, 1771.3, 3231.69, 2.87e-9]) #ACS/WFC
info_F814 = pd.Series([8044.99, 8128.69, 7972.92, 6867.80, 9626.12, 1886.7, 2418.20, 1.14e-9]) #ACS/WFC

filter_files = pd.Series(['./HST_WFC3_UVIS1.F275W.dat', 
                          './HST_WFC3_UVIS1.F336W.dat', 
                          './HST_WFC3_UVIS1.F438W.dat', 
                          './HST_ACS_WFC.F606W.dat', 
                          './HST_ACS_WFC.F814W.dat'])

NUFL = len(filter_files) 
read_filter = {}
for k in range(NUFL):
        filter =  pd.read_csv(filter_files[k], skip_blank_lines=True, 
                              comment='#', delim_whitespace=True, 
                              names=['wavelength', 'flux'],engine='python')
        read_filter[k] = [filter['wavelength'], filter['flux']]

