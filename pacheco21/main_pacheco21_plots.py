from functions import readModel
import pandas as pd

path_structure = '/Users/tpacheco/Documents/doutorado/plots/structure/'

lte_t10000K = readModel(path_structure+"t10g45_solhighHe_lte.7")
nlte_t10000K= readModel(path_structure+"t10g45_solhighHe_nlte.7")
lte_t15000K = readModel(path_structure+"t10g45_solhighHe_nlte.7")
nlte_t15000K= readModel(path_structure+"t15g45_solhighHe_nlte.7")
lte_t25000K = readModel(path_structure+"t25g45_solhighHe_lte.7")
nlte_t25000K= readModel(path_structure+"t25g45_solhighHe_nlte.7")
lte_t35000K = readModel(path_structure+"t35g45_solhighHe_lte.7")
nlte_t35000K= readModel(path_structure+"t35g45_solhighHe_nlte.7")
lte_t45000K = readModel(path_structure+"t45g45_solhighHe_lte.7")
nlte_t45000K= readModel(path_structure+"t45g45_solhighHe_nlte.7")
lte_t65000K = readModel(path_structure+"t65g45_solhighHe_lte.7")
nlte_t65000K= readModel(path_structure+"t65g45_solhighHe_nlte.7")


lt10_NDEPTHb,lt10_NUMPARb,lt10_deepPointsb,lt10_atmparsb=readModel(path_structure+"t10g65_lowZhighHe_lte.7")
nl10_NDEPTHb,nl10_NUMPARb,nl10_deepPointsb,nl10_atmparsb=readModel(path_structure+"t10g65_lowZhighHe_nlte.7")
lt15_NDEPTHb,lt15_NUMPARb,lt15_deepPointsb,lt15_atmparsb=readModel(path_structure+"t15g65_lowZhighHe_lte.7")
nl15_NDEPTHb,nl15_NUMPARb,nl15_deepPointsb,nl15_atmparsb=readModel(path_structure+"t15g65_lowZhighHe_nlte.7")
lt25_NDEPTHb,lt25_NUMPARb,lt25_deepPointsb,lt25_atmparsb=readModel(path_structure+"t25g65_lowZhighHe_lte.7")
nl25_NDEPTHb,nl25_NUMPARb,nl25_deepPointsb,nl25_atmparsb=readModel(path_structure+"t25g65_lowZhighHe_nlte.7")
lt35_NDEPTHb,lt35_NUMPARb,lt35_deepPointsb,lt35_atmparsb=readModel(path_structure+"t35g65_lowZhighHe_lte.7")
nl35_NDEPTHb,nl35_NUMPARb,nl35_deepPointsb,nl35_atmparsb=readModel(path_structure+"t35g65_lowZhighHe_nlte.7")
lt45_NDEPTHb,lt45_NUMPARb,lt45_deepPointsb,lt45_atmparsb=readModel(path_structure+"t45g65_lowZhighHe_lte.7")
nl45_NDEPTHb,nl45_NUMPARb,nl45_deepPointsb,nl45_atmparsb=readModel(path_structure+"t45g65_lowZhighHe_nlte.7")
lt65_NDEPTHb,lt65_NUMPARb,lt65_deepPointsb,lt65_atmparsb=readModel(path_structure+"t65g65_lowZhighHe_lte.7")
nl65_NDEPTHb,nl65_NUMPARb,nl65_deepPointsb,nl65_atmparsb=readModel(path_structure+"t65g65_lowZhighHe_nlte.7")

