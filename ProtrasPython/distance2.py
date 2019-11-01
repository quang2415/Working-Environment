import numpy as np
import math

def distance2(X, Y, *A):
    if(len(A)==0):
        A = np.identity(X.shape[1])

    Y = (np.asarray(Y)).reshape(1,len(Y))

    X = np.asarray(X)

    D = ((-2*X).dot(A)).dot(Y.transpose())

    E = ((X.dot(A)) * X).sum(axis=1)

    E = E.reshape(E.shape[0],1)

    F = (((Y.dot(A))*Y).sum(axis=1)).transpose()

    G = np.sqrt(D + E + F)
    return G
    # print(G.sum(axis=0))