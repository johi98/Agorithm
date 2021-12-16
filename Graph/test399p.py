from collections import deque


# 테스트 케이스 반복을 위한 반복문
for _ in range(int(input())):
    n = int(input())
    # 진입차수 초기화
    indegree = [0] * (n+1)
    # 간선 초기화
    graph = [[False] * (n+1) for _ in range(n+1)]
    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            # 간선을 리스트 배열의 True False 로 표시
            graph[data[i]][data[j]] = True
            # 간선이 그려지는 만큼 자식 노드에 진입차수 추가
            indegree[data[j]] += 1

# 변경되는 순위 개수 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향을 변경
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    q = deque()
    result = []

# 시작 노드를 큐에 넣어줌
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    good = True
    cycle = False

    for i in range(n):
# 사이클이 만들어 지는 경우 다음 노드가 오지 않기 때문에 큐 개수가 0이됨
        if len(q) == 0:
            cycle = True
            break
# 큐가 2보다 크다는 것은 진입차수가 같은 노드가 존재하기 때문에 순위를 정할 수 없음
        if len(q) >= 2:
            good = False
            break

# 노드 하나 빼고 하나를 결과에 넣음
        k = q.popleft()
        result.append(k)

# 다음으로 오는 노드를 넣어줌
        for j in range(1, n+1):
            if graph[k][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not good:
        print("?")
    else:
        print(result)





