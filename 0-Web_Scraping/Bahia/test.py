#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib3

#Pega todos os dados da página do produto:
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
url = "https://www.casasbahia.com.br/Informatica/Notebook/notebook-samsung-core-i3-7020u-4gb-1tb-tela-full-hd-15-6-windows-10-essentials-e30-np350xaa-kf2br-12918894.html?rectype=p1_ov_f_s1&recsource=cat-57"
http = urllib3.PoolManager(10, headers=user_agent)

conteudo_prod = http.request('GET', url)

soup_prod = BeautifulSoup(conteudo_prod.data.decode('utf-8'), 'html.parser')
b = soup_prod.find_all("b")
dt = soup_prod.find_all("dt", )
dd = soup_prod.find_all("dd")
info = dict()
info['title'] = b[0].get_text()

#get_text(strip=True, separator='  '): remove espaços inúteis
# print("tam dd:", len(dd))
# for i in range(0, len(dd)):
#     print(dd[i].get_text(strip=True, separator='  '))

# print("\n \n")

# print("tam dt:", len(dt))
# for j in range(0, len(dt)):
#     print(dt[j].get_text(strip=True, separator='  '))

for i in range(0, len(dt)):
    info[dt[i].get_text(strip=True, separator='  ')] = dd[i].get_text(strip=True, separator='  ')
