from functools import reduce



def count_vowels(word):
    list_vowels_char_ru = list('АаУуеЕЫыОоЭэЯяИиЮю')
    return len(list(filter(lambda char: char in list_vowels_char_ru, word)))


def is_text(text:str):
    list_count_words = list(map(lambda word: count_vowels(word),text.split()))
    return all(i == list_count_words[0] for i in list_count_words)


if __name__ == "__main__":
    my_text = "пара-ра-рам рам-пам-папам па-ра-па-да"
    print("Парам пам-пам" if is_text(my_text) else "Пам парам")