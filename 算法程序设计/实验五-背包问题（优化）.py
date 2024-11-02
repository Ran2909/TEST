import time
def Max_Value(n, W, V, weights, volumes, values):
    # 创建一个二维数组dp，dp[j][k]表示总重量不超过j、总体积不超过k时的最大价值
    dp = [[0] * (V + 1) for _ in range(W + 1)]
    # 遍历每种物品
    for i in range(n):
        for j in range(weights[i], W + 1):  # 考虑质量
            for k in range(volumes[i], V + 1):  # 考虑体积
                # 更新状态，选择当前物品的最优解
                dp[j][k] = max(dp[j][k], dp[j - weights[i]][k - volumes[i]] + values[i])
    #返回最大价值
    return dp[W][V]
n = 6
W = 30
V = 50
weights = [1,2,3,5,8,9]
volumes = [2,3,7,5,13,11]
values = [1,3,8,8,19,17]
start=time.perf_counter()
# 调用函数，计算最大价值
max_value = Max_Value(n, W, V, weights, volumes, values)
end=time.perf_counter()
# 输出结果
print("最大价值:", max_value)
print("运行时间为",end-start)