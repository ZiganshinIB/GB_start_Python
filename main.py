# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# from Task import t10
# # number = int (input ("Введите число - > "))
# # n = 1
# # while (number > 0):
# #     n *= number
# #     number -= 1
# # print(n)
#
#
#
# number = int (input ("натуральное число A > 1 - > "))
#
# flag = True
# i = 1
# while(flag):
#     temp = t10.fib(i)
#     if temp < number:
#         i+=1
#     elif temp == number:
#         print(i)
#         flag = False
#     else:
#         print(-1)
#         flag = False

# import random
#
# n = int(input("общее количество рассматриваемых дней (1 ≤ N ≤ 100)"))
# count = 0
# day_max = 0
# for i in range(n):
#     t = random.randint(-50, 50)
#     if t>0:
#         count += 1
#     else:
#         if day_max < count:
#             day_max = count
#         count = 0
# if day_max < count:
#     day_max = count
# print(day_max)


n = int(input("общее количество рассматриваемых дней (1 ≤ N ≤ 100)"))
p = 1
for i in range(n):
    print(f"{p}", end='  ')
    p *= -3
