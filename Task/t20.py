
def dict_scrabble_machin(data: dict, text: str = " ", score: int = 0) -> dict:
    for c in list(text):
        data[c] = score
    return data


def dict_scrabble_list_machin(data: dict, texts: list, scores: list) -> dict:
    for key, value in zip(texts, scores):
        dict_scrabble_machin(data, key, value)
    return data


def scrabble_1(text: str, score_data: dict) -> int:
    score = 0
    for c in list(text):
        for k in score_data:
            if c in k:
                score += score_data[k]
    return score


def scrabble_2(text: str, score_data: dict) -> int:
    score = 0
    for c in list(text.upper()):
        score += score_data[c]
    return score
