n, m = map(int, input().split())
board = list(map(int, input().split()))
dp = []
for i in board:
    dp.append(abs(i))

dp = list(set(dp))

for _ in range(m-1):
    for i in range(len(dp)):
        for j in range(len(board)):
            dp.append(dp[i] ^ board[j])
    dp = list(set(dp))

print(max(dp))
