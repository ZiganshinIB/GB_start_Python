

def fib(n: int) -> int:
    old_n = 0
    new_n = 1
    fib = 0
    for i in range(n-1):
        fib = old_n + new_n
        old_n, new_n = new_n, fib
    return fib

