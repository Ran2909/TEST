#建立列表
score=[0]*5

#输入评委打分
for i in range(0,5):
    score[i]=int(input('请输入第%d个评委的打分'%(i+1)))
    while score[i]<0 or score[i]>10:
        score[i] = int(input('输入数据有错，请重新输入'))

#将评分排序再去掉列表的首尾项就相当于去掉一个最高分和一个最低分
score.sort()
del score[0]
score.pop()

#计算最终得分并输出
final_score=(score[0]+score[1]+score[2])/3
print('该选手的最终得分为%d'%final_score)