def pyramid(n):
    for i in range(1,n+1):
        num='*'*(2*i-1)
        #居中对齐
        print('{0:^{1}}'.format(num,2*n))
num=int(input('How many layers does your pyramid have?'))
pyramid(num)