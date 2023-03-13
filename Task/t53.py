# Напишите функцию same_by
# (characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой
# характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то
# False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

from functools import reduce
def same_by(characteristic, objects):
    reduce(lambda a,b: characteristic(a)==characteristic(b), objects)

# def random_list_words():
#     list_words = []
#     for i in range(100):
#         for _ in range(random.randint(1,len(words))):



if __name__ == "__main__":
    my_list_words = ['Hello', 'Cat fdad dfa ', "Car", "World", "Word", "Bye"]
    print(get_one_word(my_list_words))