n = int(input())

array1 = []

for i in range(n):
    array1.append(int(input()))


def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x >= pivot]
    right = [x for x in tail if x < pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(array1))
print(sorted(array1))
print(sorted(array1, reverse=True))

