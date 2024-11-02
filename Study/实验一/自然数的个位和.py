# 输入两个自然数
natural_number1=int(input('Please input a natural number\n'))
natural_number2=int(input('Input a natural number again\n'))
flag=0
# 使用while循环检验输入的数据
while flag!=2:
    flag=0
    if natural_number1<0:
        print('The first number is not a natural number.Please input it again')
        natural_number1=int(input())
    else:
        flag=flag+1
    if natural_number2 < 0:
            print('The second number is not a natural number.Please input it again')
            natural_number2 = int(input())
    else:
        flag=flag+1
# 输出两个自然数的个位之和
print(natural_number1%10+natural_number2%10)




