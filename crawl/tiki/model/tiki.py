from logging import error
import time
import requests
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup


class tiki():
    __rootLink = 'https://tiki.vn/'
    
    def __init__(self,key,file):
        self.key = re.sub("\s+", "+", str(key))
        self.url = 'https://tiki.vn/search?q='+self.key
        self.file = file
    
    def open_file(self):
        data =  open(self.file, 'w',  newline = '', encoding="UTF-8") 
        fieldnames = ["Title", "Price", "Link"]
        self.writer = csv.DictWriter(data, fieldnames=fieldnames)
        self.writer.writeheader()

    def getProduct(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        source = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(source.text, 'html.parser')
        data = soup.find_all('a',class_='product-item')

        for itm in data:
            try:
                data ={
                    "title": itm.select_one('.name span').text.strip(),
                    "price": itm.select_one('.price-discount__price').text.strip(),
                    "link": 'https://tiki.vn'+itm['href'].replace('https://tiki.vn','')
                }
                self.writer.writerow({"Title": data["title"].title() , "Price": data["price"], "Link": data["link"]})
                print(data)
            except NameError:
                print(NameError)
        
    def insertData(self):
        # insert data into database
        pass

    def close_file(self):
        self.file.close()