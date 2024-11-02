import re

def find_IP_addresses(string):
    # 定义正则表达式
    pattern = r'(?:\d{1,3}\.){3}\d{1,3}'
    matches = re.findall(pattern, string)

    return set(matches)  #除去重复IP
# 测试
string = '这是一段包含了多个IP地址（192.168.0.1、10.0.0.1）的测试文本'
print(find_IP_addresses(string))
string1=input('请输入其他测试文本')
print(find_IP_addresses(string1))