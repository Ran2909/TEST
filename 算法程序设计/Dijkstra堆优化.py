import time

start=time.perf_counter()

class GNode:
    def __init__(self, vertex, distance):
        self.vertex = vertex  # 节点编号
        self.distance = distance  # 两点间的距离
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # 结点
        self.graph = [[float('inf') for column in range(vertices)] \
                      for row in range(vertices)]  # 初始化邻接矩阵，"inf"表示两点间没有边相连，"0"表示该点到本身的距离
        self.min_distance= [0]+[65536] * (self.V-1) # 初始化 起始结点 到 所有结点 的最短距离

    # 为所有路径复制随机距离，便于测试代码稳定性
    def random_distance(self,V,graph):

        import random

        # 距离矩阵是对称矩阵
        # 只为上三角矩阵随机数生成，剩下的一半直接对称赋值
        for i in range(V):
            for j in range(i+1,V):
                if self.graph[i][j]==1:  # 表示 i,j两点有边相连
                    self.graph[i][j]=random.randint(1,100) # 生成随机距离
                    self.graph[j][i]=self.graph[i][j] # 对称赋值
                else:
                    self.graph[i][j]=float('inf')
                    self.graph[j][i]=self.graph[i][j]
            print(self.graph[i])

    #迪杰斯特拉算法求最短路径
    def Dijkstra(self,s,graph):
        import heapq
        G = {}
        for i in range(len(graph)):
            G[i] = {}
            for j in range(len(graph)):
                if graph[i][j] != 0 and graph[i][j] != float('inf'):
                    G[i][j] = graph[i][j]
        print(G)
        INF = 999999999

        dis = dict((key, INF) for key in G)  # start到每个点的距离
        dis[start] = 0
        vis = dict((key, False) for key in G)  # 是否访问过，1位访问过，0为未访问
        ###堆优化
        pq = []  # 存放排序后的值
        heapq.heappush(pq, [dis[start], start])

        t3 = time.time()
        path = dict((key, [start]) for key in G)  # 记录到每个点的路径
        while len(pq) > 0:
            v_dis, v = heapq.heappop(pq)  # 未访问点中距离最小的点和对应的距离
            if vis[v] != False:
                continue
            vis[v] = True
            p = path[v].copy()  # 到v的最短路径
            for node in G[v]:  # 与v直接相连的点
                new_dis = dis[v] + float(G[v][node])
                if new_dis < dis[node] and (not vis[node]):  # 如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                    dis[node] = new_dis  # 更新点的距离
                    #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                    heapq.heappush(pq, [dis[node], node])
                    temp = p.copy()
                    temp.append(node)  # 更新node的路径
                    path[node] = temp  # 将新路径赋值给temp

        t4 = time.time()
        print('Dijkstra算法所用时间:', t4 - t3)
        return dis, path

    def Floyd(self, V, start_vertex, end_vertex):
        dist = self.graph.copy()  # 复制邻接矩阵
        path = [[-1 for row in range(V)] for column in range(V)]  # 中间结点矩阵

        # Floyd算法的主循环
        for k in range(self.V):  # 遍历所有可作为中间结点的顶点
            for i in range(self.V):  # 遍历所有顶点对
                for j in range(self.V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:  # 如果经过中间结点k的路径更短
                        dist[i][j] = dist[i][k] + dist[k][j]  # 更新最短路径长度
                        path[i][j] = k  # 记录中间结点k

        print("最短路径为:", end="")
        print(0, end=' ')  # 输出起始顶点
        self.printPath(start_vertex, end_vertex, path)  # 调用打印路径的函数

    def printPath(self, start_vertex, end_vertex, path):
        if path[start_vertex][end_vertex] == -1:  # 如果不存在中间结点，则直接输出结束顶点
            print('->', end_vertex, end=" ")
        else:
            mid = path[start_vertex][end_vertex]  # 获取中间结点
            self.printPath(start_vertex, mid, path)  # 递归打印路径：起始顶点到中间结点
            self.printPath(mid, end_vertex, path)  # 递归打印路径：中间结点到结束顶点


# 测试代码
vertex_num=7
g = Graph(vertex_num)
g.graph = [[0, 1, 1, 0, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0],
           [1, 1, 0, 1, 1, 0, 0],
           [0, 1, 1, 0, 1, 1, 0],
           [0, 0, 1, 1, 0, 1, 1],
           [0, 0, 0, 1, 1, 0, 1],
           [0, 0, 0, 0, 1, 1, 0]]
g.random_distance(vertex_num,g.graph)
# 迪杰斯拉算法
print("\033[31m迪杰斯特拉算法\033[0m")
g.Dijkstra(0,g.graph)
# 佛洛依德算法
print("\033[31m佛洛依德算法\033[0m")
g.Floyd(vertex_num,0,4)

end=time.perf_counter()
print("\n\n运行时间:",end-start)

