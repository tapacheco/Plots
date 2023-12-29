from functions import readModel
from plot_structure import fig_structure 
from plot_density import fig_density 
from plot_InglisTeler import fig_inglisTeller
from plot_coverage import fig_coverage
from plot_UV import fig_UV
from plot_visible import fig_visible
from plot_spectrum_25000 import fig_compare25
from plot_spectrum_45000 import fig_compare45
from plot_spectrum_optic import fig_compare
from plot_spectrum_ultraviolet import fig_compareUV
from plot_colorcolor import fig_corcor
from plot_sdss import fig_sdss
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
fig_structure(a_lte_t10000K, a_nlte_t10000K, a_lte_t15000K, a_nlte_t15000K, 
              a_lte_t25000K, a_nlte_t25000K, a_lte_t35000K, a_nlte_t35000K, 
              a_lte_t45000K, a_nlte_t45000K, a_lte_t65000K, a_nlte_t65000K,
              'solhighHe')

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
fig_structure(b_lte_t10000K, b_nlte_t10000K, b_lte_t15000K, b_nlte_t15000K, 
              b_lte_t25000K, b_nlte_t25000K, b_lte_t35000K, b_nlte_t35000K, 
              b_lte_t45000K, b_nlte_t45000K, b_lte_t65000K, b_nlte_t65000K,
              'lowZhighHe')

b_nlte_t10000K_g45=readModel(path_structure+"t10g45_lowZhighHe_nlte.7")
b_nlte_t10000K_g55=readModel(path_structure+"t10g55_lowZhighHe_nlte.7")
b_nlte_t65000K_g45=readModel(path_structure+"t65g45_lowZhighHe_nlte.7")
b_nlte_t65000K_g55=readModel(path_structure+"t65g55_lowZhighHe_nlte.7")
fig_density(b_nlte_t10000K_g45, b_nlte_t10000K_g55, b_nlte_t10000K, \
            b_nlte_t65000K_g45, b_nlte_t65000K_g55, b_nlte_t65000K)

path_spectra = '/Users/tpacheco/Documents/doutorado/plots/spectra/'
data_IT = pd.read_csv(path_spectra+"dados_InglisTeller_lowZHerich.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,
                      names=['Teff','gravity','eletronic_density','Nmax'])
fig_inglisTeller(data_IT)

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
fig_coverage(data10B,data10R, data15B,data15R, data20B,data20R, data25B,data25R,
             data30B,data30R, data35B,data35R, data45B,data45R, data65B,data65R )

data10B = pd.read_csv(path_spectra+"syB_t10g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data10R = pd.read_csv(path_spectra+"syR_t10g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data15B = pd.read_csv(path_spectra+"syB_t15g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data15R = pd.read_csv(path_spectra+"syR_t15g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data20B = pd.read_csv(path_spectra+"syB_t20g55lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data20R = pd.read_csv(path_spectra+"syR_t20g55lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data25B = pd.read_csv(path_spectra+"syB_t25g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data25R = pd.read_csv(path_spectra+"syR_t25g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data30B = pd.read_csv(path_spectra+"syB_t30g55lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data30R = pd.read_csv(path_spectra+"syR_t30g55lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data35B = pd.read_csv(path_spectra+"syB_t35g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data35R = pd.read_csv(path_spectra+"syR_t35g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data45B = pd.read_csv(path_spectra+"syB_t45g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data45R = pd.read_csv(path_spectra+"syR_t45g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data65B = pd.read_csv(path_spectra+"syB_t65g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
data65R = pd.read_csv(path_spectra+"syR_t65g55_lowZHerich_fwhm5.spec",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
fig_UV(data10B, data15B, data20B, data25B, data30B, data35B, data45B, data65B)
fig_visible(data10B,data10R, data15B,data15R, data20B,data20R, data25B,data25R,
           data30B,data30R, data35B,data35R, data45B,data45R, data65B,data65R )

specStar1 = pd.read_csv("/Users/tpacheco/Documents/doutorado/plots/442708048-flux.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,
                      names=['wavelength','flux'])
specMod1 = pd.read_csv("/Users/tpacheco/Documents/doutorado/plots/442708048-modelo-R0.19.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,
                      names=['wavelength','flux'])
fig_compare25(specMod1,specStar1)
specStar2 = pd.read_csv("/Users/tpacheco/Documents/doutorado/plots/183405148-flux.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
specMod2 = pd.read_csv("/Users/tpacheco/Documents/doutorado/plots/183405148-modelo-R0.13.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,names=['wavelength','flux'])
fig_compare45(specMod2,specStar2)
fig_compare(specMod1,specStar1,specMod2,specStar2)

specMod3 = pd.read_csv("/Users/tpacheco/Documents/doutorado/sd26_52.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,
                      names=['wavelength','flux'])
specStar3 = pd.read_csv("/Users/tpacheco/Documents/doutorado/hd4539_noext20.dat",
                      skip_blank_lines=True,header=None,delim_whitespace=True,
                      names=['wavelength','flux'])
fig_compareUV(specMod3,specStar3)

hst = pd.read_csv("/Users/tpacheco/Documents/doutorado/hstwfc3-ab-novo.dat",
                  skip_blank_lines=True,header=1,delim_whitespace=True, 
                  names=['Z','He','Teff','logg', 'F469N_F673N','F343N_FQ378N','FQ575N_FQ750N'])
stg = pd.read_csv("/Users/tpacheco/Documents/doutorado/stromgren-vega-novo.dat",
                  skip_blank_lines=True,header=2,delim_whitespace=True, 
                  names=['Z','He','Teff','logg','u_v','v_b','b_y','m1','c1'])
fig_corcor(hst,stg)

geier = pd.read_fwf("/Users/tpacheco/Documents/doutorado/J_A+A_635_A193/sdcatdr2.dat",
                    skip_blank_lines=True,header=None,delim_whitespace=True, 
    names=['Name','Gaia','DR2','GaiaDR2','RAdeg','DEdeg','GLON','GLAT','SpClass','SpSimbad','cClSDSS',
           'cClAPASS','cClPS1','cClSKYM','Plx','e_Plx','GMAG','Gmag','e_Gmag','BPmag','e_BPmag','RPmag',
           'e_RPmag','pmRA','e_pmRA','pmDE','e_pmDE','RVSDSS','e_RVSDSS','RVLAMOST','e_RVLAMOST',
           'Teff','e_Teff','logg','e_logg','logY','e_logY','Refs','E(B-V)','e_E(B-V)','AV','FUVmag','e_FUVmag',
           'NUVmag','e_NUVmag','VmagAPASS','e_VmagAPASS','BmagAPASS','e_BmagAPASS','gmagAPASS','e_gmagAPASS',
           'rmagAPASS','e_rmagAPASS','imagAPASS','e_imagAPASS','umagSDSS','e_umagSDSS','gmagSDSS','e_gmagSDSS',
           'rmagSDSS','e_rmagSDSS','imagSDSS','e_imagSDSS','zmagSDSS','e_zmagSDSS','umagVST','e_umagVST',
           'gmagVST','e_gmagVST','rmagVST','e_rmagVST','imagVST','e_imagVST','zmagVST','e_zmagVST',
           'umagSKYM','e_umagSKYM','vmagSKYM','e_vmagSKYM','gmagSKYM','e_gmagSKYM','rmagSKYM','e_rmagSKYM',
           'imagSKYM','e_imagSKYM','zmagSKYM','e_zmagSKYM','gmagPS1','e_gmagPS1','rmagPS1','e_rmagPS1',
           'imagPS1','e_imagPS1','zmagPS1','e_zmagPS1','ymagPS1','e_ymagPS1','Jmag2MASS','e_Jmag2MASS',
           'Hmag2MASS','e_Hmag2MASS','Kmag2MASS','e_Kmag2MASS','YmagUKIDSS','e_YmagUKIDSS','JmagUKIDSS',
           'e_JmagUKIDSS','HmagUKIDSS','e_HmagUKIDSS','KmagUKIDSS','e_KmagUKIDSS','ZmagVISTA','e_ZmagVISTA',
           'YmagVISTA','e_YmagVISTA','JmagVISTA','e_JmagVISTA','HmagVISTA','e_HmagVISTA','KsmagVISTA',
           'e_KsmagVISTA','W1mag','e_W1mag','W2mag','e_W2mag','W3mag','e_W3mag','W4mag','e_W4mag'])

teorico21 = pd.read_csv("/Users/tpacheco/Documents/doutorado/code_SSP/Plots/pacheco21/sdss-ab-novo.dat",
                        skip_blank_lines=True,header=1,delim_whitespace=True, 
                        names=['Z','He','Teff','logg','tu_g','tg_r','tr_i','ti_z'])
teorico23 = pd.read_csv("/Users/tpacheco/Documents/doutorado/code_SSP/Plots/pacheco21/sdss2.dat",
                        skip_blank_lines=True,header=1,delim_whitespace=True, 
                        names=['Z','He','Teff','logg','tu_g','tg_r','tr_i','ti_z'])
fig_sdss(geier, teorico21, teorico23)