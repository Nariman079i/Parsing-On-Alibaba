#парсинг товаров с Alibaba

from requests import *
from bs4 import BeautifulSoup as Bs
from time import time

_url = "https://www.alibaba.com/trade/search?IndexArea=product_en&SearchText=iphone12&page=2"
_parser = "lxml"

def search_goods():

    content = get(_url)

    if content.status_code == 200:

        text = content.text
        soup = Bs(text , _parser)
        title = soup.findAll('h2')

        urls = []

        for t in title:
            urls.append("https:"+str(t.find('a').get("href")))

        for url in urls[0:2]:
            content = get(url).text
            soup = Bs(content , _parser).find_all('div')

            for elem in soup:
                r = str(elem.find('h1' ))
                if r == "None":
                    continue
                else:
                    print(r.split('"')[3].split("  ")[0])







search_goods()