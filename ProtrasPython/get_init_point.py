from distance2 import distance2

def get_init_point (T):
    n,p = T.shape
    vitual_point = []

    for c in range (0,p):
        # print(min(T.loc[:,c]))
        vitual_point.append(min(T.loc[:,c]))

    print(vitual_point)

    T = T.drop_duplicates()
    print(T)
    for x in range(0,T.shape[0]):
        print(T.loc[x,:].tolist())
        if(vitual_point==T.loc[x,:].tolist()):
            T = T.drop([x])
    diffT = T.reset_index(drop=True)
    d = distance2(diffT,vitual_point)