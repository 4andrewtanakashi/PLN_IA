#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

from fileApp import Get

def main() :
    url = "https://www.casasbahia.com.br/c/tablets/tablet/?filtro=c2031_c2032"
    g = Get()
    soup = g.__iniciador__(url)
    prods = g.__PropriedadesCod__(soup, 3)

    file = open("products_bahia_tablet.txt", "w")

    for i in prods:
        json.dump(i, file, ensure_ascii=False, indent=4)
        file.write("\n\n")

    file.close()

    for i in prods:
        print(i)
        print("\n\n")

if __name__ == "__main__":
    main()

# print("\n \n")

# #Pega o link da proxima página
# encontrou = False
# link = str()
# point = ''
# compare = "<li class="+"\""+"atual"+ "\""+"><strong>"
# for ul in soup.findAll('ul', {'class':'ListaPaginas'}):
#     for li in ul.find_all('li'):

#         # Se a string compare está contida em str(li)
#         if ( compare in str(li) ):
#             point = 'Ready'
#             print("here")
#         if (li.find('a') and ((encontrou == False) and (point =='Ready')) ):
#                 encontrou = True
#                 a = li.find('a')
#                 link = str(a.attrs['href'])
