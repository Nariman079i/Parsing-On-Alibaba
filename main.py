#парсинг товаров с Alibaba

from requests import *
from bs4 import BeautifulSoup as Bs
from time import time

url = "https://www.alibaba.com/trade/search?IndexArea=product_en&SearchText=iphone12&page=2"
_parser = "lxml"

def search_goods():

    content = get(url)
    print(content.status_code)
    content = content.text


    soup = Bs(content , _parser)
    div = soup.findAll('h2')


    for i in div:
        outPut = str(i.find('a').get("href"))
        print(outPut.strip('//'))


search_goods()