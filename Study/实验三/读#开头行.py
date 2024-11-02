#打开文件
with open('D:\pythonProject\学习\作业\实验三\开头行.txt','a+', encoding='utf-8') as file:
    file.seek(0)

    #将每一行的字符存储在strings列表中
    strings=file.readlines()
    for i in range(0,len(strings)):

        #判断该行首字符是否是‘#’
        if strings[i][0]=='#':
            continue
        print(strings[i],end='')
