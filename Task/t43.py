# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

def _res(arr: list) -> int:
    counter = 0
    for item in arr:
        counter += (arr.count(item)//2)
    return counter//2


def random_list(N: int, min=-100, max=100) -> list:
    import random
    arr = []
    for i in range(N):
        arr.append(random.randint(min, max))
    return arr


if __name__ == "__main__":
    count = int(input("Введите длину списка: "))
    arr = [3,3,5,5,5,3]
    print(arr)
    print(_res(arr))