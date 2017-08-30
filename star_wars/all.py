import requests, sys, codecs, itertools, operator
from bs4 import BeautifulSoup

session = requests.session()
front = session.get('https://swgoh.gg/')
collection = BeautifulSoup(front.text,'html.parser')
toons=collection.find_all("li","media list-group-item p-0 character")

links = []
for i in range(0,len(toons)):
	links.append(toons[i].a.get('href'))
char=[]
list=[]
for h in range(0,len(toons)):
	r = session.get('https://swgoh.gg'+links[h]+'gear/')
	gear = BeautifulSoup(r.text,'html.parser')
	rawlist = gear.find_all('li', 'media list-group-item p-0 character')
	name = gear.find_all('a', 'no-decoration')[0].text
	gear_list={}
	for i in range(0,len(rawlist)):
		inputs=[]
		numbers=[]
		mats={}
		try:
			for j in range(0,len(rawlist[i].find_all('li'))):
				inputs.append(rawlist[i].find_all('li')[j].span.get('title'))
		except IndexError:
			inputs.append("None")
		try:
			for j in range(0,len(rawlist[i].find_all('li'))):
				numbers.append(int(rawlist[i].find_all('li')[j].text.split('x')[0].strip()))
		except IndexError:
			numbers.append("None")

		for j in range(0,len(inputs)):
			mats[inputs[j]]=numbers[j]
		try:
			gear_list[rawlist[i].a.get('title')]
			gear_list[rawlist[i].a.get('title')]=gear_list[rawlist[i].a.get('title')]+1
		except:
			gear_list[rawlist[i].a.get('title')]=1
					

	char.append(name)
	list.append(gear_list)


file=open('all.txt','w')
for i in range(0,len(char)):
	file.write(char[i]+";")
	for key,value in list[i].items():
		file.write(str(key)+","+str(value)+";")
	file.write("\n")
file.close()