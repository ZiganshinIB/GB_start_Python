# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def sum_three(number: int)-> int:
    if 999 >= number >= 100:
        n1 = number % 10
        n2 = (number//10) % 10
        n3 = (number//100) % 10
        return n1+n2 + n3
    else:
        print("Число не 3 значная либо она отрицательная")
        return -1