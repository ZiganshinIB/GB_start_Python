import random
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