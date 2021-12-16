import random
import time

# 문제: 배열의 크기 N , 숫자가 더해지는 횟수 M , 연속된 숫자가 쓰일 수 있는 횟수 K
# N 크기의 배열에서 M, K를 사용해서 만들 수 있는 가장 큰 숫자를 구하시오
# 조건: 2번째 크기의 숫자가 같아도 서로 다른 숫자로 판단한다.

answer = 0
count = 0 # 연속되는 횟수를 알기 위한 count
n, m, k = map(int, input().split())
# n , m ,k 값 받기
data = []
# 랜덤으로 값 생성 이후 배열에 집어넣기
for i in range(n):
    data.append(random.randrange(1, 11))

data.sort(reverse=True)   # 내림차순 정렬
print(data)
# 정렬로 인하여 [0] [1]은 가장 큰 숫자 두개가 됨
big1 = data[0]
big2 = data[1]

start_t = time.time()
# k번 연속으로 덧셈이후 두번째 큰수를 더하는 코드
for i in range(m):
    if count < k:
        answer += big1
        count += 1
        # print(str(big1)+" :" + str(i))
    else:
        answer += big2
        count = 0
        # print(str(big2) + " :" + str(i))
# 답
print(answer)

end_t = time.time()

print(end_t - start_t)
