import pandas as pd

data={'country':['aaa','bbb','cccc'],
      'population':[10,14,12]}
df_data=pd.DataFrame(data)
#print(df_data)
'''自己创建一个dataframe结构'''
#print(df_data.info())
'''取指定数据'''
df=pd.read_csv("titanic_test.csv")
age=df['Age']
#print(age[:5])
'''series : dataframe中的一列或一行'''
#print(age.index)
#print(age.values)
#print(df['Age'][:5])
'''指定索引'''
df=df.set_index('Name')
#print(df.head())
#print(age)
#print(age.mean())
#print(age.max())
print(df.describe())