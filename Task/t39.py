# 39. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел
# - элементы массива. Затем число M - количество элементов во втором массиве. Затем
# элементы второго массива


def print_res(arr_1: list, arr_2: list):
    for item in arr_1:
        if not (item in arr_2):
            print(item, end=', ')


def random_list(N:int, min=-100, max=100) -> list:
    import random
    arr = []
    for i in range(N):
        arr.append(random.randint(min, max))
    return arr


if __name__ == "__main__":
    count_1 = int(input("Введите длину 1 списка: "))
    count_2 = int(input("Введите длину 2 списка: "))
    arr_1 = random_list(count_1)
    print(arr_1)
    arr_2 = random_list(count_2)
    print(arr_2)
    print_res(arr_1, arr_2)




