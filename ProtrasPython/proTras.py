from normalize import normalize
from get_init_point import get_init_point
import numpy as np
from distance2 import distance2

def proTras(NT):
    n,p = NT.shape
    print('Size data : ')
    print(NT.shape)
    eps = 0.1
    T = normalize(NT)
    s = 1
    x_init = get_init_point(T)
    T = np.asarray(T)
    print(x_init)

    for idx, x in enumerate(T):
        if np.allclose(x, x_init):
            x_init_ind = idx

    Cost = 1
    TI = np.linspace(1,n,num=n, dtype=int).reshape(n,1)
    Ty = np.zeros((n,1), dtype=int)
    S = x_init_ind
    iS = [1]
    wr = [0]
    pre_max_dist = [0]
    weight = [0]
    idMax = [0]
    index_remove_group = [1]
    index_remove_elements = np.full((n,1), False)
    print(index_remove_elements)

    while Cost>eps:
        index_remove_elements[S] = True
        diffPoints_Opt = TI[~index_remove_elements]
        Ty[S[-1]] = s

        "Tim khoang cach nho nhat tu 1 diem den 1 cum"
        d = distance2(T[diffPoints_Opt,:], T[S[iS],:])


    return 0