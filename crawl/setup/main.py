import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

def get_data(link):
    title = ''
    category = ''
    content = ''

    data = {
        "tilte": title,
        "category": category,
        "content": content
    }
    return data


def main():

    print("======= Begin =========")
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Title', 'Category', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(1,10):
            url = ''
            # driver = webdriver.Chrome('/home/cuong/project/crawl/search.robots.jobs/chromedriver')
            # driver.get(url)
            # source = driver.page_source
            # soup = BeautifulSoup(source, 'html.parser')
           
            # source = requests.get(url)
            # soup = BeautifulSoup(source.text, 'html.parser')
            
            
            job_page = soup.find_all('div', class_='')
            for idx, itm in enumerate(job_page):
                link = itm.find('a')['href']
                data = get_data(link,idx)

                writer.writerow({
                    'Title': data["tilte"], 
                    'Category': data["category"],
                    'Content': data["content"]
                    })
            # driver.quit()

if __name__ == "__main__":
    main()