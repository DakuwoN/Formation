def firstKTimes(array, k):
    counts = {}

    for i in range(len(array)):
        new_count = counts.get(array[i], 0) + 1
        if new_count == k:
            return array[i]
        counts[array[i]] = new_count
    return -1
