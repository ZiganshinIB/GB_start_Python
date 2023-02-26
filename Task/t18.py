import random


def generator_random_list(count: int) -> list:
    return [random.randint(1, count) for _ in range(count)]


def find_all_nearby(array: list, value: int) -> dict:
    """
    Hello world ☻
    :param array: List
    :param value:  Find value
    :return: {index: item}
    """
    nearby: dict = {}
    sub_arr: list = [abs(item - value) for item in array]
    min_len = min(sub_arr)
    for index in range(len(sub_arr)):
        if min_len == sub_arr[index]:
            nearby[index] = array[index]
    return nearby


if __name__ == "__main__":
    n: int = int(input("Введите натуральное число N – количество элементов в массиве: "))
    arr: list = generator_random_list(count=n)
    print(arr)
    x = int(input("x: "))
    print(find_all_nearby(arr, x))

