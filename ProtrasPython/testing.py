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
b = np.array([[3, 0],[1, 5]])
c = np.asarray([[0]])
d = [0]
# print(a.argmin(axis=1))
# print(a.min())
# print(b[np.ix_(c.flatten())])

e = np.insert(a,len(a),0)
print(e)

# a = np.asarray(np.linspace(1,n,num=n, dtype=int)).transpose()

# a = np.linspace(1,n,num=n, dtype=int).reshape(n,1)
# x = 15
# S = []
# S.append(x)
# print(S[-1])
