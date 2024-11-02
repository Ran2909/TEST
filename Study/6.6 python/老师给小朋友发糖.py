import random

num =int(input('有几个小朋友？'))
candy = [0] * num
for i in range(0, num):
    candy[i] = random.randint(0, 3)
    candy[i] = candy[i] * 2
    print('第%d个小朋友有%d个糖果' % (i+1, candy[i]))
print('\n')
def repeat():
    flag=1
    for i in range(0, num-1):
        candy[i] = int(candy[i]//2 + candy[i+1]//2)
        if candy[i]%2!=0:
            candy[i]=candy[i]+1
        print('第%d个小朋友有%d个糖果' % (i+1, candy[i]))
    candy[-1] = int(candy[-1]//2 + candy[0]//2)
    if candy[-1] % 2 != 0:
        candy[-1] = candy[-1] + 1
    print('第%d个小朋友有%d个糖果\n' % (num, candy[-1]))
    for i in range(0,num-1):
        if candy[i]!=candy[i+1]:
            flag=0
            break
    if flag==0:
        repeat()
repeat()