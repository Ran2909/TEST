pi=3.14
radius=float(input('请输入圆的半径'))

#自定义错误
class NegativeError(Exception):
    def __init__(self):
        self.__class__.__name__='NegativeError is triggered'
    def judge(self):
        return repr(NegativeError)
#try/except
try:
    if radius<0:
        raise NegativeError
    print(pi*(radius*radius))

except NegativeError as N:
    print(N.__class__.__name__)
