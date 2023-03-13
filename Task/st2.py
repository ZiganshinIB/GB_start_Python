# Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по
# диагонали от верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы
# чисел как показано в примере ниже.
#
#
# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
def get_matrix(n):
    return [[int(i==j) for i in range(n)] for j in range(n)]


if __name__ == "__main__":
    print(*get_matrix(4), sep='\n')
    N = int(input())
    lst = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    for r in lst:
        print(*r)