n = int(input())

graph = []

for i in range(n):
    graph.append(map(int, input().split()))

graph.sort()

print(graph[(n-1)//2])