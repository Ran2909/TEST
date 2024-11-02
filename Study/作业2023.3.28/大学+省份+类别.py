#建立字典，一个键对应一个包含两个键的字典
university={'清华大学':{'province':'北京','type':'985 211'},
            '西南大学':{'province':'重庆','type':'211'},
            '重庆交通大学':{'province':'重庆','type':'双一流'}}

#遍历输出字典
for key in university:
    print(key,university[key])
