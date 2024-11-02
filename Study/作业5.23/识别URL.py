import re
s = input("请输入字符串")

# 定义正则表达式
p = r'(?:\'|\")?(https?|ftp)?://(?:www\.)?(\w+\.)*\w{2,}(?:\'|\")?(?:/\S*)?'

# 匹配
match = re.search(p, s)
print(match)
# 输出结果
if match:
    print(f"Found URL: {match.group()}")
else:
    print("No URL found.")