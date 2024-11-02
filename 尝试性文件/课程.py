
words=input("你想对阎王说什么话\n")
list=''
str = [i for i in words]
for i in range(len(str)):
    a_ascii = ord(str[i])
    a_b = bin(a_ascii)[2:]
    list=list+'{:0>8b}'.format(a_ascii)
print("\"阎王，{0}\"".format(words))

print('已向生死簿中写入\"{0}\"'.format(list))
resurrection=0
death=0
for i in list:
    if i=='1':
        resurrection+=1
        print("被试，堂堂复活！！")
    else:
        death+=1
        print("...")
print('被试死去了{0}次，复活了{1}次'.format(resurrection,death))
if list[-1]=="1":
    print("被试存活...")
else:
    print("被试已死...")