import time

def unbounded_knapsack_2constraints(n, W, V, weights, volumes, values):
    # 创建一个二维数组dp，dp[i][j]表示总重量不超过j、总体积不超过i时的最大价值
    dp = [[0] * (W + 1) for _ in range(2)]

    # 遍历每种物品
    for i in range(n):
        # 拷贝上一层的状态到当前层
        dp[0] = dp[1][:]
        # 逐个考虑每种重量
        for j in range(weights[i], W + 1):
            # 逐个考虑每种体积
            print(dp,end='\n\n')
            for k in range(volumes[i], V + 1):
                # 更新状态，选择当前物品的最优解
                dp[1][j] = max(dp[1][j], dp[0][j - weights[i]] + values[i])

    # 返回总重量不超过W、总体积不超过V时的最大价值
    return dp[1][W]

n = 6
W = 30
V = 50
weights = [1, 2, 3, 5, 8, 9]
volumes = [2, 3, 7, 5, 13, 11]
values = [1, 3, 8, 8, 19, 17]

start = time.perf_counter()
# 调用函数，计算最大价值
result_unbounded_2constraints = unbounded_knapsack_2constraints(n, W, V, weights, volumes, values)
end = time.perf_counter()

# 输出结果
print("带有两个约束条件的完全背包问题的最大价值:", result_unbounded_2constraints)
print("运行时间为", end - start)
