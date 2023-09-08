def fib(k):
    if k <= 1:
        return 1
    prev = curr = 1
    for i in range(2, k+1):
        prev, curr = curr, prev + curr
    return curr
