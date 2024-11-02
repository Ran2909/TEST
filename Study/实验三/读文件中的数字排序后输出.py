
with open('D:\pythonProject\学习\作业\实验三\混杂数字串.txt','r+') as file:
    number = ['0','1','2','3','4','5','6','7','8','9']
    strings=file.readlines()
    strings=''.join(strings)
    num=[i for i in strings if i in number]
    num.sort()
    num=''.join(num)

with open('D:\pythonProject\学习\作业\实验三\混杂数字串.txt','w') as file:
    file.write(num)



