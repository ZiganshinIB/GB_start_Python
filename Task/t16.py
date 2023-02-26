import random


def generator_random_list(count: int) -> list:
    return [random.randint(1, count) for _ in range(count)]


if __name__ == "__main__":
    n: int = int(input("Введите натуральное число N – количество элементов в массиве: "))
    arr: list = generator_random_list(count=n)
    # print(arr)
    print(arr.count(int(input("x: "))))

