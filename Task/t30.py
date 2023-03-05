# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
from typing import Union


# a1 = - and
def arr_arithmetic_progression(start: Union[int, float], step: Union[int, float], count: int) -> list:
    return [start+i*step for i in range(count)]


if __name__ == "__main__":
    assert arr_arithmetic_progression(7, 2, 5) == [7, 9, 11, 13, 15]
    print(arr_arithmetic_progression(7, 2, 5))
