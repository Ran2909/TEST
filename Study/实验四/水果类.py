class Fruit:
    def __init__(self,color):
        self.color=color

class apple(Fruit):
    def __init__(self, color):
        super().__init__(color)
    def __str__(self):
        return 'It is an '+__class__.__name__+'. It is '+self.color+'.'

class orange(Fruit):
    def __init__(self, color):
        super().__init__(color)
    def __str__(self):
        return 'It is an '+__class__.__name__+'. It is '+self.color+'.'

class watermelon(Fruit):
    def __init__(self, color):
        super().__init__(color)
    def __str__(self):
        return 'It is a '+__class__.__name__+'. It is '+self.color+'.'

a=apple('red')
o=orange('orange')
w=watermelon('green')
print(a)
print(o)
print(w)
