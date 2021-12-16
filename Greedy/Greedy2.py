import random
import time

answer = 0
count = 0
n, m, k = map(int, input().split())
# n , m ,k 값 받기
data = []
# 랜덤으로 값 생성 이후 배열에 집어넣기
for i in range(n):
    data.append(random.randrange(1, 11))

# 내림차순 정렬
data.sort(reverse=True)
print(data)

# 정렬로 인하여 [0] [1]은 가장 큰 숫자 두개가 됨
big1 = data[0]
big2 = data[1]

# big1 * k +  big2 + ...이 배열처럼 반복됨으로 공식으로 계산

start_t = time.time()
# 배열에서 반복되는 big1의 수 = 반복횟수 / (연속횟수 + 1)
count = m//(k+1) * k
# 나머지 big1의 수 반복횟수
count += m % (k + 1)
answer += count * big1
answer += (m-count) * big2

print(answer)

end_t = time.time()

print(end_t - start_t )
