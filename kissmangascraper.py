#note this version works only for windows next version i will improve linux compatibility

#modules
import urllib3
from bs4 import BeautifulSoup
import os
import webbrowser

#clear function
clear = lambda: os.system('cls')
clear()  #clear the console

url_list = []
episode_url = 'https://1stkissmanga.com/manga/pounding/chapter-3' + input('Enter Episode Number $')
http = urllib3.PoolManager()
html = http.request('GET', episode_url)
soup = BeautifulSoup(html.data, features="html.parser")
title = soup.title.string
print(title)

imgs = soup.findAll("div", {"class":"page-break no-gaps"})

for img in imgs:
    img_urls = img.img['data-lazy-src']
    url_list.append(img_urls)
clear()


for img_url in range(len(url_list)):
	url_list[img_url] = '<img src=' + url_list[img_url] + '>'

img_urls_txt = '\n'.join(url_list)


site = '<html><head><title>' + title + '</title></head><bodystyle="margin: 0px;"><div style="text-align:center;background-color: #1d1d1d;padding: 0px;">' + img_urls_txt  + '</div></body></html>'

with open('index.html', 'w') as index:
	index.write(site)

path = os.getcwd()

import webbrowser

webbrowser.open('file://' + os.path.realpath('index.html'))

