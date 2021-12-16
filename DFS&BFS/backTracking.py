n, k = map(int, input().split())

color = [0, 1, 2, 3, 4, 5, 6, 0, 0, 0]

# 3가지 색으로 색칠을 못할 줄 알아 계속 틀렸구나 생각했지만
# 문제를 오래 풀다 보니 이상함을 느껴 실제로 그려보니
# 3가지 색으로도 가능한 트리였습니다....
result = False

tree = [
    []
    , [2, 3, 4, 6]
    , [1, 6, 5]
    , [1, 6]
    , [1, 5, 6]
    , [2, 4, 6]
    , [1, 2, 3, 4, 5]
]


def valid(i, c):
    for j in tree[i]:
        if color[j] == c:
            print(i, " ", j, " ", color[j], " ", c, "안됨")
            return False
        print(i, " ", j, " ", color[j], " ", c, "가능")
    return True


def kColoring(i, c):
    if valid(i, c):
        color[i] = c
        if i == n:
            return True
        else:
            result = False
            d = 1
            while result is False and d <= k:
                result = kColoring(i+1, d)
                d = d + 1

        return result
    else:
        return False


print(kColoring(1, 1))
