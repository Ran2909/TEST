import pandas as pd
df=pd.read_csv("titanic_test.csv")
print(df.head())
df.info()
print(df.index)
print(df.columns)
print((df.values))