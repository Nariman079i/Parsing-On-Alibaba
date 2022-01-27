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
    div = soup.find_all('h2')
    price = soup.find_all('div')

    for i in price:

        print(i.find('div', _class="list-no-v2-outter J-offer-wrapper").find('span'))


search_goods()