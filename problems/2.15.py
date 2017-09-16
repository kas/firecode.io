# 2.15 Better Fibonacci

def better_fibonacci(n):
    if n < 2:
        return n

    i = 1
    second_to_last = 0
    last = 1
    current = None

    while i < n:
        current = second_to_last + last
        second_to_last = last
        last = current

        i += 1

    return current

