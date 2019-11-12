import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, 100, 95],
        'Second Score': [30, 30, 30, 56],
        'Third Score': [52, 52, 52, 98],
        'Fourth Score': [82, 82, 82, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)
# print(df)

# print(df.drop_duplicates(subset="Second Score"))
# print(df.drop([0]).reset_index(drop=True))


a = np.array([1, 3, 2, -4, 5, 7, 10])
b = np.array([[3, 0],[-1, 5]])
c = np.asarray([[0]])
# d = [0]
# print(a.argmin(axis=1))
# print(a.min())
# print(b[np.ix_(c.flatten())])

e = np.array([True,True,False,True,True,True,True])
a[e] = []
print(a)

# e = np.insert(a,len(a),0)
# f = b.min(1)
# print(f)

# a = np.asarray(np.linspace(1,n,num=n, dtype=int)).transpose()

# a = np.linspace(1,n,num=n, dtype=int).reshape(n,1)
# x = 15
# S = []
# S.append(x)
# print(S[-1])

is_prime = np.ones((100,), dtype=bool)
print(is_prime)
is_prime[:2] = 0
print(is_prime)

index_remove_elements = np.full((10,1), False)
rTy = np.asarray([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]])
# rTy(index_remove_elements) = []
print('End')