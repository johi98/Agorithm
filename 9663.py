n = int(input())

result = 0;

board = [0] * n
# 퀸이 놓이는 위치는 만약 board[1, 0, 0, 0] 일경우
# 1번째 행의 2번째 열
# 가능한 이유는 퀸은 일렬로 같이 놓일 수 없기 때문에
# 한 행에 하나의 퀸이 존재
# 퀸을 기준으로 행의 차이와 열의 차이가 같다면 위치는 대각선의 존재한다.

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