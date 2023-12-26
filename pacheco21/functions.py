import numpy as np
import pandas as pd

def readModel(filename):
    model=pd.DataFrame()
    deepPoints=[]
    NDEPTH=0;NUMPAR=0;
    with open(filename) as f:
        line = f.readline()
        [NDEPTH,NUMPAR]=[int(s) for s in line.split()]
        while len(deepPoints) < NDEPTH:
            line = f.readline().split()
            deepPoints.extend([float(s.replace('D', 'E')) for s in line])
        modelAllLines=f.readlines()
        outList=[]
        lines=[x.strip() for x in modelAllLines]
        for line in lines:
            outList.extend([float(s.replace('D', 'E')) for s in line.split()])
        out=np.asarray(outList)
        model=np.transpose(out.flatten().reshape((-1,NUMPAR)))

    data =pd.DataFrame({#'NDEPTH':   NDEPTH,
           #'NUMPAR':    NUMPAR,
           'deepPoints':deepPoints,
           'atmpars':model[0].flatten()
           })
    return data