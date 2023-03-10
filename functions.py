# english
A = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"] # 1 очка
D = ["D", "G"] # 2 очка
B = ["B", "C", "M", "P"] # 3 очка
F = ["F", "H", "V", "W", "Y"] # 4 очка
K = ["K",] # 5 очков
J = ["J", "X"] # 8 очков
Q = ["Q", "Z"] # 10 очков
listEn = [[A,1],[D,2],[B,3],[F,4],[K,5],[J,8],[Q,10]]
# russia
ruA = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"] # 1 очка
ruD = ["Д", "К", "Л", "М", "П", "У"] # 2 очка
ruB = ["Б", "Г", "Ё", "Ь", "Я"] # 3 очка
ruI = ["Й", "Ы"] # 4 очка
ruJ = ["Ж", "З", "Х", "Ц", "Ч"] # 5 очков
ruSh = ["Ш", "Э", "Ю"] # 8 очков
ruF = ["Ф", "Щ", "Ъ"] # 10 очков
listRu = [[ruA,1],[ruD,2],[ruB,3],[ruI,4],[ruJ,5],[ruSh,8],[ruF,10]]

# заполним словарь
def Fill(dict,list,balls):
    for a in list:
        dict[a] = balls
        
# подсчет стоимости
def PayWord(dict, word):
    pay = 0
    for w in word:
        if w.upper() in dict:
            pay+= int(dict.get(w.upper()))
    return pay