from logging import error
import time
import requests
import re
import csv
from bs4 import BeautifulSoup


class tiki():
    __rootLink = 'https://tiki.vn/'
    
    def __init__(self,key,file):
        self.key = re.sub("\s+", "+", str(key))
        # self.url = 'https://tiki.vn/search?q='+self.key
        self.file = file
    
    def check_value(value):
        return value if value else None

    def insert_data(self, **data):
        self.writer.writerow({"Title": data["title"].title() , "Price": data["price"], "Link": data["link"]})

    def open_file(self):
        self.file=  open(self.file, 'a',  newline = '', encoding="UTF-8") 
        fieldnames = ["Title", "Price", "Link"]
        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()

    def getProduct(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        source = requests.get(url, headers=headers)
        soup = BeautifulSoup(source.text, 'html.parser')
        data = soup.find_all('a',class_='product-item')
        for itm in data:
            try:
                data ={
                    "title": tiki.check_value(itm.select_one('h3').text.strip()),
                    "price": tiki.check_value(itm.select_one('.price-discount__price').text.strip()),
                    "link": tiki.check_value('https://tiki.vn'+itm['href'].replace('https://tiki.vn',''))
                }
                # self.writer.writerow({"Title": data["title"].title() , "Price": data["price"], "Link": data["link"]})
                tiki.insert_data(self, **data)
                print(data)
            except NameError:
                print(NameError)

    def close_file(self):
        self.file.close()