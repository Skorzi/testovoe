import csv
import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r = requests.get('https://mediakit.iportal.ru/our-team', headers=headers)
soup = r.content
mydivs = soup.find_all("div", {"class": ""})

if __name__== '__main__':
    print(r.content)