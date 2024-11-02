strings=input('请输入待检测字符串')

class yorn:

    #初始化
    def __init__(self,string):
        self.string=[i for i in string]


    #单独将括号存储到一个新列表中
    def delete(self):
        brackets = ['{', '}', '(', ')', '<', '>', '[', ']']
        self.string=[i for i in self.string if i in brackets]
        '''print(self.string)'''
        return self.string

    #判断部分
    def judge(self):
        flag=0
        brackets = ['{', '}', '(', ')', '<', '>', '[', ']']
        #单数括号肯定少
        if len(self.string) % 2 !=0:
            print('搭配错误')
        #双数括号判断搭配
        if len(self.string) % 2 == 0:
            for i in range(0,len(self.string)//2):
                '''print([self.string[i],self.string[len(self.string)-1-i]])'''
                if (self.string[i]==brackets[0]) and (self.string[len(self.string)-1-i]==brackets[1])\
                        or (self.string[i]==brackets[2]) and (self.string[len(self.string)-1-i]==brackets[3])\
                        or (self.string[i]==brackets[4]) and (self.string[len(self.string)-1-i]==brackets[5])\
                        or (self.string[i]==brackets[6]) and (self.string[len(self.string)-1-i]==brackets[7]):
                   flag=0
                else:
                    flag=1
                    print('搭配不正确')
                    break
            if flag==0:
                print('搭配正确')

string=yorn(strings)
string.delete()
string.judge()


