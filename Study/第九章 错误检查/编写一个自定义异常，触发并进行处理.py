class Numerror(Exception):
    def __init__(self,value):
        self.value=value
        self.__class__.__name__=self.__class__.__name__

    def __Getstr__(self):
        return repr(self)+'第%d个数据有误'%(i+1)
i=-1
string=input('请输入一段数字')
while (True and i<len(string)-1):
    try:
        i=i+1
        if string[i] not in ['0','1','2','3','4','5','6','7','8','9']:

            raise Numerror(string[i])

    except Numerror as ne:
        print(ne.__class__.__name__,'已触发，值为',ne.value)
        print(ne.__Getstr__())