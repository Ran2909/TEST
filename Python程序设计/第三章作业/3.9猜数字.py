import random
derive_number=random.randint(1,1000)
print(derive_number)
number=input('Guess a number')
number=int(number)
while derive_number!=number:
    if derive_number>number:
        print('Guess a larger number')
    else :
        print('Guess a smaller number')
    number=input()
    number=int(number)
print('Right')