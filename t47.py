# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.

def get_line_list(d,):
    res = []
    for i in d:
        if type(i) == list:
            res += get_line_list(i)
        else:
            res.append(i)
    return res

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
print(get_line_list(d))