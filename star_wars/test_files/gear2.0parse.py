import itertools
import operator
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
toon=['Wedge Antilles','Biggs Darklighter','Princess Leia','Stormtrooper Han','Lando Calrissian','Jedi Knight Anakin','CT-5555 "Fives"']

toons = open('C:/Users/ryburk/Desktop/Projects/Data/toons.txt','r')
toons = map(str.strip,toons.readlines())
levels = open('C:/Users/ryburk/Desktop/Projects/Data/levels.txt','r')
levels = map(str.strip,levels.readlines())
gear_level = open('C:/Users/ryburk/Desktop/Projects/Data/gear_level.txt','r')
gear_level = map(str.strip,gear_level.readlines())
gear1 = open('C:/Users/ryburk/Desktop/Projects/Data/gear1.txt','r')
gear1 = map(str.strip,gear1.readlines())
gear2 = open('C:/Users/ryburk/Desktop/Projects/Data/gear2.txt','r')
gear2 = map(str.strip,gear2.readlines())
gear3 = open('C:/Users/ryburk/Desktop/Projects/Data/gear3.txt','r')
gear3 = map(str.strip,gear3.readlines())
gear4 = open('C:/Users/ryburk/Desktop/Projects/Data/gear4.txt','r')
gear4 = map(str.strip,gear4.readlines())
gear5 = open('C:/Users/ryburk/Desktop/Projects/Data/gear5.txt','r')
gear5 = map(str.strip,gear5.readlines())
gear6 = open('C:/Users/ryburk/Desktop/Projects/Data/gear6.txt','r')
gear6 = map(str.strip,gear6.readlines())
stars = open('C:/Users/ryburk/Desktop/Projects/Data/stars.txt','r')
stars = map(str.strip,stars.readlines())
gear_needed = open('C:/Users/ryburk/Desktop/Projects/Data/gear_needed.txt','r')
gear_needed = map(str.strip,gear_needed.readlines())
number_needed = open('C:/Users/ryburk/Desktop/Projects/Data/number_needed.txt','r')
number_needed = map(str.strip,number_needed.readlines())
#gearnum = open('C:/Users/ryburk/Desktop/Projects/Data/gearnum.txt','r')
#gearnum = map(str.strip,gearnum.readlines())
gearname = open('C:/Users/ryburk/Desktop/Projects/Data/gearname.txt','r')
gearname = map(str.strip,gearname.readlines())
gearmats = open('C:/Users/ryburk/Desktop/Projects/Data/gearmats.txt','r')
gearmats = map(str.strip,gearmats.readlines())

team_gear=[]
team_gear1=[]
locked=[]

final={}
gear_list=list()
number_list=list()
for i in range(0,len(toons)):
	split1 = gear_needed[i].split(', ')
	split2 = number_needed[i].split(', ')
	gear_list.append(split1)
	number_list.append(split2)
for i in range(0,len(toon)):
	try:
		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
		place = place[0]
	except IndexError:
		continue
	for j in range(0,len(gear_list[place])):
		final[gear_list[place][j]]=0
for i in range(0,len(toon)):
	try:
		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
		place = place[0]
	except IndexError:
		locked.append(toon[i])
		continue
	chargear=[]
	for j in range(0,len(gear_list[place])):
		final[gear_list[place][j]]+=int(number_list[place][j])

	
	if gear1[place] != "None" and gear1[place] != "Unknown Gear":
		team_gear.append(gear1[place])
		team_gear1.append(gear1[place])
		chargear.append(gear1[place])
	if gear2[place] != "None" and gear2[place] != "Unknown Gear":
		team_gear.append(gear2[place])
		team_gear1.append(gear2[place])
		chargear.append(gear2[place])
	if gear3[place] != "None" and gear3[place] != "Unknown Gear":
		team_gear.append(gear3[place])
		team_gear1.append(gear3[place])
		chargear.append(gear3[place])
	if gear4[place] != "None" and gear4[place] != "Unknown Gear":
		team_gear.append(gear4[place])
		team_gear1.append(gear4[place])
		chargear.append(gear4[place])
	if gear5[place] != "None" and gear5[place] != "Unknown Gear":
		team_gear.append(gear5[place])
		team_gear1.append(gear5[place])
		chargear.append(gear5[place])
	if gear6[place] != "None" and gear6[place] != "Unknown Gear":
		team_gear.append(gear6[place])
		team_gear1.append(gear6[place])
		chargear.append(gear6[place])

	f=open('C:/Users/ryburk/Desktop/Projects/Data/output.csv','r')
	file=f.readlines()
	f.close()

	part1=[]
	for i in range(0,len(file)):
		part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))

	gear={}
	for i in range(0,len(part1)):
		mats={}
		for j in range(1,len(part1[i])-1,2):
			mats[part1[i][j]]=int(part1[i][j+1])
		gear[part1[i][0]]=mats

	team_gear2={}
	for key,val in final.items():
		for keys,vals in gear[key].items():
			try:
				team_gear2[keys]=team_gear2[keys]+(vals*val)
			except KeyError:
				team_gear2[keys]=vals*val



body = "Have you unlocked "+' or '.join(locked)+"?\n\n"+"\n"

for key, val in team_gear2.items():
	if val > 0:
		print key+": "+str(val)

'''
f=open('C:/Users/ryburk/Desktop/Projects/Data/output.csv','r')
file=f.readlines()
f.close()

part1=[]
for i in range(0,len(file)):
part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))

gear={}
for i in range(0,len(part1)):
mats={}
for j in range(1,len(part1[i])-1,2):
	mats[part1[i][j]]=part1[i][j+1]
gear[part1[i][0]]=mats
'''