import numpy as np
import math

def distance2(X, Y, *A):
    if(len(A)==0):
        A = np.identity(X.shape[1])

    # D = math.sqrt((-2*X*A*Y.getH())+(X*A*X).sum(axis=1) + (Y*A*Y).sum(axis=1))
    # print(type(X))

    print(type(X))
    X = X.to_numpy()
    print(type(X))

    Y = np.asarray(Y)
    Y = Y.transpose()
    print(type(Y))
    # print(Y.transpose())

    print('Ay yo')