from bs4 import BeautifulSoup
import requests
# import time
# time.sleep(0.5)
mainpage=requests.get('https://coinmarketcap.com/exchanges/binance/',verify=False)
soup=BeautifulSoup(mainpage.content,'html.parser')

whatis=soup.find_all("div",{'class':'sc-3502f6cd-0 JxHqg'})
title=whatis[0].find_all('h2')
print(title[0].text.strip()+"\n")