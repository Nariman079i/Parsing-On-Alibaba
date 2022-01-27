#парсинг товаров с Alibaba

from requests import *
from bs4 import BeautifulSoup as Bs
from time import time

url = "https://www.alibaba.com/trade/search?IndexArea=product_en&SearchText=iphone12&page=2&f0=y"
_parser = "html.parser"

def search_goods():

    content = get(url)
    content = content.text

    soup = Bs(content , _parser)

    print(soup)

search_goods()