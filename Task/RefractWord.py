

def polynomial(word: str) -> bool:
    if len(word) == 1:
        return True
    if len(word) == 2:
        return word[0] == word[1]
    return (word[0] == word[-1]) and polynomial(word[1:-1])


if __name__ == "__main__":
    my_word = input("Введите слово: ").upper()
    print(polynomial(my_word))
