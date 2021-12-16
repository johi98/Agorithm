n = int(input())
soldier = list(map(int, input().split()))

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if soldier[j] > soldier[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))

