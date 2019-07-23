import ast
import json
import nltk
nltk.download()
import string
import pandas as pd

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
lAmeProc = []
lAmePlVid = []

lisBah = []
lBahSisInc = []
lBahProc = []
lBahPlVid = []

lisM = []


while True:
    try:
        x = arq2.readline().rstrip()

        if (x == ''):
            break

        lisAmer.append(data[x]["title"])

        if "Modelo" in data[x]:
            lAmeMod.append(data[x]["Modelo"])
        else:
            lAmeMod.append(" ")

        if "Softwares inclusos" in data[x]:
            lAmeSisInc.append(data[x]["Softwares inclusos"])
        else:
            lAmeSisInc.append(" ")

        if "Processador" in data[x]:
            lAmeProc.append(data[x]["Processador"])
        else:
            lAmeProc.append(" ")

        if "Placa de vídeo" in data[x]:
            lAmePlVid.append(data[x]["Placa de vídeo"])
        else:
            lAmePlVid.append(" ")

        y = arq2.readline().rstrip()
        if (y == ''):
            break
        lisBah.append(data[y]["title"])

        if "Softwares inclusos" in data[y]:
            lBahSisInc.append(data[y]["Softwares inclusos"])
        else:
            lBahSisInc.append(" ")

        if "Processador" in data[y]:
            lBahProc.append(data[y]["Processador"])
        else:
            lBahProc.append(" ")

        if "Placa de vídeo" in data[y]:
            lBahPlVid.append(data[y]["Placa de vídeo"])
        else:
            lBahPlVid.append(" ")


        z = arq2.readline().rstrip()
        if (z == ''):
            break
        lisM.append(int(z))

    except EOFError:
        break

arq2.close()


stopwords_list = nltk.corpus.stopwords.words('portuguese')

def tokenize_words(t):
    return nltk.tokenize.word_tokenize(t)

def remove_stopwords(tokens):
    return [t for t in tokens if t not in stopwords_list]

def remove_punctuation(t):
    return t.translate(str.maketrans('','',string.punctuation))

def word_overlap(t1, t2):
    tokens1 = remove_stopwords(tokenize_words(remove_punctuation(t1)))
    tokens2 = remove_stopwords(tokenize_words(remove_punctuation(t2)))
    matches = [1 for t in tokens1 if t in tokens2]
    return sum(matches) / (len(tokens1) + len(tokens2))


textAme = ""
textBah = ""
lisT = []

for i in range(len(lisAmer)):
    textAme += lisAmer[i] + lAmeMod[i] + lAmeSisInc[i] + lAmeProc[i] + lAmePlVid[i]
    textBah += lisBah[i] + lBahSisInc[i] + lBahProc[i] + lBahPlVid[i]
    token = word_overlap(textAme, textBah)
    lisT.append(token)

data = {"x0_amer":lisAmer, "x1_ameMod": lAmeMod, "x2_ameSoftInc": lAmeSisInc,
        "x3_AmeProc":lAmeProc, "x4_AmePlacVid":lAmePlVid, "x5_bahia":lisBah,
        "x6_bahSoftInc": lBahSisInc, "x7_BahProc":lBahProc, "x8_BahPlacVid": lBahPlVid,
        "x":lisT, "y":lisM
        }
df = pd.DataFrame(data)

#print(df)
