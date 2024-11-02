import numpy as np

def min_time_scheduling(tasks):
    n = len(tasks)  # 任务数量

    # 动态规划数组，max_time[i][j]表示前i个任务分配到机器上总时间为j的最大时间
    max_time = np.zeros((n + 1, sum(tasks) // 2 + 1), dtype=int)

    # 标记数组，flag[i][j]表示前i个任务是否分配到机器上总时间为j的方案中
    flag = np.zeros((n + 1, sum(tasks) // 2 + 1), dtype=int)

    # 保存每个任务分配的机器编号，默认为0
    allocate = np.zeros(n + 1, dtype=int)

    # 动态规划过程，计算最大总时间和方案
    for i in range(1, n + 1):
        for j in range(1, sum(tasks) // 2 + 1):
            if j >= tasks[i - 1]:

                # 当前任务分配到机器上总时间为j的方案时间更长
                if max_time[i][j] <= max_time[i - 1][j - tasks[i - 1]] + tasks[i - 1]:
                    # 更新最大总时间
                    max_time[i][j] = max_time[i - 1][j - tasks[i - 1]] + tasks[i - 1]
                    flag[i][j] = 1  # 标记当前方案可行
                else:
                    max_time[i][j] = max_time[i - 1][j]  # 不选择当前任务
            else:
                max_time[i][j] = max_time[i - 1][j]  # 不选择当前任务

    V = sum(tasks) // 2  # 目标总时间的一半
    while V >= 0 and flag[n][V] == 0:  # 找到最大总时间对应的方案
        V -= 1

    print("最小总调度时间:", max(max_time[n][V], sum(tasks) - max_time[n][V]))  # 输出最大总时间
    print("任务分配:")
    for i in range(1, n + 1):
        if allocate[i] == 0 and max_time[i][V] == max_time[i - 1][V]:
            allocate[i] = 0  # 当前任务没有分配到机器上总时间为V的方案
        elif max_time[i][V] > max_time[i - 1][V]:
            V -= tasks[i - 1]  # 当前任务分配到机器上总时间为V的方案
            allocate[i] = 1

        print("任务", i, "由机器", allocate[i] + 1,"完成")  # 输出每个任务的机器编号

tasks = [2, 9, 9, 8, 8, 6, 7, 8, 6, 9]
print(tasks)
print(sum(tasks))
min_time_scheduling(tasks)
