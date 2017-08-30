import requests, sys, codecs
from bs4 import BeautifulSoup

a="list-group media-list media-list-stream"
session = requests.session()
# Try accessing a page that requires you to be logged in
r = session.get('https://swgoh.gg/')

#collection = BeautifulSoup(r.text,'html.parser').encode('utf-8')
collection = BeautifulSoup(r.text,'html.parser')
toons=collection.find_all("li","media list-group-item p-0 character")
num_chars = len(toons)

links = []
for i in range(0,num_chars):
	links.append(toons[i].a.get('href'))


