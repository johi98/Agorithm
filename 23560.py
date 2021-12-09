n = int(input())

result = 1
if n == 1:
    result = 1
else:
    for _ in range(n-1):
        result = result * 3

print(result * 2)