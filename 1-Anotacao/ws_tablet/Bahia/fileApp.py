#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib3
import time
import random

#Casas Bahia possui certificado de proteção para scrap
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

class Get(object):

    _qnt_dados_atual = 0

    #Produz dados para extração
    @staticmethod
    def __iniciador__ (url, sleep = 0.5):

        time.sleep(abs(sleep + random.randint(-5, 5)/20))
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        http = urllib3.PoolManager(10, headers=user_agent)
        conteudo= http.request('GET', url)
        soup = BeautifulSoup(conteudo.data.decode('utf-8'), 'html.parser')
        return soup

    def __PropriedadesCod__(self, soup, qntDados):
        var = self.__controlador__(self, soup, qntDados)
        return var

    #Método gerenciador e retorna uma lista de dicionários de produtos
    @staticmethod
    def __controlador__ (self, soup, qntDados):
        prods = list()
        x = self.__class__._qnt_dados_atual
        while x < qntDados:
            links = self.__linksProds__(self, soup, qntDados)
            for i in links:
                prods.append(self.__informacoes__(i))
            x += self.__class__._qnt_dados_atual
            url2 = self.__proxPag__(soup)
            print(url2)
            print("\n")
            soup = self.__iniciador__(url2)
        return prods

    #Pega todos links de notebooks da página atual
    @staticmethod
    def __linksProds__ (self, soup, qntDados) :
        resUrl = []
        for div in soup.findAll('div', {'class':'cont-product'}):
            if (self.__class__._qnt_dados_atual < qntDados):
                a = div.find('a')
                resUrl.append(a.attrs['href'])
                self.__class__._qnt_dados_atual += 1
        # for i in resUrl:
        #     print(i)
        return resUrl

    #Pega o link da proxima página
    @staticmethod
    def __proxPag__ (soup):
        encontrou = False
        link = str()
        point = ''
        compare = "<li class="+"\""+"atual"+ "\""+"><strong>"
        for ul in soup.findAll('ul', {'class':'ListaPaginas'}):
            for li in ul.find_all('li'):

                # Se a string compare está contida em str(li)
                if ( compare in str(li) ):
                    point = 'Ready'
                    print("here")
                if (li.find('a') and ((encontrou == False) and (point =='Ready')) ):
                        encontrou = True
                        a = li.find('a')
                        link = str(a.attrs['href'])
        return link


    #Pega todos os dados da página do produto:
    @staticmethod
    def __informacoes__ (url, sleep = 0.5):

        time.sleep(abs(sleep + random.randint(-5, 5)/20))
        http = urllib3.PoolManager(10, headers=user_agent)
        conteudo_prod = http.request('GET', url)

        soup_prod = BeautifulSoup(conteudo_prod.data.decode('utf-8'), 'html.parser')
        b = soup_prod.find_all("b")
        dt = soup_prod.find_all("dt", )
        dd = soup_prod.find_all("dd")
        info = dict()
        info['title'] = b[0].get_text().encode('utf8')

        #get_text(strip=True, separator='  '): remove espaços inúteis
        # print("tam dd:", len(dd))
        # for i in range(0, len(dd)):
        #     print(dd[i].get_text(strip=True, separator='  '))

        # print("\n \n")

        # print("tam dt:", len(dt))
        # for j in range(0, len(dt)):
        #     print(dt[j].get_text(strip=True, separator='  '))

        for i in range(0, len(dt)):
            info[dt[i].get_text(strip=True, separator='  ').encode('utf8')] = dd[i].get_text(strip=True, separator='  ').encode('utf8')
                #info['description'] = p[0].get_text().encode('utf8')
        return info

        @classmethod
        def all(cls):
            return cls.objects