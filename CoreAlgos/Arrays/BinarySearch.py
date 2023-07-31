def binarySearch(array, target):
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False
