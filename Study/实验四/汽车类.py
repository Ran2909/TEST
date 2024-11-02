class car:
    def __init__(self,color,horsepower,type):
        self.color=color
        self.horsepower=horsepower
        self.type=type

    def move(self, color,horsepower,type):
        self.color=color
        self.horsepower=horsepower
        self.type=type

class BMW_X9(car):
    def __init__(self,color, horsepower, type):
        super().__init__(color,horsepower,type)
        self.color='white'
        self.horsepower='609'
        self.type='sport'
    def __str__(self):
        return '型号:'+__class__.__name__+\
               '\n颜色:'+self.color+\
               '\n马力:'+self.horsepower+\
               '\n车型:'+self.type

class AUDI_A9(car):
    def __init__(self, color, horsepower, type):
        super().__init__(color,horsepower,type)
        self.color='grey'
        self.horsepower='605'
        self.type='business'
    def __str__(self):
        return '型号:'+__class__.__name__+\
               '\n颜色:'+self.color+\
               '\n马力:'+self.horsepower+\
               '\n车型:'+self.type


bwm=BMW_X9('white','609','sport')
audi=AUDI_A9('grey','605','business')
print(bwm)
print('')
print(audi)
print('')
audi.move('black','609','sport')
print(audi)