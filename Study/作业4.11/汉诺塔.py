print('有三个柱子，分别为A,B,C。默认所有盘最初都在A柱上')
flag=0
def hanoi(n, start, target, another):
    global flag
    flag=flag+1
    if n == 1:
        print(f"把第 1 个盘从 {start} 移动到 {target}")
    else:
        #自己验算汉诺塔得出的规律
        hanoi(n - 1, start, another, target)
        print(f"把第 {n} 个盘从 {start} 移动到 {target}")
        hanoi(n - 1, another, target, start)
start=input("你想从哪个柱子开始")
target=input('你想将所有盘移动到哪个柱子')
another=input('剩下那个柱子是哪个柱子')
num=int(input('一共有几个盘'))
hanoi(num, start, target, another)
print('一共移动了%d次'%flag)