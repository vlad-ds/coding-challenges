def factorial1(n):
    result = 1
    while n:
        result *= n
        n -= 1
    return result

def factorial2(n):
    if n == 1:
        return 1
    return n * factorial2(n-1)

assert factorial1(4) == 24
assert factorial2(4) == 24