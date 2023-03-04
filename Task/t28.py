# Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных исел.Из всех
# арифметических операций допускаются
# только + 1 и - 1. Также нельзя использовать
# циклы.

def refSum(a: int, b: int) -> int:
    if b == 1 and a == 1:
        return 1+1
    elif b == 1:
        return 1 + refSum(a-1, b)
    elif a == 1:
        return 1 + refSum(a, b-1)
    return 1+1 + refSum(a-1, b-1)


if __name__ == "__main__":
    first_number = int(input("Введите 1-ое число: "))
    second_number = int(input("Введите 2-ое число: "))
    print(refSum(a=first_number, b=second_number))
