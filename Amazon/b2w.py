#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging
import time
import random
from tqdm import tqdm


class B2W:
    
    # Recupera informações de um produto com base em sua URL
    @staticmethod
    def Get_Properties_By_Prod(url):

        # Recupera página
        page = requests.get(url)

        # Extrai os dados do HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        res = soup.find_all("td")

        for i in res:
            print(i)
        #<h1 class="product-title__TitleUI-sc-116vf1e-0 fhQQvU TitleH1-c6mv26-0 lgUBdv" id="product-name-default" icon="[object Object]">Notebook Essentials E30 Intel Core I3 4GB 1TB LED Full HD 15.6'' W10 Cinza Titânio - Samsung</h1>#

        span = soup.find_all("span")

        for j in span:
            print(j)
        # Dicionário para armazenar as propriedades do produto
        values = dict()
        values['title'] = span[0].get_text().encode('utf8')

        # Recupera cada par; propriedade e valor
        for idx in range(0, len(res), 2):
            values[res[idx].get_text().encode('utf8')] = res[idx + 1].get_text().encode('utf8')

        # Retorna valores
        return values
    
    @staticmethod
    def Get_Properties_By_Cods(codes, sleep = 0.5):
                
        prods = list()
        for code in tqdm(codes, desc='Downloading properties by {} products'.format(len(codes))):
            url = '//www.amazon.com.br/gp/product/{}'.format(code)
            prods.append(B2W.Get_Properties_By_Prod(url))
            time.sleep(sleep + random.randint(-5, 5)/20)
            print(code)

        return prods
    
    
    # Recupera os IDs dos produtos de uma determina categoria (URL)
    @staticmethod
    def Get_Prod_Codes_By_Cat(url, count_limit, sleep = 0.5):
        pattern1 = 'TouchableA-sc-9v9alh-0 bCFQWo" href="/product/'
        pattern2 = 'ref='
        limite = 24
        offset = 0
        url += '?limite={}&offset={}'

        #https://www.americanas.com.br/produto/133621821/notebook-samsung-expert-x40-intel-core-8a-i5-quad-core-8gb-geforce-mx110-com-2gb-1tb-tela-led-hd-15-6-windows-10-cinza-titanio?pfm_carac=Notebook&pfm_index=1&pfm_page=category&pfm_pos=grid&pfm_type=vit_product_grid&sellerId&voltagem=BIVOLT

        codeList = list()
        oldSize = len(codeList)

        # Condição de parada para mudanças de páginas
        stop = False

        # Enquanto houver conteúdo na página
        while not stop and len(codeList) < count_limit:

            # recupera página
            r = requests.get(url.format(limite, offset))

            # Recupera texto do HTML
            text = r.text

            # Condição de parada para quantidade de produtos
            cond = True

            # Enquando houver produtos a serem extraídos
            while (cond) and len(codeList) < count_limit:

                # tenta buscas, quando não encontra lança erro
                try:
                    idx1 = text.index(pattern1) + len(pattern1)
                    #idx2 = text.index(pattern2)
                    code = text[idx1:idx1 + 9]
                    text = text[idx1 + 9:]#[idx2 + len(idx2):]

                    try:
                        idx2 = code.index('?')

                        code = code[:idx2]

                    except:
                        pass

                    codeList.append(code)

                except:
                    # Fim da página
                    cond = False

            # Verifica se realizou leitura
            if oldSize == len(codeList):
                stop = True
            else:
                # Atualiza valor da quantidade de elementos anterior
                oldSize = len(codeList)

                # Muda offset da página para nova leitura
                offset += limite
                logging.info('{} IDs extraídos'.format(oldSize))
                time.sleep(sleep + random.randint(-5, 5)/20)

        return codeList

