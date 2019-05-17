from bs4 import BeautifulSoup
import requests

class Get:

    @staticmethod
    def informacoes(url):
        conteudo_prod = requests.get(url)
        soup_prod = BeautifulSoup(conteudo_prod.content, 'html.parser')
        b = soup_prod.find_all("b")
        dt = soup_prod.find_all("dt")
        dd = soup_prod.find_all("dd")
        info = dict()
        info['title'] = h1[0].get_text().encode('utf8')
        for i in dt:
            info[i] = d[len(i)]
        #info['description'] = p[0].get_text().encode('utf8')
        return info
