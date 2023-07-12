def mergeSort(array):
    if len(array) <= 1:
        return array

    half = len(array) // 2
    left = array[:half]
    right = array[half:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(array1, array2):
    result = []
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    if j == len(array2):
        result += array1[i:]
    else:
        result += array2[j:]
    return result
