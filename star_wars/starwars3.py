import requests
import operator
import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#sender's address
sender = "titaniusvomz@gmail.com"
#recipient's address
recipient = "rcburky@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Gear Report'
msg['From'] = sender
msg['To'] = recipient
msg['BCC'] = 'rcburky@gmail.com'

# #function to choose up to ten characters to study
# def choose():
# 	toon=[]
# 	alpha = raw_input("How many characters do you want to evaluate? (no more than 10!!)")
# 	if alpha == '1':
# 		toon.append(raw_input("Which character should be first?"))
# 	elif alpha == '2':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 	elif alpha == '3':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '4':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '5':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Which character should be fourth?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '6':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Which character should be fourth?"))
# 		toon.append(raw_input("Which character should be fifth?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '7':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Which character should be fourth?"))
# 		toon.append(raw_input("Which character should be fifth?"))
# 		toon.append(raw_input("Which character should be sixth?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '8':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Which character should be fourth?"))
# 		toon.append(raw_input("Which character should be fifth?"))
# 		toon.append(raw_input("Which character should be sixth?"))
# 		toon.append(raw_input("Which character should be seventh?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '9':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Which character should be fourth?"))
# 		toon.append(raw_input("Which character should be fifth?"))
# 		toon.append(raw_input("Which character should be sixth?"))
# 		toon.append(raw_input("Which character should be seventh?"))
# 		toon.append(raw_input("Which character should be eighth?"))
# 		toon.append(raw_input("Who is the last character you want?"))
# 	elif alpha == '10':
# 		toon.append(raw_input("Which character should be first?"))
# 		toon.append(raw_input("Which character should be second?"))
# 		toon.append(raw_input("Which character should be third?"))
# 		toon.append(raw_input("Which character should be fourth?"))
# 		toon.append(raw_input("Which character should be fifth?"))
# 		toon.append(raw_input("Which character should be sixth?"))
# 		toon.append(raw_input("Which character should be seventh?"))
# 		toon.append(raw_input("Which character should be eighth?"))
# 		toon.append(raw_input("Which character should be ninth?"))
# 		toon.append(raw_input("Who is the last character you want?"))
	

# 	#opens and reads all files created by starwars.py and creates other variables that are needed
# 	toons = open('Data/toons.txt','r')
# 	toons = map(str.strip,toons.readlines())
# 	levels = open('Data/levels.txt','r')
# 	levels = map(str.strip,levels.readlines())
# 	gear_level = open('Data/gear_level.txt','r')
# 	gear_level = map(str.strip,gear_level.readlines())
# 	stars = open('Data/stars.txt','r')
# 	stars = map(str.strip,stars.readlines())
# 	gear_needed = open('Data/gear_needed.txt','r')
# 	gear_needed = map(str.strip,gear_needed.readlines())
# 	number_needed = open('Data/number_needed.txt','r')
# 	number_needed = map(str.strip,number_needed.readlines())
# 	locked=[]
# 	final={}
# 	gear_list=list()
# 	number_list=list()


# 	#adds individual characters gear to list of gear needed
# 	for i in range(0,len(toons)):
# 		split1 = gear_needed[i].split(', ')
# 		split2 = number_needed[i].split(', ')
# 		gear_list.append(split1)
# 		number_list.append(split2)

# 	#creates the team's gear dictionary	
# 	for i in range(0,len(toon)):
# 		try:
# 			place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 			place = place[0]
# 		except IndexError:
# 			continue
# 		for j in range(0,len(gear_list[place])):
# 			final[gear_list[place][j]]=0

# 	#Creates an entry into the gear dictionary for each character, if character has been unlocked
# 	for i in range(0,len(toon)):
# 		try:
# 			place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 			place = place[0]
# 		except IndexError:
# 			locked.append(toon[i])
# 			continue
# 		for j in range(0,len(gear_list[place])):
# 			final[gear_list[place][j]]+=int(number_list[place][j])

# 		f=open('Data/output.csv','r')
# 		file=f.readlines()
# 		f.close()

# 		part1=[]
# 		for i in range(0,len(file)):
# 			part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))

# 		gear={}
# 		for i in range(0,len(part1)):
# 			mats={}
# 			for j in range(1,len(part1[i])-1,2):
# 				mats[part1[i][j]]=int(part1[i][j+1])
# 			gear[part1[i][0]]=mats

# 		team_gear2={}
# 		for key,val in final.items():
# 			for keys,vals in gear[key].items():
# 				try:
# 					team_gear2[keys]=team_gear2[keys]+(vals*val)
# 				except KeyError:
# 					team_gear2[keys]=vals*val

# 	#creates printable list of all the farmable gear needed
# 	input_list=[]
# 	sorted_team_gear2 = sorted(team_gear2.items(), key=operator.itemgetter(1),reverse=True)
# 	for i in range(0,len(sorted_team_gear2)):
# 		input_list.append(sorted_team_gear2[i][0]+": "+str(sorted_team_gear2[i][1]))

# 	full_list=[]
# 	sorted_final = sorted(final.items(), key=operator.itemgetter(1),reverse=True)
# 	for i in range(0,len(sorted_final)):
# 		full_list.append(sorted_final[i][0]+": "+str(sorted_final[i][1]))

# 	#creates the body of the email
# 	if len(locked) > 0:
# 		body = "Have you unlocked "+' or '.join(locked)+"?\n"+'These are the full pieces of gear '+', '.join(toon)+' need the most of.'+'\n\n'+'\n'.join(full_list)+'\n\nThese are the pieces of salvage:\n\n'+'\n'.join(input_list)
# 	else:
# 		body = 'These are the full pieces of gear '+', '.join(toon)+' need the most of.'+'\n\n'+'\n'.join(full_list)+'\n\nThese are the pieces of salvage:\n\n'+'\n'.join(input_list)

	
# 	# Record the MIME type
# 	email_body = MIMEText(body, 'plain')

# 	# Attach body into message container.
# 	msg.attach(email_body)

# 	# Send the message via local SMTP server.
# 	server = smtplib.SMTP('smtp.gmail.com:587')
# 	server.ehlo()
# 	server.starttls()
# 	server.ehlo()
# 	server.login('rcburky@gmail.com','')
# 	# sendmail function takes 3 arguments: sender's address, recipient's address
# 	# and message to send - here it is sent as one string.
# 	server.sendmail(sender, recipient, msg.as_string())
# 	server.quit()


# def arena():
	#which toons are wanted
toon=['Ahsoka Tano (Fulcrum)','Hera Syndulla','Ezra Bridger','Sabine Wren','Garazeb "Zeb" Orrelios','Kanan Jarrus','Jyn Erso','Cassian Andor','K-2SO','Chirrut Imwe','Baze Malbus']
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
    if gear_needed[i] == '':
        split1 = ['Complete']
        split2 = [0]
        gear_list.append(split1)
        number_list.append(split2)
    else:
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
        if gear_list[place][j]==['']:
            continue
        else:
            final[gear_list[place][j]]+=int(number_list[place][j])

    f=open('Data/output.csv','r')
    file=f.readlines()
    f.close()
    part1=[]
    for k in range(0,len(file)):
        part1.append(file[k].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))
        gear={}
        for l in range(0,len(part1)):
            mats={}
            for m in range(1,len(part1[l])-1,2):
                if part1[l][m] == '':
                    mats[part1[l][m]]=0
                    gear["Complete"]=mats
                else:
                    mats[part1[l][m]]=int(part1[l][m+1])
                    gear[part1[l][0]]=mats

    team_gear2={}
    for key,val in final.items():
        for keys,vals in gear[key].items():
            try:
                team_gear2[keys]=team_gear2[keys]+(vals*val)
            except KeyError:
                team_gear2[keys]=vals*val
    delta={}
    for k in range(0,len(toon)):
        g=[]
        place=[j for j,x in enumerate(toons) if x == "%s" % toon[k]]
        place = place[0]
        for j in range(0,len(gear_list[place])):
            g.append(str(gear_list[place][j])+': '+str(number_list[place][j]))
        delta[toon[k]]=g

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
server.login('rcburky@gmail.com','')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
server.sendmail(sender, recipient, msg.as_string())
server.quit()

# def everything():
# 	#opens and reads all files created by starwars.py and creates other variables that are needed
# 	toons = open('Data/toons.txt','r')
# 	toons = map(str.strip,toons.readlines())
# 	levels = open('Data/levels.txt','r')
# 	levels = map(str.strip,levels.readlines())
# 	gear_level = open('Data/gear_level.txt','r')
# 	gear_level = map(str.strip,gear_level.readlines())
# 	stars = open('Data/stars.txt','r')
# 	stars = map(str.strip,stars.readlines())
# 	gear_needed = open('Data/gear_needed.txt','r')
# 	gear_needed = map(str.strip,gear_needed.readlines())
# 	number_needed = open('Data/number_needed.txt','r')
# 	number_needed = map(str.strip,number_needed.readlines())
# 	locked=[]
# 	final={}
# 	gear_list=list()
# 	number_list=list()
# 	toon=toons

# 	#adds individual characters gear to list of gear needed
# 	for i in range(0,len(toons)):
# 		split1 = gear_needed[i].split(', ')
# 		split2 = number_needed[i].split(', ')
# 		gear_list.append(split1)
# 		number_list.append(split2)

# 	#creates the team's gear dictionary	
# 	for i in range(0,len(toon)):
# 		try:
# 			place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 			place = place[0]
# 		except IndexError:
# 			continue
# 		for j in range(0,len(gear_list[place])):
# 			final[gear_list[place][j]]=0

# 	#Creates an entry into the gear dictionary for each character, if character has been unlocked
# 	for i in range(0,len(toon)):
# 		try:
# 			place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 			place = place[0]
# 		except IndexError:
# 			locked.append(toon[i])
# 			continue
# 		for j in range(0,len(gear_list[place])):
# 			try:
# 				final[gear_list[place][j]]+=int(number_list[place][j])
# 			except:
# 				pass

# 		f=open('Data/output.csv','r')
# 		file=f.readlines()
# 		f.close()

# 		part1=[]
# 		for i in range(0,len(file)):
# 			part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))

# 		gear={}
# 		for i in range(0,len(part1)):
# 			mats={}
# 			for j in range(1,len(part1[i])-1,2):
# 				mats[part1[i][j]]=int(part1[i][j+1])
# 			gear[part1[i][0]]=mats

# 		team_gear2={}
# 		for key,val in final.items():
# 			try:
# 				for keys,vals in gear[key].items():
# 					try:
# 						team_gear2[keys]=team_gear2[keys]+(vals*val)
# 					except KeyError:
# 						team_gear2[keys]=vals*val
# 			except:
# 				pass

# 	#creates printable list of all the farmable gear needed
# 	input_list=[]
# 	sorted_team_gear2 = sorted(team_gear2.items(), key=operator.itemgetter(1),reverse=True)
# 	for i in range(0,len(sorted_team_gear2)):
# 		input_list.append(sorted_team_gear2[i][0]+","+str(sorted_team_gear2[i][1]))

# 	full_list=[]
# 	sorted_final = sorted(final.items(), key=operator.itemgetter(1),reverse=True)
# 	for i in range(0,len(sorted_final)):
# 		full_list.append(sorted_final[i][0]+","+str(sorted_final[i][1]))

# 	full_list.pop(len(full_list)-1)
# 	file=open('data.txt','w')
# 	file.write("Full Items,Count,Salvage Items,Count\n")
# 	if len(input_list) >= len(full_list):
# 		for i in range(0,len(input_list)):
# 			try:
# 				file.write(input_list[i]+","+full_list[i]+"\n")
# 			except:
# 				file.write(input_list[i]+"\n")
# 	elif len(input_list) < len(full_list):
# 		for i in range(0,len(full_list)):
# 			try:
# 				file.write(full_list[i]+","+input_list[i]+"\n")
# 			except:
# 				file.write(full_list[i]+"\n")



# def toons_sep():
# 	#opens and reads all files created by starwars.py and creates other variables that are needed
# 	toons = open('Data/toons.txt','r')
# 	toons = map(str.strip,toons.readlines())
# 	levels = open('Data/levels.txt','r')
# 	levels = map(str.strip,levels.readlines())
# 	gear_level = open('Data/gear_level.txt','r')
# 	gear_level = map(str.strip,gear_level.readlines())
# 	stars = open('Data/stars.txt','r')
# 	stars = map(str.strip,stars.readlines())
# 	gear_needed = open('Data/gear_needed.txt','r')
# 	gear_needed = map(str.strip,gear_needed.readlines())
# 	number_needed = open('Data/number_needed.txt','r')
# 	number_needed = map(str.strip,number_needed.readlines())

# 	toon=toons
# 	final={}
# 	input_list=[]
# 	full_list=[]
# 	for x in range(0,len(toon)):

# 		gear_list=[]
# 		number_list=[]
# 		#adds character's gear to list of gear needed
# 		split1 = gear_needed[x].split(', ')
# 		split2 = number_needed[x].split(', ')
# 		gear_list.append(split1)
# 		number_list.append(split2)
# 		#creates final dictionary
# 		for y in range(0,len(gear_list[0])):
# 			final[gear_list[0][y]]=number_list[0][y]

# 		f=open('Data/output.csv','r')
# 		file=f.readlines()
# 		f.close()

# 		part1=[]
# 		for i in range(0,len(file)):
# 			part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))

# 		gear={}
# 		for i in range(0,len(part1)):
# 			mats={}
# 			for j in range(1,len(part1[i])-1,2):
# 				mats[part1[i][j]]=int(part1[i][j+1])
# 			gear[part1[i][0]]=mats

# 		gear2={}
# 		for key,val in final.items():
# 			try:
# 				for keys,vals in gear[key].items():
# 					try:
# 						gear2[keys]=int(gear2[keys])+(int(vals)*int(val))
# 					except KeyError:
# 						gear2[keys]=int(vals)*int(val)
# 			except:
# 				pass

# 		#creates printable list of all the farmable gear needed
# 		sorted_gear2 = sorted(gear2.items(), key=operator.itemgetter(1),reverse=True)
# 		if len(sorted_gear2) == 0:
# 			input_list.append("Salvage Items:"+toon[x]+":None")
# 		else:
# 			for i in range(0,len(sorted_gear2)):
# 				input_list.append("Salvage Items:"+toon[x]+":"+sorted_gear2[i][0]+":"+str(sorted_gear2[i][1]))
# 		sorted_final = sorted(final.items(), key=operator.itemgetter(1),reverse=True)
# 		for i in range(0,len(sorted_final)):
# 			full_list.append("Full Items:"+toon[x]+":"+sorted_final[i][0]+":"+str(sorted_final[i][1]))

# 	file1=open('character_data.txt','w')
# 	file1.write('\n'.join(full_list)+"\n")
# 	file1.write('\n'.join(input_list)+"\n")
# 	file1.close()

# def gear_char():
# 	toon=['TIE Fighter Pilot','Clone Sergeant - Phase I','Boba Fett','Dengar']
# 	#characters = raw_input('List: ')
# 	#toon = characters.split(',')
# 	toons = open('Data/toons.txt','r')
# 	toons = map(str.strip,toons.readlines())
# 	gear_needed = open('Data/gear_needed.txt','r')
# 	gear_needed = map(str.strip,gear_needed.readlines())
# 	number_needed = open('Data/number_needed.txt','r')
# 	number_needed = map(str.strip,number_needed.readlines())
# 	gear_list=[]

# 	#adds individual characters gear to list of gear needed
# 	for i in range(0,len(toon)):
# 		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 		place = place[0]
# 		split1 = gear_needed[place].split(', ')
# 		for k in range(0,len(split1)):
# 			gear_list.append(split1[k])
# 	gear={}
# 	for i in range(0,len(gear_list)):
# 		gear[gear_list[i]]=1

# 	for i in range(0,len(toon)):
# 		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 		place = place[0]
# 		list=gear_needed[place].split(', ')
# 		number=number_needed[place].split(', ')
# 		for j in range(0,len(list)):
# 			if gear[list[j]] == 1:
# 				gear[list[j]] = []
# 				for r in range(0,int(number[j])):
# 					gear[list[j]].append(toon[i])
# 			else:
# 				for r in range(0,int(number[j])):
# 					gear[list[j]].append(toon[i])
# 	printable=[]
# 	for key,value in gear.items():
# 		#if len(value) > 2:
# 		#if key == 'Mk 3 Sienar Holo Projector' or key == 'Mk 5 CEC Fusion Furnace' or key == 'Mk 7 TaggeCo Holo Lens':
# 		printable.append(str(len(value))+":   "+key+": "+str(value).replace('[','').replace(']','').replace("'",'')+"\n\n")

# 	body = "".join(sorted(printable,reverse=True))

# 	# Record the MIME type
# 	email_body = MIMEText(body, 'plain')

# 	# Attach body into message container.
# 	msg.attach(email_body)

# 	# Send the message via local SMTP server.
# 	server = smtplib.SMTP('smtp.gmail.com:587')
# 	server.ehlo()
# 	server.starttls()
# 	server.ehlo()
# 	server.login('rcburky@gmail.com','')
# 	# sendmail function takes 3 arguments: sender's address, recipient's address
# 	# and message to send - here it is sent as one string.
# 	server.sendmail(sender, recipient, msg.as_string())
# 	server.quit()

# def levelsearch_all():
# 	#opens and reads all files created by starwars.py and creates other variables that are needed
# 	toons = open('Data/toons.txt','r')
# 	toons = map(str.strip,toons.readlines())
# 	levels = open('Data/levels.txt','r')
# 	levels = map(str.strip,levels.readlines())
# 	gear_level = open('Data/gear_level.txt','r')
# 	gear_level = map(str.strip,gear_level.readlines())
# 	stars = open('Data/stars.txt','r')
# 	stars = map(str.strip,stars.readlines())
# 	gear_needed = open('Data/gear_needed.txt','r')
# 	gear_needed = map(str.strip,gear_needed.readlines())
# 	number_needed = open('Data/number_needed.txt','r')
# 	number_needed = map(str.strip,number_needed.readlines())
# 	locked=[]
# 	final={}
# 	gear_list=list()
# 	number_list=list()
# 	toon=toons

# 	#adds individual characters gear to list of gear needed
# 	for i in range(0,len(toons)):
# 		split1 = gear_needed[i].split(', ')
# 		split2 = number_needed[i].split(', ')
# 		gear_list.append(split1)
# 		number_list.append(split2)

# 	#creates the team's gear dictionary	
# 	for i in range(0,len(toon)):
# 		try:
# 			place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 			place = place[0]
# 		except IndexError:
# 			continue
# 		for j in range(0,len(gear_list[place])):
# 			final[gear_list[place][j]]=0

# 	#Creates an entry into the gear dictionary for each character, if character has been unlocked
# 	for i in range(0,len(toon)):
# 		try:
# 			place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
# 			place = place[0]
# 		except IndexError:
# 			locked.append(toon[i])
# 			continue
# 		for j in range(0,len(gear_list[place])):
# 			try:
# 				final[gear_list[place][j]]+=int(number_list[place][j])
# 			except:
# 				pass

# 		f=open('Data/output.csv','r')
# 		file=f.readlines()
# 		f.close()

# 		part1=[]
# 		for i in range(0,len(file)):
# 			part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))

# 		gear={}
# 		for i in range(0,len(part1)):
# 			mats={}
# 			for j in range(1,len(part1[i])-1,2):
# 				mats[part1[i][j]]=int(part1[i][j+1])
# 			gear[part1[i][0]]=mats

# 		team_gear2={}
# 		for key,val in final.items():
# 			try:
# 				for keys,vals in gear[key].items():
# 					try:
# 						team_gear2[keys]=team_gear2[keys]+(vals*val)
# 					except KeyError:
# 						team_gear2[keys]=vals*val
# 			except:
# 				pass

# 	#creates printable list of all the farmable gear needed
# 	input_list=[]
# 	sorted_team_gear2 = sorted(team_gear2.items(), key=operator.itemgetter(1),reverse=True)
# 	for i in range(0,len(sorted_team_gear2)):
# 		input_list.append(sorted_team_gear2[i][0]+","+str(sorted_team_gear2[i][1]))

# 	full_list=[]
# 	sorted_final = sorted(final.items(), key=operator.itemgetter(1),reverse=True)
# 	for i in range(0,len(sorted_final)):
# 		full_list.append(sorted_final[i][0]+","+str(sorted_final[i][1]))

# 	full_list.pop(len(full_list)-1)
# 	return input_list

# def levelsearch_team():
#     #which toons are wanted
#     #toon=['Wedge Antilles','Princess Leia','Biggs Darklighter','Stormtrooper Han','Lando Calrissian','CT-5555 "Fives"','Rey','Jedi Knight Anakin','Captain Phasma','Teebo','Ewok Elder','Qui-Gon Jinn','HK-47','IG-88','IG-86 Sentinel Droid','Jawa Engineer','Chief Nebit','Chief Chirpa','Clone Sergeant - Phase I']
#     toon=['TIE Fighter Pilot','Clone Sergeant - Phase I','Boba Fett','Dengar']
#     #toon=['Ima-Gun Di']
#     #opens and reads all files created by starwars.py and creates other variables that are needed
#     toons = open('Data/toons.txt','r')
#     toons = map(str.strip,toons.readlines())
#     levels = open('Data/levels.txt','r')
#     levels = map(str.strip,levels.readlines())
#     gear_level = open('Data/gear_level.txt','r')
#     gear_level = map(str.strip,gear_level.readlines())
#     stars = open('Data/stars.txt','r')
#     stars = map(str.strip,stars.readlines())
#     gear_needed = open('Data/gear_needed.txt','r')
#     gear_needed = map(str.strip,gear_needed.readlines())
#     number_needed = open('Data/number_needed.txt','r')
#     number_needed = map(str.strip,number_needed.readlines())
#     locked=[]
#     final={}
#     gear_list=list()
#     number_list=list()
    
#     #adds individual characters gear to list of gear needed
#     for i in range(0,len(toons)):
#     	split1 = gear_needed[i].split(', ')
#     	split2 = number_needed[i].split(', ')
#     	gear_list.append(split1)
#     	number_list.append(split2)
#     #creates the team's gear dictionary	
#     for i in range(0,len(toon)):
#     	try:
#     		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
#     		place = place[0]
#     	except IndexError:
#     		continue
#     	for j in range(0,len(gear_list[place])):
#     		final[gear_list[place][j]]=0
    
#     #Creates an entry into the gear dictionary for each character, if character has been unlocked
#     for i in range(0,len(toon)):
#     	try:
#     		place=[j for j,x in enumerate(toons) if x == "%s" % toon[i]]
#     		place = place[0]
#     	except IndexError:
#     		locked.append(toon[i])
#     		continue
#     	for j in range(0,len(gear_list[place])):
#     		final[gear_list[place][j]]+=int(number_list[place][j])
#     	f=open('Data/output.csv','r')
#     	file=f.readlines()
#     	f.close()
    
#     	part1=[]
#     	for i in range(0,len(file)):
#     		part1.append(file[i].replace("u'",'').replace("'",'').replace('\r\n','').replace('"','').replace('}','').replace(',{',',').replace(': ',',').replace(', ',',').split(','))
#     	gear={}
#     	for i in range(0,len(part1)):
#     		mats={}
#     		for j in range(1,len(part1[i])-1,2):
#     			mats[part1[i][j]]=int(part1[i][j+1])
#     		gear[part1[i][0]]=mats
#     	team_gear2={}
#     	for key,val in final.items():
#     		for keys,vals in gear[key].items():
#     			try:
#     				team_gear2[keys]=team_gear2[keys]+(vals*val)
#     			except KeyError:
#     				team_gear2[keys]=vals*val
    
#     #creates printable list of all the farmable gear needed
#     global input_list
#     input_list=[]
#     sorted_team_gear2 = sorted(team_gear2.items(), key=operator.itemgetter(1),reverse=True)
#     for i in range(0,len(sorted_team_gear2)):
#     	input_list.append(sorted_team_gear2[i][0])
    
#     global num_list
#     num_list=[]
#     sorted_team_gear2 = sorted(team_gear2.items(), key=operator.itemgetter(1),reverse=True)
#     for i in range(0,len(sorted_team_gear2)):
#     	num_list.append(str(sorted_team_gear2[i][1]))

# def level_rec():
#     url = 'https://swgoh.gg/db/missions/lightside/'

#     # Start a session so we can have persistant cookies
#     session = requests.session()
    
#     # Try accessing a page that requires you to be logged in
#     r = session.get(url)
    
#     collection = BeautifulSoup(r.text,'html.parser')
#     lightlevels = collection.find_all('div','media-heading')
#     lightlevels = [level.h4.text for level in lightlevels]
#     lightrewards = collection.find_all('li','media list-group-item p-a')
#     lightrewards = [re.find_all('div','loot-item \
#         loot-gear \
#         \
#         \
#         ') for re in lightrewards]
#     lightrewards = [[re.span.img.get('alt') for re in x] for x in lightrewards]
    
#     durl = 'https://swgoh.gg/db/missions/darkside/'
#     rx = session.get(durl)
    
#     dcollection = BeautifulSoup(rx.text,'html.parser')
#     darklevels = collection.find_all('div','media-heading')
#     darklevels = [level.h4.text for level in darklevels]
#     darkrewards = dcollection.find_all('li','media list-group-item p-a')
#     darkrewards = [re.find_all('div','loot-item \
#         loot-gear \
#         \
#         \
#         ') for re in darkrewards]
#     darkrewards = [[re.span.img.get('alt') for re in x] for x in darkrewards]
#     levelsearch_team()
    
#     items = input_list
#     itemnum = num_list
#     remove_list=['Mk 8 BioTech Implant Salvage','Mk 8 BioTech Implant Component','Mk 6 Nubian Design Tech Salvage','Mk 7 Nubian Security Scanner Salvage','Mk 5 Arakyd Droid Caller Salvage','Mk 5 CEC Fusion Furnace Salvage','Mk 3 Zaltin Bacta Gel Salvage','Mk 6 CEC Fusion Furnace Salvage','Mk 6 Merr-Sonn Thermal Detonator Prototype Salvage','Mk 4 Sienar Holo Projector Salvage','Mk 10 TaggeCo Holo Lens Salvage','Mk 11 BlasTech Weapon Mod Salvage']
    
#     for i in range(0,len(remove_list)):
#         try:
#             place=[j for j,x in enumerate(items) if x == "%s" % remove_list[i]]
#             itemnum.pop(int(place[0]))
#             items.remove(remove_list[i])
#         except:
#             pass
    
        
#     lightrec = {}
#     for i in range(0,len(lightrewards)):
#         lightrec[lightlevels[i]] = 0
#         for j in range(0,len(items)):
#             if 'Hard' in lightlevels[i]:
#                 pass
#             else:
#                 if items[j] in lightrewards[i]:
#                         lightrec[lightlevels[i]] = lightrec[lightlevels[i]] + float(float(itemnum[j])/float(itemnum[0]))*100
#                 else:
#                     pass
#     lightcount=[]
#     for key,value in lightrec.items():
#         if value == lightrec[max(lightrec.iterkeys(), key=(lambda key: lightrec[key]))]:
#             lightcount.append(key)
            
#     darkrec = {}
#     for i in range(0,len(darkrewards)):
#         darkrec[darklevels[i]] = 0
#         for j in range(0,len(items)):
#             if 'Hard' in darklevels[i]:
#                 pass
#             else:
#                 if items[j] in darkrewards[i]:
#                         darkrec[darklevels[i]] = darkrec[darklevels[i]] + float(float(itemnum[j])/float(itemnum[0]))*100
#                 else:
#                     pass
#     darkcount=[]
#     for key,value in darkrec.items():
#         if value == darkrec[max(darkrec.iterkeys(), key=(lambda key: darkrec[key]))]:
#             darkcount.append(key)
#     print(lightcount)
#     print(darkcount)

# def item_rec(need):
    
#     url = 'https://swgoh.gg/db/missions/lightside/'
    
#     # Start a session so we can have persistant cookies
#     session = requests.session()
    
#     # Try accessing a page that requires you to be logged in
#     r = session.get(url)
    
#     collection = BeautifulSoup(r.text,'html.parser')
#     lightlevels = collection.find_all('div','media-heading')
#     lightlevels = [level.h4.text for level in lightlevels]
#     lightrewards = collection.find_all('li','media list-group-item p-a')
#     lightrewards = [re.find_all('div','loot-item \
#         loot-gear \
#         \
#         \
#         ') for re in lightrewards]
#     lightrewards = [[re.span.img.get('alt') for re in x] for x in lightrewards]
    
#     durl = 'https://swgoh.gg/db/missions/darkside/'
#     rx = session.get(durl)
    
#     dcollection = BeautifulSoup(rx.text,'html.parser')
#     darklevels = collection.find_all('div','media-heading')
#     darklevels = [level.h4.text for level in darklevels]
#     darkrewards = dcollection.find_all('li','media list-group-item p-a')
#     darkrewards = [re.find_all('div','loot-item \
#         loot-gear \
#         \
#         \
#         ') for re in darkrewards]
#     darkrewards = [[re.span.img.get('alt') for re in x] for x in darkrewards]
#     levelsearch_team()
    
#     items = input_list
#     itemnum = num_list
#     remove_list=[]
    
#     for i in range(0,len(remove_list)):
#         try:
#             place=[j for j,x in enumerate(items) if x == "%s" % remove_list[i]]
#             itemnum.pop(int(place[0]))
#             items.remove(remove_list[i])
#         except:
#             pass
    
        
#     lightrec = {}
#     for i in range(0,len(lightrewards)):
#         lightrec[lightlevels[i]] = 0
#         for j in range(0,len(items)):
#             if 'Hard' in lightlevels[i]:
#                 pass
#             else:
#                 if items[j] in lightrewards[i]:
#                     lightrec[lightlevels[i]] = lightrec[lightlevels[i]] + float(float(itemnum[j])/float(itemnum[0]))*100
#                 else:
#                     pass
#                 if items[j] in lightrewards[i] and items[j] == need:
#                     lightrec[lightlevels[i]] = lightrec[lightlevels[i]] + float(float(itemnum[j])/float(itemnum[0]))*100 + 200                    
#                 else:                    
#                     pass
#     lightcount=[]
#     for key,value in lightrec.items():
#         if value == lightrec[max(lightrec.iterkeys(), key=(lambda key: lightrec[key]))]:
#             lightcount.append(key)
            
#     darkrec = {}
#     for i in range(0,len(darkrewards)):
#         darkrec[darklevels[i]] = 0
#         for j in range(0,len(items)):
#             if 'Hard' in darklevels[i]:
#                 pass
#             else:
#                 if items[j] in darkrewards[i]:
#                     darkrec[darklevels[i]] = darkrec[darklevels[i]] + float(float(itemnum[j])/float(itemnum[0]))*100
#                 else:
#                     pass
#                 if items[j] in darkrewards[i] and items[j] == need:
#                     darkrec[darklevels[i]] = darkrec[darklevels[i]] + float(float(itemnum[j])/float(itemnum[0]))*100 + 200                    
#                 else:                    
#                     pass
#     darkcount=[]
#     for key,value in darkrec.items():
#         if value == darkrec[max(darkrec.iterkeys(), key=(lambda key: darkrec[key]))]:
#             darkcount.append(key)
#     print(lightcount)
#     print(darkcount)
