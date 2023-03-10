# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).


def print_res(k):
    for i in range(2, k-1):
        s = sum(get_divs(i))
        if i == sum(get_divs(s)):
            print(i, s)



def get_divs(number) -> list:
    return [index for index in range(1, number) if (number % index) == 0]


if __name__ == "__main__":
    k = int(input("Введите k: "))
    print_res(300)

