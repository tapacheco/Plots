from functions import readModel
from plot_structure import fig_structure 
from plot_density import fig_density 
from plot_InglisTeler import fig_inglisTeller
from coverage import fig_coverage
import pandas as pd

path_structure = '/Users/tpacheco/Documents/doutorado/plots/structure/'

a_lte_t10000K = readModel(path_structure+"t10g45_solhighHe_lte.7")
a_nlte_t10000K= readModel(path_structure+"t10g45_solhighHe_nlte.7")
a_lte_t15000K = readModel(path_structure+"t15g45_solhighHe_lte.7")
a_nlte_t15000K= readModel(path_structure+"t15g45_solhighHe_nlte.7")
a_lte_t25000K = readModel(path_structure+"t25g45_solhighHe_lte.7")
a_nlte_t25000K= readModel(path_structure+"t25g45_solhighHe_nlte.7")
a_lte_t35000K = readModel(path_structure+"t35g45_solhighHe_lte.7")
a_nlte_t35000K= readModel(path_structure+"t35g45_solhighHe_nlte.7")
a_lte_t45000K = readModel(path_structure+"t45g45_solhighHe_lte.7")
a_nlte_t45000K= readModel(path_structure+"t45g45_solhighHe_nlte.7")
a_lte_t65000K = readModel(path_structure+"t65g45_solhighHe_lte.7")
a_nlte_t65000K= readModel(path_structure+"t65g45_solhighHe_nlte.7")
#fig_structure(a_lte_t10000K, a_nlte_t10000K, a_lte_t15000K, a_nlte_t15000K, 
#              a_lte_t25000K, a_nlte_t25000K, a_lte_t35000K, a_nlte_t35000K, 
#              a_lte_t45000K, a_nlte_t45000K, a_lte_t65000K, a_nlte_t65000K,
#              'solhighHe')

b_lte_t10000K = readModel(path_structure+"t10g65_lowZhighHe_lte.7")
b_nlte_t10000K= readModel(path_structure+"t10g65_lowZhighHe_nlte.7")
b_lte_t15000K = readModel(path_structure+"t15g65_lowZhighHe_lte.7")
b_nlte_t15000K= readModel(path_structure+"t15g65_lowZhighHe_nlte.7")
b_lte_t25000K = readModel(path_structure+"t25g65_lowZhighHe_lte.7")
b_nlte_t25000K= readModel(path_structure+"t25g65_lowZhighHe_nlte.7")
b_lte_t35000K = readModel(path_structure+"t35g65_lowZhighHe_lte.7")
b_nlte_t35000K= readModel(path_structure+"t35g65_lowZhighHe_nlte.7")
b_lte_t45000K = readModel(path_structure+"t45g65_lowZhighHe_lte.7")
b_nlte_t45000K= readModel(path_structure+"t45g65_lowZhighHe_nlte.7")
b_lte_t65000K = readModel(path_structure+"t65g65_lowZhighHe_lte.7")
b_nlte_t65000K= readModel(path_structure+"t65g65_lowZhighHe_nlte.7")
#fig_structure(b_lte_t10000K, b_nlte_t10000K, b_lte_t15000K, b_nlte_t15000K, 
#              b_lte_t25000K, b_nlte_t25000K, b_lte_t35000K, b_nlte_t35000K, 
#              b_lte_t45000K, b_nlte_t45000K, b_lte_t65000K, b_nlte_t65000K,
#              'lowZhighHe')

b_nlte_t10000K_g45=readModel(path_structure+"t10g45_lowZhighHe_nlte.7")
b_nlte_t10000K_g55=readModel(path_structure+"t10g55_lowZhighHe_nlte.7")
b_nlte_t65000K_g45=readModel(path_structure+"t65g45_lowZhighHe_nlte.7")
b_nlte_t65000K_g55=readModel(path_structure+"t65g55_lowZhighHe_nlte.7")
#fig_density(b_nlte_t10000K_g45, b_nlte_t10000K_g55, b_nlte_t10000K, \
#            b_nlte_t65000K_g45, b_nlte_t65000K_g55, b_nlte_t65000K)

path_spectra = '/Users/tpacheco/Documents/doutorado/plots/spectra/'
data_IT = pd.read_csv(path_spectra+"dados_InglisTeller_lowZHerich.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,
                      names=['Teff','gravity','eletronic_density','Nmax'])
#fig_inglisTeller(data_IT)


data10B = pd.read_csv(path_spectra+"norm/syB_t10g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data10R = pd.read_csv(path_spectra+"norm/syR_t10g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data15B = pd.read_csv(path_spectra+"norm/syB_t15g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data15R = pd.read_csv(path_spectra+"norm/syR_t15g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data20B = pd.read_csv(path_spectra+"norm/syB_t20g55lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data20R = pd.read_csv(path_spectra+"norm/syR_t20g55lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data25B = pd.read_csv(path_spectra+"norm/syB_t25g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data25R = pd.read_csv(path_spectra+"norm/syR_t25g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data30B = pd.read_csv(path_spectra+"norm/syB_t30g55lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data30R = pd.read_csv(path_spectra+"norm/syR_t30g55lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data35B = pd.read_csv(path_spectra+"norm/syB_t35g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data35R = pd.read_csv(path_spectra+"norm/syR_t35g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data45B = pd.read_csv(path_spectra+"norm/syB_t45g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data45R = pd.read_csv(path_spectra+"norm/syR_t45g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data65B = pd.read_csv(path_spectra+"norm/syB_t65g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data65R = pd.read_csv(path_spectra+"norm/syR_t65g55_lowZHerich_norm.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])

#fig_coverage(data10B,data10R,
#                 data15B,data15R,
#                 data20B,data20R,
#                 data25B,data25R,
#                 data30B,data30R,
#                 data35B,data35R,
#                 data45B,data45R,
#                 data65B,data65R
#                 )