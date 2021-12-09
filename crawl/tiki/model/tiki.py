import requests
from bs4 import BeautifulSoup

class tiki():
    def __init__(self,key) -> None:
        self.key = str(key).replace(' ','%20')
        self.url = 'https://tiki.vn/search?q='+self.key
        
    def getProduct(self):
        # sent requests
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        source = requests.get(self.url, headers=headers)

        # receive respone and process data
        page = BeautifulSoup(source.text, 'html.parser')
        

        data ={
            "title": title,
            "price": price,
            "sold": sold,
            "image": image,
            "link": link
        }

        return data

    def insertData(self):
        pass