import os
import functions as f
os.system('cls')
# create to dictonary
dictEn = {}
dictRu = {}

for l in f.listEn:
    f.Fill(dictEn, l[0], l[1])
print(dictEn)
#
for l in f.listRu:
    f.Fill(dictRu,l[0],l[1])
print(dictRu)
# 