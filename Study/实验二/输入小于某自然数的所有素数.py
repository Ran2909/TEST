#输入一个大于2的整数
num = int(input("Enter a natural number greater than 2: "))
list = []

# 设立标识，用于输出素数
flag=1

#循环判断求出素数
for i in range(2, num):
    flag=1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag=0
            break
#满足条件，将素数纳入列表
    if flag==1:
        list.append(i)
print(list)