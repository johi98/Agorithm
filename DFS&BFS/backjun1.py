import sys


def dfs(v):
    global count
    visited[v] = True
    for k in graph[v]:
        if not visited[k]:
            dfs(k)
            count += 1


n = int(input())
m = int(input())
count = 0
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)

dfs(1)

print(count)
