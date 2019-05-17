#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

from fileApp import Get

url = "https://www.casasbahia.com.br/c/informatica/notebook/?filtro=c56_c57"

#file = open("products.txt", "w")


#for i in prods :
#    json.dump(i, file, ensure_ascii=False, indent=4)
#    file.write("\n\n")

#file.close()

#print(prods)

#For don't turn loop infinite:

try:
    conteudo = requests.get(url, timeout = 5)
    if conteudo.status_code == 200:
        soup = BeautifulSoup(conteudo.text)

        res = soup.findAll('a')
        i = 0
        while i < 10:
            # pull = link.get('href')
            # pull = Get.informacoes(pull)
            # print(pull)
            # print("\n \n")
            print(res[i])
            i += 1
except requests.Timeout as e:
    print("tempo excedido")
    print(str(e))