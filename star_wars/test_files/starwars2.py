import requests, sys, codecs
from bs4 import BeautifulSoup

# Start a session so we can have persistant cookies
session = requests.session()

# Try accessing a page that requires you to be logged in
r = session.get('https://swgoh.gg')

#collection = BeautifulSoup(r.text,'html.parser').encode('utf-8')
collection = BeautifulSoup(r.text,'html.parser')
toons=collection.find_all("li","media list-group-item p-0 character")
num_chars = len(toons)

links = []
for i in range(0,num_chars):
	links.append(toons[i].a.get('href'))
names=[]
shards=[]
for i in range(0,len(links)):
	page=session.get('https://swgoh.gg/'+links[i])
	character=BeautifulSoup(page.text,'html.parser')
	names.append(character.find_all('a','no-decoration')[0].text)
	shards.append(character.find_all('div','pull-right')[18].text)
	page=page.close()

file = open('shards.txt','w')
for i in range(0,len(names)):
	file.write(names[i]+","+shards[i]+"\n")
file.close()

