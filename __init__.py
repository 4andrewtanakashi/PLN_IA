#!/usr/bin/python3
# -*- coding: utf-8 -*-

from b2w import B2W
import json

codes = B2W.Get_Prod_Codes_By_Cat("https://www.americanas.com.br/categoria/informatica/notebook", 40)
prods = B2W.Get_Properties_By_Cods(codes)

file = open("products.txt", "w")


for i in prods :
    json.dump(i, file, ensure_ascii=False, indent=4)
    file.write("\n\n")

file.close()

print(prods)
