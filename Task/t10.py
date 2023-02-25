import random


def fib(n: int) -> int:
    old_n = 0
    new_n = 1
    fib = 0
    for i in range(n-1):
        fib = old_n + new_n
        old_n, new_n = new_n, fib
    return fib


def get_count_flip(count_coins: int) -> tuple:
    count_eagle = int(random.normalvariate(count_coins/2, count_coins/7))
    if count_eagle > 100:
        count_eagle = 100
    elif count_eagle < 0:
        count_eagle = 0
    count_tails = count_coins - count_eagle
    return (count_tails, "решек", "орлом")if count_tails < count_eagle else (count_eagle, "орлов", "решкой")
