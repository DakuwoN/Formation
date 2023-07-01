def selectionSort(input):
    for i in range(len(input) - 1):
        min_index = i
        for j in range(i+1, len(input)):
            if input[j] < input[min_index]:
                min_index = j
        input[min_index], input[i] = input[i], input[min_index]
    return input
