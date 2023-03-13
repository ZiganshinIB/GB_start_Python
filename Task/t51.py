import random
words = ['Hello', 'Cat', "Car", "World", "Word", "Bye"]

def get_one_word(list_words):
    return list(filter(lambda word: len(word.split()) == 1, list_words))

# def random_list_words():
#     list_words = []
#     for i in range(100):
#         for _ in range(random.randint(1,len(words))):



if __name__ == "__main__":
    my_list_words = ['Hello', 'Cat fdad dfa ', "Car", "World", "Word", "Bye"]
    print(get_one_word(my_list_words))