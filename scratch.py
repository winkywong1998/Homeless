import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

def getHtml(URL):
    response = requests.get(URL,headers = headers)
    if response.status_code == 200:
        parseHtml(response.text)
    else:
        print("Error", response.status_code)

def parseHtml(content):
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup)
    for i in soup.findAll(name='div', attrs={'class': 'flex card-container'}):
        print(i)
    # rowSingle = soup.find('div', class_= "content row-single")
    # print(rowSingle)
if __name__ == '__main__':
    URL = "https://www.morgan-properties.com/apartments/md/baltimore/the-carlyle/floor-plans#/"
    getHtml(URL)