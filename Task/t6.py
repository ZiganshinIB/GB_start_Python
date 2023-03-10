# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

def is_lucky_number(number: str) -> bool:
    if number.isdigit():
        if len(number) == 6:
            left_sum = sum([int(x) for x in number[:3]])
            right_sum = sum([int(x) for x in number[3:]])
            return left_sum == right_sum
        else:
            print("Ошибка: не ожидал 6 значное число")
    else:
        print("Ошибка: не ожидал число, но у вас есть символы")