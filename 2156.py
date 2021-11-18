n = int(input())

array = [0]
result = 0
dp = [0] * (n + 1)

for _ in range(n):
    array.append(int(input()))

dp[1] = array[1]
if n > 1:
    dp[2] = array[1] + array[2]
if n > 2:
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + array[i-1] + array[i], dp[i-2] + array[i])
        dp[i] = max(dp[i], dp[i-1])

print(max(dp))
