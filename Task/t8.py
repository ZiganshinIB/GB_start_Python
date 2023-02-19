# Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками(то есть разломить шоколадку на
# два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

def can_chocolate_slices(col: int, row: int, pieces: int) -> bool:
    square = col * row
    if pieces <= square:
        return ((pieces % col) == 0) or ((pieces % row) == 0)
    else:
        print("Купите еще шоколада по акции у нас https://github.com/ZiganshinIB/GB_start_Python.git")
        return False


