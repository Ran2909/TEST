#建立字典
number=dict()

#用for循环建立201条字典数据
for i in range(1,202):
    number[i]=['xiaoming%d'%i,'xiaoming%d@china.com'%i,'pwd%d'%i]
page=int(input('Please enter the page that you want to query'))
while page>21:
    page=int(input('Only 21 pages.Please enter page again.'))

#输出目标页数中的数据
for i in range((page-1)*10+1,page*10+1):
    if i>201:
        break
    else:
        for j in range(0,3):
            print(number[i][j],end=' ')
        print()
