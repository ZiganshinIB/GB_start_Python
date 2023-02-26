from Task import t20

score_data = {}
t20.dict_scrabble_list_machin(score_data,
                              texts=["AEIOULNSTR", 'DG', 'BCMP', 'FHVWY', 'K', 'JX', 'QZ',
                                     'АВЕИНОРСТ', 'ДКЛМПУ', 'БГЁЬЯ', 'ЙЫ', 'ЖЗХЦЧ', 'ШЭЮ', 'ФЩЪ' ],
                              scores=[1, 2, 3, 4, 5, 8, 10,
                                      1, 2, 3, 4, 5, 8, 10])

print(t20.scrabble_2('ноутбук', score_data))
