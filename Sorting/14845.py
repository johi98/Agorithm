n, m = map(int, input().split())
graph = list(map(int, input().split()))
save = []
magic = []
for i in range(m):
    magic.append(list(map(int, input().split())))

for i in range(m):
    # 오름차순
    if magic[i][0] < magic[i][1]:
        graph[(magic[i][0]-1):magic[i][1]] = sorted(graph[(magic[i][0]-1):magic[i][1]])
    else:
        graph[(magic[i][1]-1):magic[i][0]] = sorted(graph[(magic[i][1]-1):magic[i][0]], reverse=True)

print(graph[int(((n+1)/2)-1)])
