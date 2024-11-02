import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_excel('乘客与航班数据.xlsx',sheet_name='sheet1')
year = df.iloc[0:5, 0].values.tolist()
month=list(df.columns[1:13])
total=df.iloc[0:5,14].values.tolist()

#分析年度乘客总量变化情况（折线图）
plt.plot(year,total,marker='o')
plt.xticks(year)
plt.title('Total numbers of passengers in a year')
plt.show()

'''获取每一年每一个月的乘客数'''
number=[]
for i in range(1,5):
    number.append(df.iloc[i, 1:13].values.tolist())


#分析年度乘客总量变化情况（折线图）

fig, years = plt.subplots(5, 1,figsize=(6,16))
fig.subplots_adjust(hspace=0.8)
for i in range(0,5):
    years[i].bar(month,number[i-1])
    years[i].set_title('%d(year)'%(i+2018),fontname='Arial',fontsize='20')
    years[i].set_xlabel('month')
    years[i].set_ylabel('number')
    years[i].set_xlim(0,12)
    years[i].set_ylim(5000,10000)
plt.show()

#分析乘客的类别和比重（饼图）
type=list(df.columns[14:19])
type_number=[]
for i in range(0,5):
    type_number.append(df.iloc[i, 14:19].values.tolist())
colors = ['#ff9999', '#66b3ff', '#99ff99']
autopct = '%1.1f%%'
fig,ax=plt.subplots(5,1,figsize=(4,16))
for i in range(0,5):
    ax[i].pie(type_number[i],labels=type,colors=colors,autopct=autopct, startangle=90)
    ax[i].set_title('%d(year)'%(i+2018))
plt.show()

#分析影响航空公司收入的乘客的各项属性的重要性（雷达图）
angles = np.linspace(0, 2 * np.pi, len(type), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
fig, ax = plt.subplots(1, 5, figsize=(25, 6))
for i in range(0,5):
    max_value = max(type_number[i])
    values = [v / max_value for v in type_number[i]]
    values = np.concatenate((values, [values[0]]))
    ax[i] = fig.add_subplot(1, 5, i + 1, polar=True)
    ax[i].plot(angles, values, '-o', linewidth=2)
    ax[i].fill(angles, values, alpha=0.25)
    ax[i].set_thetagrids(angles[:-1] * 180 / np.pi, type)
    ax[i].set_title('%d(year)'%(i+2018))
plt.show()