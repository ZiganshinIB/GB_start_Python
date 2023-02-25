# 1. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями
# статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная
# оттепель. Оттепелью они называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам
# в работе.
import random

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
#
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

n = int(input("общее количество рассматриваемых дней (1 ≤ N ≤ 100)"))
count = 0
day_max = 0
for i in range(n):
    t = random.randint(-50, 50)
    if t>0:
        count += 1
    else:
        if day_max < count:
            day_max = count
        count = 0
if day_max < count:
    day_max = count
print(day_max)