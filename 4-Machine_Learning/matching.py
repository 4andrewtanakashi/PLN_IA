import ast
import json
import nltk
nltk.download()
import string
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

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

data = {"x0_amer":lisAmer, "x1_ameMod": lAmeMod, "x2_ameSoftInc": lAmeSisInc, "x3_AmeProc":lAmeProc, "x4_AmePlacVid":lAmePlVid, 
        "x5_bahia":lisBah, "x6_bahSoftInc": lBahSisInc, "x7_BahProc":lBahProc, "x8_BahPlacVid": lBahPlVid,
        "x":lisT, "y":lisM
        }
df = pd.DataFrame(data)

data1 = {"x0_amer":lisAmer, "x1_ameMod": lAmeMod, "x2_ameSoftInc": lAmeSisInc, "x3_AmeProc":lAmeProc, "x4_AmePlacVid":lAmePlVid, 
        "x5_bahia":lisBah, "x6_bahSoftInc": lBahSisInc, "x7_BahProc":lBahProc, "x8_BahPlacVid": lBahPlVid,
        }
df1 = pd.DataFrame(data1)

dictToken = dict()
index = 0
for lista in df1.values:
    vectorizer = CountVectorizer()
    vectorizer.fit(lista)
    vectorz = vectorizer.transform(lista)
    vectToken = list()
    for elem in vectorz.toarray() :
        value = ""
        for i in range(len(elem)):
            value += str(elem[i])
        vectToken.append(int(value))
    dictToken[str(index)] = vectToken
    index += 1

dfToken = pd.DataFrame(dictToken).T

X = dfToken.values
Y = df["y"].values

from sklearn.model_selection import train_test_split
X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

LR = LogisticRegression()
SVM = SVC()
DT = DecisionTreeClassifier()
RF = RandomForestClassifier()
MLP = MLPClassifier()

print("LogisticRegression")
LR.fit(X_train, Y_train)
print("SupportVectorMachines")
SVM.fit(X_train, Y_train)
print("DecisionTreeClassifier")
DT.fit(X_train, Y_train)
print("RandomForestClassifier")
RF.fit(X_train, Y_train)
print("MultLayerPerceptron")
MLP.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score

print("LogisticRegression")
print(accuracy_score(y_test, LR.predict(x_test)))
print("SupportVectorMachines")
print(accuracy_score(y_test, SVM.predict(x_test)))
print("DecisionTreeClassifier")
print(accuracy_score(y_test, DT.predict(x_test)))
print("RandomForestClassifier")
print(accuracy_score(y_test, RF.predict(x_test)))
print("MultLayerPerceptron")
print(accuracy_score(y_test, MLP.predict(x_test)))

#print(df)
