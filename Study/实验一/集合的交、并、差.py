# 输入setA和setB
setA = set(input('Please input elements in setA and separate them with spaces\n').split())
setB = set(input('Please input elements in setB and separate them with spaces\n').split())
# 求交集
intersection = setA.intersection(setB)
print('The intersection of set A and set B is ', intersection)
# 求并集
union = setA.union(setB)
print('The union of set A and set B is ', union)
# 求差集
difference = setA.difference(setB)
print('The difference between set A and set B is ', difference)
