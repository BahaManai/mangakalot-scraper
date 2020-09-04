#note this version works only for windows next version i will improve linux compatibility

#modules
import urllib3
from bs4 import BeautifulSoup
import os
import webbrowser

#clear function
clear = lambda: os.system('cls')
clear()  #clear the console

episode_url = 'https://ww1.mangakakalots.com/chapter/kj922361/chapter_' + input('Enter Episode Number $')
http = urllib3.PoolManager()
html = http.request('GET', episode_url)
soup = BeautifulSoup(html.data, features="html.parser")
title = soup.title.string

imgs = soup.findAll('div', class_ = "vung-doc")

im = imgs.__str__()

site = '<html><head><title>' + title + '</title></head><bodystyle="margin: 0px;"><div style="text-align:center;background-color: #1d1d1d;padding: 0px;">' + im  + '</div></body></html>'

with open('index.html', 'w') as index: index.write(site)

webbrowser.open('file://' + os.path.realpath('index.html'))
