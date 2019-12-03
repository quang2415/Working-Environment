import pandas as pd

from io import StringIO

def read_dataset(dsName):
    datasetPath = 'Datasets/imb_IRlowerThan9/'
    fullPath = datasetPath+dsName
    print('fullpath dataset : ')
    print(fullPath)
    T = pd.read_table(fullPath, skiprows=12, sep="\s+", header=None, delimiter=",",
                      usecols=[0,1,2,3,4,5,6], dtype=float)
    temp = pd.read_table(fullPath,skiprows=12,sep="\s+", header=None, delimiter=",",usecols=[7], dtype=str)
    # print(X)
    # print(y)
    # print(T.loc[:,0])
    print(temp)
    return T
