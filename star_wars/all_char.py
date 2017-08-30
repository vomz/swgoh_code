import requests, sys, codecs, itertools, operator
from bs4 import BeautifulSoup

session = requests.session()
front = session.get('https://swgoh.gg/')
collection = BeautifulSoup(front.text,'html.parser')
toons=collection.find_all("li","media list-group-item p-0 character")

links = []
for i in range(0,len(toons)):
	links.append(toons[i].a.get('href'))

gear_list=[]
names=[]
#character
for h in range(0,len(links)):
	r = session.get('https://swgoh.gg'+links[h]+'gear/')
	gear = BeautifulSoup(r.text,'html.parser')
	names.append(gear.find_all('a','no-decoration')[0].text)
	rawlist = gear.find_all('ul','list-group media-list media-list-stream')
	#
	for i in range(0,len(rawlist[0])):
		inputs=[]
		numbers=[]
		glist={}
		aa=rawlist[0].findAll("li", {"class" : lambda L: L and L.startswith('media')})
		for j in range(0,len(aa)):
			try:
				if aa[j].h4.text.strip().split()[0]=='Gear' or aa[j].h4.text.strip().split()[0]=='Protection:':
					if (j/7)*7 >=42:
						glist[aa[(j/7)*7].h4.text.strip().split('\n')[1]]=[]
					else:
						glist[aa[(j/7)*7].h4.text.strip().split('\n')[0]]=[]
			except:
				if (j/7)*7 >=42:
					glist[aa[(j/7)*7].h4.text.strip().split('\n')[1]].append(aa[j].a.get('title'))
				else:
					glist[aa[(j/7)*7].h4.text.strip().split('\n')[0]].append(aa[j].a.get('title'))
	gear_list.append(glist)
file=open('all_char.txt','w')
for x in range(0,len(gear_list)):
	if 'Chirrut' in names[x]:
		names[x]='Chirrut'
	file.write(names[x]+":"+str(gear_list[x])+",")
file.close() 

