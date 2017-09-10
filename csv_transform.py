import pandas as pd
import numpy as np

df = pd.read_csv('./P00000001-WA.csv', index_col=False)

print(df.head(5))

selected = df.iloc[:, np.r_[2:5, 6:11, 17]]

print(selected.head(5))

selected.to_csv('selected.csv')
