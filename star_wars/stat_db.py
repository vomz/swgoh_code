import requests
import operator
import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#which toons are wanted
#toon=['Darth Vader','Tusken Shaman','Boba Fett','Darth Sidious','Captain Phasma','R2-D2']
toon=['Luke Skywalker','Ahsoka Tano (Fulcrum)','Captain Phasma','Kylo Ren','First Order Officer','First Order TIE Pilot','First Order Stormtrooper']
#opens and reads all files created by starwars.py and creates other variables that are needed
toons = open('Data/toons.txt','r')
toons = map(str.strip,toons.readlines())
levels = open('Data/levels.txt','r')
levels = map(str.strip,levels.readlines())
gear_level = open('Data/gear_level.txt','r')
gear_level = map(str.strip,gear_level.readlines())
stars = open('Data/stars.txt','r')
stars = map(str.strip,stars.readlines())
gear_needed = open('Data/gear_needed.txt','r')
gear_needed = map(str.strip,gear_needed.readlines())
number_needed = open('Data/number_needed.txt','r')
number_needed = map(str.strip,number_needed.readlines())
locked=[]
final={}
gear_list=list()
number_list=list()


#adds individual characters gear to list of gear needed
for i in range(0,len(toons)):
	split1 = gear_needed[i].split(', ')
	split2 = number_needed[i].split(', ')
	gear_list.append(split1)
	number_list.append(split2)

#creates the team's gear dictionary	
for i in range(0,len(toon)):
	try:
		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
		place = place[0]
	except IndexError:
		continue
	for j in range(0,len(gear_list[place])):
		final[gear_list[place][j]]=0

#Creates an entry into the gear dictionary for each character, if character has been unlocked
for i in range(0,len(toon)):
	try:
		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
		place = place[0]
	except IndexError:
		locked.append(toon[i])
		continue
	for j in range(0,len(gear_list[place])):
		final[gear_list[place][j]]+=int(number_list[place][j])

	f=open('Data/output.csv','r')
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
	delta={}
	for i in range(0,len(toon)):
		g=[]
		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
		place = place[0]
		for j in range(0,len(gear_list[place])):
			g.append(gear_list[place][j]+': '+number_list[place][j])
		delta[toon[i]]=g

#creates printable list of all the farmable gear needed
input_list=[]
sorted_team_gear2 = sorted(team_gear2.items(), key=operator.itemgetter(1),reverse=True)
for i in range(0,len(sorted_team_gear2)):
	input_list.append(sorted_team_gear2[i][0]+": "+str(sorted_team_gear2[i][1]))

full_list=[]
sorted_final = sorted(final.items(), key=operator.itemgetter(1),reverse=True)
for i in range(0,len(sorted_final)):
	full_list.append(sorted_final[i][0]+": "+str(sorted_final[i][1]))

delta_list=[]
for name,dgear in delta.items():
	delta_list.append(name+':\n'+'\n'.join(dgear))


#creates the body of the email
if len(locked) > 0:
	body = "Have you unlocked "+' or '.join(locked)+"?\n"+'These are the pieces of salvage:\n\n'+'\n'.join(input_list)+'\n\n'+'\n\n'.join(delta_list)
else:
	body = 'These are the pieces of salvage:\n\n'+'\n'.join(input_list)+'\n\n'+'\n\n'.join(delta_list)


# Record the MIME type
email_body = MIMEText(body, 'plain')

# Attach body into message container.
msg.attach(email_body)

# Send the message via local SMTP server.
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login('rcburky@gmail.com','1rznnmhcbtllJ@')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
server.sendmail(sender, recipient, msg.as_string())
server.quit()