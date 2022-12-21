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

Fill(dictEn,A,1)
Fill(dictEn,D,2)
print(dictEn)