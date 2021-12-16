n = int(input())
count = n*2
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

temp1 = []
result1 = []
for i in graph:
    temp1.append(i[0])

temp1 = list(set(temp1))


# b c 조합
def dfs1(arr, k):
    if len(arr) == 2:
        temp2 = list(arr)
        result1.append(temp2)
        return
    for i in range(k, n):
        arr.append([graph[i][1], graph[i][2]])
        dfs1(arr, i+1)
        arr.pop()


dfs1([], 0)


for i in range(len(result1)):
    for j in temp1:
        if result1[i][0][0] > result1[i][1][0]:
            if result1[i][0][1] < result1[i][1][0] or result1[i][1][1] > result1[i][0][0]:
                count -= 1
        else:
            if result1[i][0][1] > result1[i][1][0] or result1[i][1][1] < result1[i][0][0]:
                count -= 1

for i in temp1:
    for j in graph:
        if j[1] <= i <= j[2]:
            count -= 1

print(count)




