from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 0이 들어가는 것은 짝을 맞추기 위해서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs1(x, y):
    queue = deque()
    queue.append((x, y))

    # queue 가 false 로 나오는 경우는 비어있다는 뜻
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:

                continue
            if graph[nx][ny] == 0:

                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


def bfs2(x, y):
    queue = deque()
    queue.append((x, y))

    # queue 가 false 로 나오는 경우는 비어있다는 뜻
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] < graph[x][y]:
                print("[", x, "],[", y, "]")
                queue.append((nx, ny))

    return 0


print(bfs1(0, 0))
for k in graph:
    print(k)
graph[0][0] = 1
print(bfs2(n-1, m-1))




