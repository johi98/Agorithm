n = int(input())

result = 0;

board = [0] * n


def queen(m):
    global result
    if n == m:
        result += 1

    else:
        for i in range(n):
            board[m] = i
            if check(m):
                queen(m + 1)


def check(m):
    for i in range(m):
        if board[m] == board[i] or abs(board[m] - board[i]) == m - i:
            return False
    return True


queen(0)
print(result)