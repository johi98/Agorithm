n, m = map(int, input().split())

ballWeights = list(map(int, input().split()))

ballCount = [0] * 11
result = 0

for i in ballWeights:
    ballCount[i] += 1

# 자신의 무개를 제외하고 나머지 무개를 가진 공의 개수 * 자신의 공 개수
for i in range(1, m+1):
    n -= ballCount[i]
    result += ballCount[i] * n

print(result)