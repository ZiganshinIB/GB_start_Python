# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество
# элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N
# — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

def _res(arr: list):
    counter = 0
    for index in range(len(arr)):
        if arr[index-1] < arr[index] > arr[(index+1)%(len(arr))]:
            counter += 1
    return counter


def random_list(N: int, min=-100, max=100) -> list:
    import random
    arr = []
    for i in range(N):
        arr.append(random.randint(min, max))
    return arr


if __name__ == "__main__":
    count = int(input("Введите длину 1 списка: "))
    arr = random_list(count,)
    print(arr)
    print(_res(arr))