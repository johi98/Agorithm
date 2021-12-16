from math import floor

# 끝과 시작을 바꾸고 끝을 제외한 상태로 다시 힙으로 만들어 줌
# 이러면 끝에서 부터 작은 숫자가 옴으로 내림차순이 됩니다.
# 오름차순으로 만들어 주기 위해서 배열을 하나 만들고 빠지는 수를
# 새로 만든 배열에 저장해주어야 할것 같습니다.

def heapSort(array, n):
    buildHeap(array, n)
    for i in range(n-1, -1, -1):
        print(array)
        array[0], array[i] = array[i], array[0]
        heapify(array, 1, i)

    return array


def buildHeap(array, n):
    for i in range(floor(n/2), 0, -1):
        heapify(array, i, n)


def heapify(array, k, n):
    left = 2*k
    right = (2*k)+1
    if right <= n:
        if array[left-1] < array[right-1]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    if array[smaller-1] < array[k-1]:
        array[k-1], array[smaller-1] = array[smaller-1], array[k-1]
        heapify(array, smaller, n)


n = list(map(int,input().split()))
print(n)
print(heapSort(n, len(n)))
