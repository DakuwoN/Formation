def numUniqueValues(array):
    counts = {}
    num_unique = 0

    for i in range(len(input)):
        new_count = counts.get(array[i], 0) + 1
        if new_count == 1:
            num_unique += 1
        if new_count == 2:
            num_unique -= 1
        counts[array[i]] = new_acount
    return num_unique
