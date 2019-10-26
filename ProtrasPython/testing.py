import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, 100, 95],
        'Second Score': [30, 30, 30, 56],
        'Third Score': [52, 52, 52, 98],
        'Fourth Score': [82, 82, 82, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
# print(df.drop_duplicates(subset="Second Score"))
# print(df.drop([0]).reset_index(drop=True))

def test (a, b, *c):
    if(len(c)==0):
        print("Fuck yeah")

print(np.identity(3))