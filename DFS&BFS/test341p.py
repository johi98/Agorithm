n, m = map(int, input())

graph = []
tempG = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
count22 = 0


# 바이러스 퍼트리기
def infection(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tempG[nx][ny] == 0:
                tempG[nx][ny] = 2
                infection(nx, ny)


# 벽세우기
def setWall(count):
    global result
    global count22
    count22 += 1
    if count == 3:
        for i in range(n):
            for j in range(m):
                tempG[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if tempG[i][j] == 2:
                    infection(i, j)

        result = max(result, getScore())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                setWall(count)
                graph[i][j] = 0
                count -= 1


# 빈칸 반환
def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if tempG[i][j] == 0:
                score += 1

    return score


setWall(0)
print(count22)
print(result)
