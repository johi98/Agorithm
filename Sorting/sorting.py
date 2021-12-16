n = int(input())

array = []

for i in range(n):
    array.append(int(input()))


def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)


def partition(array, p, r):
    pivot = p
    left = p + 1
    right = r
    while left <= right:
        # 순서 매우중요 마지막 루프에서 left 는 array 길이를 초과하기 때문에
        # left <= r 를 먼저 검사하지 않으면 array[left] 오류
        while left <= r and array[pivot] >= array[left]:
            left += 1
        while right > p and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]

    return right


print(quickSort(array, 0, len(array)-1))
print(array)
