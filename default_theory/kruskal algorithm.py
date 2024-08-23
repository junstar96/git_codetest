#그리디 알고리즘의 일종
#그리디 알고리즘 : 순간순간 최선의 결과값만을 뽑아내 보도록 한다.

# node_list = dict()
# #풀이 방법 : 정렬 후 최소 간선들끼리 연결하고 그 가운데 사이클이 생기지 않도록 한다.
#
# input_data1 = [('a','f', 10), ('c', 'd', 12),('b','g',15),
#                ('b','c',16),('d','g',18),('d','e',22),
#                ('e','g',25),('e','f',27),('a','b', 29)]
#
# input_data1.sort(key=lambda x:x[2],reverse=True)
#
# footstep_list = list()
#
#
# while input_data1:
#     check = input_data1.pop()
#     start,finish,value = check[0],check[1],int(check[2])
#
#
#
#     if start in footstep_list and finish in footstep_list:
#         continue
#     else:
#         if start not in footstep_list:
#             footstep_list.append(start)
#
#         if finish not in footstep_list:
#             footstep_list.append(finish)
#
#         print(value)


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_mst(V, edges):
    # 간선들을 가중치 순으로 정렬
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(V)
    mst = []
    mst_weight = 0

    for u, v, weight in edges:
        # 두 정점이 다른 집합에 있다면, 해당 간선을 MST에 포함시킴
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v))
            mst_weight += weight

    return mst, mst_weight

# Example usage
V = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst, total_weight = kruskal_mst(V, edges)

print(f"MST의 간선들: {mst}")
print(f"MST의 총 가중치: {total_weight}")