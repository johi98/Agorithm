

def binarySearch(array, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    print(array[mid], mid)
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binarySearch(array, start, mid-1)
    else:
        return binarySearch(array, mid+1, end)


n = int(input())
array = list(map(int, input().split()))

print(binarySearch(array, 0, n-1))
