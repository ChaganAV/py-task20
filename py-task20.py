# create to dictonary
dictEn = {}
dictRu = {}
def Fill(dict,list,balls):
    for a in list:
        dict[a] = balls
# englange
A = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"] # 1 очка
D = ["D", "G"] # 2 очка
B = ["B", "C", "M", "P"] # 3 очка
F = ["F", "H", "V", "W", "Y"] # 4 очка
K = ["K",] # 5 очков
J = ["J", "X"] # 8 очков
Q = ["Q", "Z"] # 10 очков
# russia
ruA = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"] # 1 очка
ruD = ["Д", "К", "Л", "М", "П", "У"] # 2 очка
ruB = ["Б", "Г", "Ё", "Ь", "Я"] # 3 очка
ruI = ["Й", "Ы"] # 4 очка
ruJ = ["Ж", "З", "Х", "Ц", "Ч"] # 5 очков
ruSh = ["Ш", "Э", "Ю"] # 8 очков
ruF = ["Ф", "Щ", "Ъ"] # 10 очков
dRu = [[ruA,1],[ruD,2],[ruB,3],[ruI,4],[ruJ,5],[ruSh,8],[ruF,10]]
Fill(dictEn,A,1)
Fill(dictEn,D,2)
Fill(dictEn,B,3)
Fill(dictEn,F,4)
Fill(dictEn,K,5)
Fill(dictEn,J,8)
Fill(dictEn,Q,10)
# print(dictEn)
#
for r in dRu:
    Fill(dictRu,r[0],r[1])
    # print(r[0])
    # for item in r:
    #     print(item[0][0])
# Fill(dictRu,ruA,1)
# Fill(dictRu,ruD,2)
# Fill(dictRu,ruB,3)
# Fill(dictRu,ruI,4)
# Fill(dictRu,ruJ,5)
# Fill(dictRu,ruSh,8)
# Fill(dictRu,ruF,10)
print(dictRu)