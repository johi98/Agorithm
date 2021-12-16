n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

def dfs(x, y):
    # 범위 초과시 그만
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 재귀함수를 통해 현재 노드에서 이어져있는 모든 노드를 탐색
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
# 하나씩 다 넣어봄
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)