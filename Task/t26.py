# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
from typing import Union


def refPow(number: Union[int, float], a: int) -> Union[int, float]:
    if a == 1:
        return number
    return number * refPow(number, a-1)


if __name__ == "__main__":
    my_number = int(input("Введите число: "))
    my_a = int(input("Введите степен: "))
    print(refPow(number=my_number, a=my_a))
