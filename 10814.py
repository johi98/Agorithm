n = int(input())

board = []

for i in range(n):
    a, b = input().split()
    board.append(list([int(a), b]))

board = sorted(board, key=lambda board:board[0])

for i in range(n):
    print(board[i][0], board[i][1])
