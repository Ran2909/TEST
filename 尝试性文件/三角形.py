import numpy as np
import matplotlib.pyplot as plt

# 计算两个点之间的欧式距离
def euclidean_distance(point1, point2):
    distance = np.sqrt(np.sum((point1 - point2)**2))
    print(f"计算点 {point1} 和点 {point2} 的欧式距离：{distance}")
    return distance

# 计算簇内的平均距离
def average_distance(cluster):
    total_distance = 0
    n = len(cluster)
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean_distance(cluster[i], cluster[j])
            total_distance += distance
    average = total_distance / (n * (n-1) / 2)
    print(f"计算簇内平均距离：{average}")
    return average

# 层次聚类算法
def hierarchical_clustering(data, n_clusters):
    clusters = [[point] for point in data]

    while len(clusters) > n_clusters:
        min_distance = float('inf')
        merge_index = None

        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                distance = average_distance(clusters[i] + clusters[j])
                if distance < min_distance:
                    min_distance = distance
                    merge_index = (i, j)

        i, j = merge_index
        clusters[i] += clusters[j]
        del clusters[j]

        # 输出合并过程
        print(f"第 {len(clusters)} 次合并:")
        print(f"合并簇 {j+1} 到簇 {i+1}")
        print(f"当前聚类结果：{clusters}")
        print("")

    return clusters


# 生成随机数据集
def generate_data(num_points):
    return np.random.randint(0, 20, size=(num_points, 2))

# 展示聚类结果
def plot_clusters(clusters, title):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], color=colors[i % len(colors)], label=f'Cluster {i+1}')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

# 生成随机数据集
data = [[ 6,18],[ 1,16]
 ,[15,7]
 ,[ 2,18]
 ,[ 9,17]]
print("原始数据集：", data)
data=np.array(data)
# 层次聚类
hierarchical_clusters = hierarchical_clustering(data, 2)
print("层次聚类结果：", hierarchical_clusters)
plot_clusters(hierarchical_clusters, 'Hierarchical Clustering')
