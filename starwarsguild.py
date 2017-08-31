import requests
from bs4 import BeautifulSoup
import time

#Record beginning time
start_time = time.time()

# Start a session
session = requests.session()

front = session.get('https://swgoh.gg/')
collection = BeautifulSoup(front.text,'html.parser')
names=collection.find_all("li","media list-group-item p-0 character")

toons=[]

linkx = []
for i in range(0,len(names)):
    if 'Chirrut' in names[i].img.get('alt'):
        linkx.append('Chirrut Imwe')
    else:
        linkx.append(names[i].img.get('alt'))

dicti={key:[] for key in linkx}
    
file = open('C:\\Users\\ryanc\\Google Drive\\Coding\\Projects\\star_wars\\data\\guildstars.txt','w')
file2 = open('C:\\Users\\ryanc\\Google Drive\\Coding\\Projects\\star_wars\\data\\guildgearlevel.txt','w')
file.write(',')
file2.write(',')
for i in linkx:
    if 'Chirrut' in i:
        file.write('Chirrut Imwe,')
        file2.write('Chirrut Imwe,')
    else:
        file.write(i+',')
        file2.write(i+',')
file.write('\n')
file2.write('\n')
file.close()
file2.close()
#Collect guild members
x=session.get('https://swgoh.gg/g/602/empire-of-heroes/')

mlist = BeautifulSoup(x.text,'html.parser')

mlist2=mlist.find_all('td')

mlist3=[]

for i in mlist2:
    if i.a:
        mlist3.append(i.a.get('href'))
    else:
        pass

members=[]
for i in mlist2:
    if i.a:
        members.append(i.a.strong.text)
    else:
        pass
#mlist3=['/u/vomz/']
for q in mlist3:
    mem = q.split('/')[2]
    
    r = session.get('https://swgoh.gg'+q+'collection')
        
    # Translate the web page for use in BeautifulSoup
    collection = BeautifulSoup(r.text,'html.parser')
    
    print 'Collecting '+mem+'\'s characters.......'
    # collect and organize the characters that are unlocked
    toons=collection.find_all("div","col-xs-6 col-sm-3 col-md-3 col-lg-2")
    missing_light = len(collection.find_all("div","collection-char collection-char-missing collection-char-light-side"))
    missing_dark = len(collection.find_all("div","collection-char collection-char-missing collection-char-dark-side"))
    num_chars = len(toons) - missing_dark - missing_light
    
    # Create links for each character unlocked
    links = []
    for i in range(0,num_chars):
        links.append(toons[i].find_all('a','char-portrait-full-link')[0].get('href'))
        try:
            if 'Chirrut' in toons[i].find_all('a','char-portrait-full-link')[0].img.get('alt'):
                dicti['Chirrut Imwe'].append(mem)
            else:
                dicti[toons[i].find_all('a','char-portrait-full-link')[0].img.get('alt')].append(mem)
        except:
            pass
    
    #Define needed lists 
    toons=[]
    levels=[]
    gear_level=[]
    gear_needed=[]
    number_needed=[]
    stars=[]
    skills=[]
    skill_levels=[]
    category=[]
    
    print 'Gathering '+mem+'\'s character data.......'
    
    # Collect information about each of the characters 
    for i in range(0,len(links)):
        page=session.get('https://swgoh.gg/'+links[i])
        character=BeautifulSoup(page.text,'html.parser')
        gear_level.append(character.find_all('div','pc-heading')[0].text)
        # name
        if 'Chirrut' in character.find_all('a','pc-char-overview-name')[0].text:
            toons.append('Chirrut Imwe')
        else:
            toons.append(character.find_all('a','pc-char-overview-name')[0].text)
        
        if len(character.find_all('div','star star7'))>0:
            stars.append('7')
        else:
            if len(character.find_all('div','star star6'))>0:
                stars.append('6')
            else:
                if len(character.find_all('div','star star5'))>0:
                    stars.append('5')
                else:
                    if len(character.find_all('div','star star4'))>0:
                        stars.append('4')
                    else:
                        if len(character.find_all('div','star star3'))>0:
                            stars.append('3')
                        else:
                            if len(character.find_all('div','star star2'))>0:
                                stars.append('2')
                            else:
                                if len(character.find_all('div','star star1'))>0:
                                    stars.append('1')
            



    # Write gear and other information to text files
    print 'Writing data.......'
    

    file=open('C:\\Users\\ryanc\\Google Drive\\Coding\\Projects\\star_wars\\data\\guildstars.txt','a+')
    file2=open('C:\\Users\\ryanc\\Google Drive\\Coding\\Projects\\star_wars\\data\\guildgearlevel.txt','a+')
    file.write(mem+',')
    file2.write(mem+',')
    for j in linkx:
        if mem in dicti[j]:
            place = [q for q,ax in enumerate(toons) if ax == j]
            place=place[0]
            file.write(str(stars[place])+',')
            file2.write(str(gear_level[place])+',')
        else:
            file.write(',')
            file2.write(',')
    file.write('\n')
    file2.write('\n')
    file.close()
    file2.close()




# print length the file took to run
print("--- %s seconds ---" % (time.time() - start_time))