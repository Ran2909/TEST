def bubbles(a):
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
    return a
list=input('请输入所有需要排序数字，并用空格隔开').split()
#把数字字符转换成数字
a=[int(i) for i in list]
print(bubbles(a))