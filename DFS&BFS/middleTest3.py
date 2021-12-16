n, m = map(int, input().split())
graph = list(map(int, input().split()))
result = []
visited = [0] * n

# 순열
def dfs(arr):
    if len(arr) == m:
        temp = list(arr)
        result.append(temp)
        return

    for i in range(n):
        #if visited[i] == 1:
         #   continue
        arr.append(graph[i])
        #visited[i] = 1
        dfs(arr)
        #visited[i] = 0
        arr.pop()
dfs([])
print(result)