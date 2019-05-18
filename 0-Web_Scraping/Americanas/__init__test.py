#!/usr/bin/python3
# -*- coding: utf-8 -*-

from b2w import B2W
import json

#Suggest use to execute this file command line : python2 __init__.py
#Or execute normal switch function dump to dumps

codes = B2W.Get_Prod_Codes_By_Cat("https://www.americanas.com.br/categoria/informatica/notebook", 1000)
prods = B2W.Get_Properties_By_Cods(codes)

