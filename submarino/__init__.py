#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Suggest use to execute this file command line : python2 __init__.py
#Or execute normal switch function dump to dumps

from b2w import B2W
import json

codes = B2W.Get_Prod_Codes_By_Cat("https://www.submarino.com.br/categoria/informatica/notebook", 1000)
prods = B2W.Get_Properties_By_Cods(codes)

file = open("products_sub.txt", "w")


for i in prods :
    json.dump(i, file, ensure_ascii=False, indent=4)
    file.write("\n\n")

file.close()
