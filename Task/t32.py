# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

def get_indexes_range(array: list, min_value=7, max_value=10):
    return [index for index in range(len(array)) if min_value <= array[index] <= max_value]


def random_list(N:int, min=-100, max=100) -> list:
    import random
    arr = []
    for i in range(N):
        arr.append(random.randint(min, max))
    return arr


if __name__ == "__main__":
    arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    assert get_indexes_range(arr) == [1, 9, 13, 14, 19]
    print(get_indexes_range(arr))