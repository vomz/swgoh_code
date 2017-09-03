import requests
import operator
import smtplib
from bs4 import BeautifulSoup




#which toons are wanted
#toon=['Ahsoka Tano (Fulcrum)','Hera Syndulla','Ezra Bridger','Sabine Wren','Garazeb "Zeb" Orrelios','Kanan Jarrus','Jyn Erso','Cassian Andor','K-2SO','Chirrut Imwe','Baze Malbus']
toon=['Ahsoka Tano (Fulcrum)','CC-2224 "Cody"','CT-21-0408 "Echo"','CT-5555 "Fives"','CT-7567 "Rex"','Clone Sergeant - Phase I']
#'Ahsoka Tano (Fulcrum)','Jyn Erso','Cassian Andor','K-2SO','Chirrut Imwe'
#opens and reads all files created by starwars.py and creates other variables that are needed
#'Hera Syndulla','Ezra Bridger','Sabine Wren','Garazeb "Zeb" Orrelios','Kanan Jarrus'
toons = open('Data/toons.txt','r')
toons = map(str.strip,toons.readlines())
#levels = open('Data/levels.txt','r')
#levels = map(str.strip,levels.readlines())
#gear_level = open('Data/gear_level.txt','r')
#gear_level = map(str.strip,gear_level.readlines())
#stars = open('Data/stars.txt','r')
#stars = map(str.strip,stars.readlines())
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

    f=open('output.csv','r')
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
        try:
            for keys,vals in gear[key].items():
                try:
                    team_gear2[keys]=team_gear2[keys]+(vals*val)
                except KeyError:
                    team_gear2[keys]=vals*val
        except:
            pass
    delta={}
    for k in range(0,len(toon)):
        g=[]
        try:
            place=[j for j,x in enumerate(toons) if x == "%s" % toon[k]]
            place = place[0]
        except:
            print toon[k]+' is not unlocked...'
            break
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


print body

