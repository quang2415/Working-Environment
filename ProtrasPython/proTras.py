from normalize import normalize
from get_init_point import get_init_point

def proTras(NT):
    n,p = NT.shape
    print('Size data : ')
    print(NT.shape)
    eps = 0.1
    T = normalize(NT)
    s = 1
    x_init = get_init_point(T)



    return 0