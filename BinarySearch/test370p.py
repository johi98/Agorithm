from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

array = [[] for _ in range(10)]
reversedArray = [[] for _ in range(10)]


def getResult(words, queries):
    answer=[]
    for word in words:
        array[len(word)].append(word)
        reversedArray[len(word)].append(word[::-1])
    print(array)
    print(reversedArray)
    # 이진탐색은 반드시 정렬된 상태에서 구현됨
    for a in range(10):
        array[a].sort()
        reversedArray[a].sort()
    for q in queries:
        if q[0] != '?':
            p = countWords(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            print(q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            p = countWords(reversedArray[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            print(q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(p)

    return answer


def countWords(a, a_bisect_left, a_bisect_right):
    abl = bisect_left(a, a_bisect_left)
    abr = bisect_right(a, a_bisect_right)

    return abr - abl


print(getResult(words, queries))
