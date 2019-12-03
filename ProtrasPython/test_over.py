from imblearn.over_sampling import ADASYN
import pandas as pd
from collections import Counter
from sklearn.datasets import make_classification
import numpy as np

X, y = make_classification(n_classes=2, class_sep=2, weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0, n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=10)

fullPath = 'Datasets/imb_IRlowerThan9/ecoli2.dat'

T = pd.read_table(fullPath, skiprows=12, sep="\s+", header=None, delimiter=",",
                      usecols=[0,1,2,3,4,5,6], dtype=float)
temp = pd.read_table(fullPath,skiprows=12,sep="\s+", header=None, delimiter=",",usecols=[7], dtype=str)
temp = np.asarray(temp)
# temp = temp.reshape(1,temp.shape[0])


ada = ADASYN(random_state=0, sampling_strategy=str)
T_res, temp_res = ada.fit_resample(T,temp)
