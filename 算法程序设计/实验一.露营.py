import random

# 生成随机的宿营地距离
def campsite_distances(n):
    '''一共有n个露营地，列表首个元素是出发点，所以存储了n+1个元素'''
    distances=[0]*(n+1)

    '''相邻两个宿营地之间的距离不超过30km'''
    for i in range(1,n+1):
        distances[i]=random.randint(1,30)+distances[i-1]
    return distances

# 使用贪心算法选择宿营地
def select_campsites(distances):
    current_position = 0
    camp_days = 0
    n = len(distances)
    print('当前位置为', current_position)
    while current_position < n:
        next_campsite = current_position+1

        '''一天最多移动30km，所以直接走到30km以内的最远露营地'''
        while (next_campsite < n and distances[next_campsite] - distances[current_position] <= 30):
            print("距离为",distances[next_campsite] - distances[current_position])
            next_campsite = next_campsite+1

        if next_campsite==n:
            return camp_days + 1

        next_campsite =next_campsite-1
        camp_days =camp_days+ 1
        current_position = next_campsite
        print('下一位置为', next_campsite)

    return camp_days+1

# 生成随机的宿营地距离
n=int(input('一共有多少个露营地？'))
distances = campsite_distances(n)
print("宿营地距离列表:", distances)

# 使用贪心算法选择宿营地
min_camp_days = select_campsites(distances)
print("总的宿营天数:", min_camp_days)

