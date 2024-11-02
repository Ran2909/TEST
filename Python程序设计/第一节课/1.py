'''A=0x1e
print(A^True)
x="你"
print(ord(x))
for i in range(0,128):
    print(i,chr(i),hex(i))

a=50.5
print('score is '+str(a))

for item in range(0,10):
    print(item,end='*')

f=open('date.txt','a')
print('hello,file.',file=f)

a=50
print('%o'%int(a))

a=55.54655466
print('%.3g'%a)
print('%.3e'%a)
print('%x'%int(a))
print(hex(int(a)))
print(oct(int(a)))
print(bin(int(a)))

a='wdnmd'
print('%-10.2s'%a)
print(a[-3:])

name='zhangsan'
score=86
print("%s's score is %d"%(name,score))
'''
'''from time import *
for a in range(100):
    print('\r'+str(a)+'%',end='')
    sleep(.5)

name='zhangsan'
score=85
print(f"{name}'s score is {score}")
print("{:s}'s score is {:d}".format(name,score))
print("{a}{b}".format(a=name,b=score))

a=56
b=6
print(a%b)

print(5<a<100<b*23)

a=56.56-0.1-0.1-0.1
print(a==56.53)
print(abs(a-56.53)<0.1)
print(True and False ^ True)
print("a\t\t",'b\t\t','a and b\t','a^b')
for a in [True,False]:
    for b in [True,False]:

        print(a,'\t',b,'\t',a and b,'\t\t',a^b)
'''