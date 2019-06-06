import ast
import json
import pandas as pd
# reescrever o arquivo
# lista = [[("americanas_87", "bahia_79"),1],
# [("americanas_87","bahia_19"),1],
# [("americanas_34","bahia_69"),1],
# [("americanas_38","bahia_69"),0],
# [("americanas_5", "bahia_97"),0],
# [("americanas_37","bahia_97"),0],
# [("americanas_29","bahia_74"),0],
# [("americanas_37","bahia_74"),0],
# [("americanas_67","bahia_83"),1],
# [("americanas_44","bahia_84"),1],
# [("americanas_79","bahia_93"),1],
# [("americanas_23","bahia_8"),0],
# [("americanas_23","bahia_78"),0],
# [("americanas_10","bahia_12"),1],
# [("americanas_26","bahia_68"),1],
# [("americanas_7", "bahia_100"),1],
# [("americanas_25","bahia_35"),1],
# [("americanas_45","bahia_30"),1],
# [("americanas_99","bahia_98"),0],
# [("americanas_99","bahia_100"),0],
# [("americanas_11","bahia_29"),1],
# [("americanas_84","bahia_99"),1],
# [("americanas_0","americanas_0"),1],
# [("bahia_2","bahia_2"),1],
# [("bahia_2","bahia_2"),1],
# [("bahia_23", "americanas_12"),1],
# [("americanas_34", "bahia_69"),0],
# [("americanas_38", "americanas_34"), 0],
# [("americanas_73", "bahia_71"), 1],
# [("bahia_73", "bahia_76"), 1],
# [("americanas_80", "americanas_81"), 0],
# [("bahia_89", "americanas_85"), 1],
# [("americanas_54", "bahia_37"), 1],
# [("bahia_99", "bahia_37"), 0],
# [("bahia_55", "americanas_54"), 0],
# [("americanas_82", "bahia_101"), 0],
# [("submarino_0", "bahia_101"), 0],
# [("bahia_66", "submarino_1"), 0],
# [("americanas_41", "submarino_2"), 0]]

with open('matching', 'r') as f:
    lista = ast.literal_eval(f.read())

arq = open("matching2.txt", "w")
for i in lista:
    for j in i:
        if (j != 0 and j != 1):
            arq.write(str(j[0]) + "\n")
            arq.write(str(j[1]) + "\n")
        else:
            arq.write(str(j) + "\n")

arq.close()

with open("product.json") as file:
    data = json.load(file)


# ler o arquivo reescrito
# formatacao melhorada
arq2 = open("matching2.txt", "r")
lisAmer = []
lAmeMod = []
lAmeSisInc = []

lisBah = []
lBahSisInc = []

lisM = []


while True:
    try:
        x = arq2.readline().rstrip()

        if (x == ''):
            break
#        print(x)
        lisAmer.append(data[x]["title"])

        if "Modelo" in x:
            lAmeMod.append(data[x]["Modelo"])
        else:
            lAmeMod.append(" ")

        if "Softwares inclusos" in x:
            lAmeSisInc.append(data[x]["Softwares inclusos"])
        else:
            lAmeSisInc.append(" ")

        y = arq2.readline().rstrip()
        if (y == ''):
            break
        lisBah.append(data[y]["title"])
#        print(y)
        if "Softwares inclusos" in y:
            lBahSisInc.append(data[y]["Softwares inclusos"])
        else:
            lBahSisInc.append(" ")



        z = arq2.readline().rstrip()
        if (z == ''):
            break
        lisM.append(int(z))
        #else:
            
#       print(z)
#        lista.append([(x, y), z])
    except EOFError:
        break
#print(lista)
arq2.close()

data = {"x0_amer":lisAmer, "x1_ameMod": lAmeMod, "x2_ameSoftInc": lAmeSisInc, "x3_bahia":lisBah, "x4_bahSoftInc": lBahSisInc, "y":lisM}
df = pd.DataFrame(data)

print(df)
