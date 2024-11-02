num=int(input('How many fibonacci numbers do you want to get'))
fib=[0,1]
def fibonacci(n):

    if n==1:
        return([fib[0]])
    elif n==2:
        return(fib)
    else:
        #斐波那契数列
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
            return fib
print(fibonacci(num))