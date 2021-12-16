n, m = map(int, input().split())

graph = list(map(int, input().split()))
result = []


# 조합
def dfs(arr, k):
    if len(arr) == m:
        temp = list(arr)
        result.append(temp)
        return
    for i in range(k, n):
        arr.append(graph[i])
        dfs(arr, i)
        arr.pop()


dfs([], 0)
print(result)