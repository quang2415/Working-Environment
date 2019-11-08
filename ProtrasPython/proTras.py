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
    S = []
    S.append(x_init_ind)

    # S = np.asarray([])
    # np.insert(S,len(S),x_init_ind)

    iS = np.asarray([1])
    wr = [0]
    pre_max_dist = [0]
    weight = [0]
    idMax = [0]
    index_remove_group = [1]
    index_remove_elements = np.full((n,1), False)

    while Cost>eps:
        index_remove_elements[S] = True
        diffPoints_Opt = TI[~index_remove_elements]
        # diffPoints_Opt = diffPoints_Opt.reshape(len(diffPoints_Opt),1)
        diffPoints_Opt = diffPoints_Opt.reshape(len(diffPoints_Opt),1)
        Ty[S[-1]] = s

        "Tim khoang cach nho nhat tu 1 diem den 1 cum"
        a = T[np.ix_((diffPoints_Opt-1).flatten())]
        temp = np.asarray(S)
        b = temp[np.ix_(np.asarray(iS)-1)]
        c = T[np.ix_(temp[np.ix_(np.asarray(iS)-1)])]

        d = distance2(T[(diffPoints_Opt-1).flatten()], (T[np.ix_(temp[np.ix_(np.asarray(iS)-1)])]).flatten())
        a = T[(diffPoints_Opt-1).flatten()]
        indMin = np.argmin(d, axis=1)
        indMin = indMin.reshape(len(indMin),1)
        # indMin = indMin.flatten()

        # Ty[np.ix_((diffPoints_Opt-1).flatten())] = iS[indMin]

        # t_temp = iS[indMin]
        # print(Ty[(diffPoints_Opt-1).flatten()])

        for x in range(diffPoints_Opt.size):
            # print(x-1,Ty[x-1],indMin[x-1])
            # Ty[x-1] = iS[indMin[x-1]]
            print(x)
            Ty[diffPoints_Opt[x]-1] = iS[indMin[x]]

        rTy = Ty


        print('Ay yo')


    return 0