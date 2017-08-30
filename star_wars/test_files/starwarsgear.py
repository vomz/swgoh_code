import requests, sys, codecs
from bs4 import BeautifulSoup
'''
# Start a session so we can have persistant cookies
session = requests.session()
r = session.get('https://swgoh.gg/db/gear/')
gear = BeautifulSoup(r.text,'html.parser')
beta = gear.find_all('div','col-md-4 gear')
main_link=[]
main_item=[]

for i in range(0,len(beta)):
	main_link.append(beta[i].a.get('href'))
	main_item.append(beta[i].h5.text)

main_name=[]
main_mats=[]
main_num=[]


for a in range(0,len(main_item)):
	matnum=[]
	matname=[]

	site = 'https://swgoh.gg'+main_link[a]
	s = session.get(site)
	piece = BeautifulSoup(s.text,'html.parser')
	materials = piece.find_all('a','media-body gear-tooltip')
	numbers = piece.find_all('div','pull-left')
	for b in range(0,len(materials)):
		try:
			matnum.append(int(materials[b].div.text.split('x')[0]))
			matname.append(materials[b].get('title'))
		except:
			continue
	main_name.append(main_item[a])
	main_mats.append(matname)
	main_num.append(matnum)

file = open('gearname.txt','w')
for i in range(0,len(main_name)):
	file.write(str(main_name[i])+"\n")
file.close()

file = open('gearmats.txt','w')
for i in range(0,len(main_mats)):
	for j in range(0,len(main_mats[i])):
		if j == len(main_mats[i])-1:
			file.write(str(main_mats[i][j])+"\n")
		else:
			file.write(str(main_mats[i][j])+", ")
file.close()

file = open('gearnum.txt','w')
for i in range(0,len(main_num)):
	for j in range(0,len(main_num[i])):
		if j == len(main_num[i])-1:
			file.write(str(main_num[i][j])+"\n")
		else:
			file.write(str(main_num[i][j])+", ")
file.close()



'''
# Start a session so we can have persistant cookies
session = requests.session()
r = session.get('https://swgoh.gg/db/gear/')
gear = BeautifulSoup(r.text,'html.parser')
beta = gear.find_all('div','col-md-4 gear')
main_link=[]
main_item=[]

for i in range(0,len(beta)):
	main_link.append(beta[i].a.get('href'))
	main_item.append(beta[i].h5.text)

main_name=[]
main_mats=[]
main_num=[]


for a in range(0,len(main_link)):
	matnum=[]
	matname=[]

	site = 'https://swgoh.gg'+main_link[a]
	s = session.get(site)
	piece = BeautifulSoup(s.text,'html.parser')
	materials = piece.find_all('a','media-body gear-tooltip')
	for i in range(0,len(materials)):
		if 'gear-icon-small' in str(materials[i]):
			mat_array = materials[i].find_all('span',class_='gear-icon-small')
			try:
				for j in range(0,len(mat_array)):
					matnum.append(int(mat_array[j].parent.text.split('x')[0].strip()))
					matname.append(mat_array[j].get('title'))
			except:
				continue
		else:
			try:
				matnum.append(int(materials[i].div.text.split('x')[0]))
				matname.append(materials[i].get('title'))
			except:
				continue

	main_name.append(main_item[a])
	main_mats.append(matname)
	main_num.append(matnum)

file = open('gearname.txt','w')
for i in range(0,len(main_name)):
	file.write(str(main_name[i])+"\n")
file.close()

file = open('gearmats.txt','w')
for i in range(0,len(main_mats)):
	for j in range(0,len(main_mats[i])):
		if j == len(main_mats[i])-1:
			file.write(str(main_mats[i][j])+"\n")
		else:
			file.write(str(main_mats[i][j])+", ")
file.close()

file = open('gearnum.txt','w')
for i in range(0,len(main_num)):
	for j in range(0,len(main_num[i])):
		if j == len(main_num[i])-1:
			file.write(str(main_num[i][j])+"\n")
		else:
			file.write(str(main_num[i][j])+", ")
file.close()


