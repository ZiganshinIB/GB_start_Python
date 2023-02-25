from Task import t10
import random
# task #10
# def get_count_flip(count_coins: int) -> tuple:
#     count_eagle = int(random.normalvariate(count_coins/2, count_coins/7))
#     if count_eagle > 100:
#         count_eagle = 100
#     elif count_eagle < 0:
#         count_eagle = 0
#     count_tails = count_coins - count_eagle
#     return (count_tails, "решки")if count_tails < count_eagle else (count_eagle, "орлы")

n = int(input("Сколько На столе лежат монеток: "))
count, side, side_2 = t10.get_count_flip(count_coins=n)
print(f"Минимальное {count} монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх {side_2} стороной.")

# ------------------------------------ #

number_1 = random.randint(1, 1000)
number_2 = random.randint(1, 1000)
S = number_1 + number_2
P = number_1 * number_2
print(f"Сумма: {S} Произведение: {P}")
# Формула ментальной связи
X1 = int((S + (S**2-4*P)**0.5)/2)
X2 = int((S - (S**2-4*P)**0.5)/2)
#
print(f"Наш результат ({X1}, {X2}), задумал ({number_1}, {number_2})")
