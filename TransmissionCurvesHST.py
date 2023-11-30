import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import gridspec
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)
import itertools
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

fig, axt = plt.subplots(sharex=True, figsize=(16,8), tight_layout=True)
plt.minorticks_on()

# 400# 450# 510# 600# 730
palette = itertools.cycle(["#882E72", "#882E72",
                           "#0077BB", "#0077BB", 
                           "#EE7733", "#EE7733",
                           "#009988", "#009988",
                           "#EE3377", "#EE3377"])

NUFL = len(filter_files) 
for k in range(NUFL):
    filter =  pd.read_csv(filter_files[k], skip_blank_lines=True, 
                          comment='#', delim_whitespace=True, 
                          names=['wavelength', 'flux'],engine='python')
 
    sns.lineplot(data=filter, x='wavelength', y='flux', linewidth=2.5,
                 color=next(palette))
    axt.fill_between(filter['wavelength'], filter['flux'], color=next(palette), alpha=0.25)

axt.text(2300, 0.14, 'F275W', color='#882E72', weight='bold', fontsize=30)
axt.text(3000, 0.215, 'F336W', color='#0077BB', weight='bold', fontsize=30)
axt.text(3950, 0.26, 'F438W', color='#EE7733', weight='bold', fontsize=30)
axt.text(5400, 0.445, 'F606W', color='#009988', weight='bold', fontsize=30)
axt.text(8200, 0.36, 'F814W', color='#EE3377', weight='bold', fontsize=30)

xmin, xmax, ymin, ymax = (2100, 9900, 0, 0.51)
axt.set_xlim(xmin, xmax)
axt.set_ylim(ymin, ymax)
plt.title("", fontsize=30)
plt.ylabel(r'Transmission curve', fontsize=30)
plt.xlabel(r'Wavelength [\AA]', fontsize=30)
plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
plt.tick_params(direction='in', which='major', length=8, width=1.5, top=True, right=True)
plt.tick_params(direction='in', which='minor', length=5, width=1.2, top=True, right=True)
plt.rcParams['ytick.right'] = True 

plt.show()
plt.savefig('Filters_HST.png', dpi=200, bbox_inches = 'tight')
