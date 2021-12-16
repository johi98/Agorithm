import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
INF = 9999
distance = [INF] * (n + 1)
count = 0
# 비용은 모두 같음으로 1로 고정
# 양방향임으로 양쪽에 넣어준다
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])
    graph[b].append([a, 1])


# 다익스트라 알고리즘
def dijkstra(start):
    global count
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        count += 1
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드를 확인한다
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)

maxNode = 0
maxDistance = 0
sameNode = 0

result = []
for i in range(1, len(distance)):
    if maxDistance < distance[i]:
        maxNode = i
        maxDistance = distance[i]
        sameNode = 1
    elif maxDistance == distance[i]:
        sameNode += 1

print(count)
print(distance)
print(maxNode, maxDistance, sameNode)