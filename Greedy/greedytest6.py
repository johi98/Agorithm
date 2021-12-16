# 풀이 방법
# 배열의 최소화 이후
# 네트워크 지연까지 남은 시간 % 배열의 길이 +1
# = 정답

# 음식마다 걸리는 시간을 받는다
food_times = list(map(int, input().split()))
k = int(input())
result = 0
# k가 음식을 다 먹는 시간보다 크거나 같을 경우 -1을 반환한다.
if sum(food_times) <= k:
    result = -1
length = len(food_times)
# 음식을 다 먹는데 걸리는 시간
food_count = k

q = []

for i in range(length):
    q.append([food_times[i], i+1])

p = q.copy()

# 최소값 배열 * 배열의 길이
while min(q)[0] * len(q) <= food_count:
    q.sort()
    print(q)
    food_count = food_count - (q[0][0] * len(q))
    p.remove(q[0])
    del q[0]

result = p[(food_count % len(q))]

print(q)
print(p)
print(food_count)
print(result, "번째 음식")
