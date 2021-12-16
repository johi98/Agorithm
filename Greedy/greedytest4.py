n = list(map(int, input().split()))
n.sort()

target = 1

for i in n:
    if target < i:
        break
    target += i

print(target)