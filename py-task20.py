import os
import functions as f
os.system('cls')
# create to dictonary
dictEn = {}
dictRu = {}
try:
    # заполняем словари алфавитов
    for l in f.listEn:
        f.Fill(dictEn, l[0], l[1])
    # print(dictEn)
    #
    for l in f.listRu:
        f.Fill(dictRu,l[0],l[1])
    # print(dictRu)
    # объединим словари для удобства поиска
    dicts = {**dictEn,**dictRu}
    print(dicts)
    # определим слово
    # word = "Привет"
    word = input("Введите слово: ")
    payBalls = f.PayWord(dicts,word)
    count = 0
    for w in word.split():
        count+= 1
    if count>1:
        print(f'Ваше фраза "{word}" стоит {payBalls} очков')
    else:
        print(f'Ваше слово "{word}" стоит {payBalls} очков')
except:
    print("Что-то пошло не так :(")