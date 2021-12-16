import random

n = int(input())# 인구수
k = list()
count = 0
for i in range(n):
     k.append(random.randrange(1, 4))

k.sort()

print(k)
# 인구수 - 공포도 ? 인구수-공포도 0이상일때 까지
for i in range(n):
    n -= k[i]
    if n - k[i] >= 0:
        count += 1

    else:
        break


print(count)


