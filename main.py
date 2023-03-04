from Task import t20

# 1. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.
#
# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# def rec(N:int):
#      i = input()
#      if N == 1:
#          return i
#      return rec(N-1) + " " + i
# #
# # print(rec(4))
#
# # Написать функцию для нахождения наибольшего общего делителя двух чисел:
#
# def nod(a, b):
#     if a<b:
#         a, b = b, a
#     if a%b == 0:
#         return b
#     return nod(b, a%b)
# print(nod(18, 30))
#
#
# def sum_number(n):
#     if (n // 10) == 0:
#         return n % 10
#     return sum_number(n//10) + n % 10 #
#
# print(sum_number(2))
#
# a = int(input("Введите число A: "))
# b = int(input("Введите число B: "))
#
#
# def nod(x, y):
#     if not(x != 0 and y != 0):
#         #print(x + y)
#         return x
#     else:
#         if x > y:
#             return nod(x % y, y)
#         else:
#             return nod(x, y % x)
#
# print(nod(a,b))


# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

def fib(n, fib_d={0: 0, 1: 1}):
    if n in fib_d:
        return fib_d[n]
    else:
        fib_d[n] = fib(n-1, fib_d) + fib_d[(n-2)]
        return fib_d[n]


print(fib(100), )


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

scores = [5, 5, 3, 5, 2, 2, 2, 2]


# Написать функцию для проверки, является ли слово палиндромом
word = "воров"
print(all([word[i] == word[len(word)-1 - i] for i in range(len(word))]))

