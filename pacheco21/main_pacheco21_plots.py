from functions import readModel
from plot_structure import fig_structure 
from plot_density import fig_density 
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

