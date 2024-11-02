class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return 'point('+str(self.x+other.x)+','+str(self.y+other.y)+')'

    def __sub__(self, other):
        return 'point('+str(self.x-other.x)+','+str(self.y-other.y)+')'

    def __mul__(self, other):
        return 'point('+str(self.x*other)+','+str(self.y*other)+')'

    def __floordiv__(self, other):
        return 'point('+str(self.x/other)+','+str(self.y/other)+')'
a,b=Point(4,5),Point(2,3)
print(a+b)
print(a-b)
print(a*2)
print(a//2)

