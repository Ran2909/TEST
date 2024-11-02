import time
def max_value(n, W, V, weights, volumes, values):

    # 初始化dp数组
    dp = [[[0 for _ in range(V + 1)] for _ in range(W + 1)] for _ in range(n + 1)]
    max_index = [[0 for _ in range(V + 1)] for _ in range(W + 1)]
    # 动态规划求解最大总价值
    start=time.perf_counter()
    for i in range(1, n + 1):
        for j in range(1, W + 1):  # 考虑质量
            for k in range(1, V + 1):  # 考虑体积
                if weights[i - 1] > j or volumes[i - 1] > k:
                    dp[i][j][k] = dp[i - 1][j][k]
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k],dp[i][j - weights[i - 1]][k - volumes[i - 1]] + values[i - 1])
                    max_index[j][k] =i
    end = time.perf_counter()
    print(end-start)

    # 返回结果
    return dp[n][W][V]
# 测试代码
n = 6
W = 30
V = 50
weights = [1,2,3,5,8,9]
volumes = [2,3,7,5,13,11]
values = [1,3,8,8,19,17]
max_value = max_value(n, W, V, weights, volumes, values)
print("最大总价值为：", max_value)

