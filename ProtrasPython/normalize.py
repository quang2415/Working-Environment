import math

def normalize(NT):
    Ecart = 0
    Moy = 0
    N_pattern, p = NT.shape
    print(N_pattern,p)

    for k in range(0,p):
        for i in range(0,N_pattern):
            Moy = Moy + NT.at[i,k]

        Moy = Moy / N_pattern

        for i in range(0,N_pattern):
            Ecart = Ecart + (Moy - NT.at[i,k])*(Moy - NT.at[i,k])

        Ecart = math.sqrt(Ecart/N_pattern)
        NT.loc[:,k] = (NT.loc[:,k] - Moy)/Ecart
        Ecart = 0
        Moy = 0

    NT = NT.round(6)
    print(NT)
    return NT