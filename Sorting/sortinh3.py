n = int(input())

array1 = []

for i in range(n):
    array1.append(int(input()))


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = []
    right = []

    for i in range(1, len(array)):
        if array[i] >= pivot:
            left.append(array[i])
        elif array[i] < pivot:
            right.append(array[i])

    return quick_sort(left) + pivot + quick_sort(right)


print(quick_sort(array1))
