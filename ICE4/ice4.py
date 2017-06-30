import requests
from bs4 import BeautifulSoup
import os

def search(key):
    url = "https://en.wikipedia.org/w/index.php?limit=offset=0&search="+key
    # url = "https://en.wikipedia.org/w/index.php?limit="+lim+"&offset=0&search="+sea
    content = requests.get(url)
    # extracted_text = content.text
    soup = BeautifulSoup(content.content, "html.parser")

    print("---------prettify output--------")
    print(soup.prettify())

    print("---------body output--------")
    body = soup.find('body')
    print(body.get_text())

    print("------------The h1 in body-----------------")
    for data_body in soup.find_all('body'):
        for data in data_body.find_all('div'):
            result = data.find('h1')
            if (result!=None):
                print(result.get_text())


    print("------------The h1 in div-----------------")
    for data in soup.find_all('div'):
        result = data.find('h1')
        if (result!=None):
            print(result.get_text())

def main():
    str = input("enter the word that you want to search for:")
    search(str)

main()