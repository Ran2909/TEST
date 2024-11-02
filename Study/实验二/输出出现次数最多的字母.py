import string
#输入字符串
strings=input('Please enter the target string:')

#字符串中出现的字母转列表并将元素从小到达排序
string_list=[i for i in strings if i in string.ascii_letters]
string_list.sort()

#将元素和元素出现频次作为键值对录入字典
dict={}
for i in string_list:
    if i not in dict.keys():
        dict[i]=string_list.count(i)

#求出最大频次并和字典中的值比较，输出出现频次最多的元素
max_number=dict[max(dict,key=dict.get)]
for key in dict:
    if dict[key]==max_number:
        print(key,dict[key])


