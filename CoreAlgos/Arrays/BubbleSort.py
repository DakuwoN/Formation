def bubbleSort(input):
    length = len(input)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
    return input
