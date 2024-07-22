# gpt가 작성한 코드
from collections import deque

def dfs(v):
    visited[v] = True
    dfs_result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for key in graph.keys():
    graph[key].sort()

visited = [False] * (n + 1)
dfs_result = []
dfs(v)
print(' '.join(map(str, dfs_result)))

visited = [False] * (n + 1)
bfs_result = []
bfs(v)
print(' '.join(map(str, bfs_result)))