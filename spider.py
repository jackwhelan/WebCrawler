import requests
from bs4 import BeautifulSoup

def ebay_spider(max_pages, sort_by):
    page = 0
    while page < max_pages:
        page += 1
        url = 'https://www.ebay.ie/b/Internal-Hard-Disk-Drives/56083/bn_780224?rt=nc&_pgn=' + str(page) + '&'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class':'s-item__link'}):
            href = link.get('href')
            title = link.string
            print(title)

ebay_spider(1)