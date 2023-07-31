def numDuplicates(array):
    counts = {}
    num_dupes = 0

    for i in range(len(array)):
        new_count = counts.get(array[i], 0) + 1
        if new_count == 2:
            num_dupes += 1
        counts[array[i]] = new_count
    return num_dupes
