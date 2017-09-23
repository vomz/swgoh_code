import requests
from bs4 import BeautifulSoup
import time

def starcount(starlist):
    x=[]
    for i in starlist:
        if 'star' in i.get('class') and 'star-inactive' in i.get('class'):
            pass
        elif 'star' in i.get('class') and 'star-inactive' not in i.get('class'):
            x.append(i.get('class'))
        else:
            pass
    y=[]
    for j in x:
                for k in j:
                    if k == 'star':
                        pass
                    else:
                        y.append(int(k.split('star')[1]))
    return max(y)   

#Record beginning time
start_time = time.time()

# Start a session
session = requests.session()

front = session.get('https://swgoh.gg/')
collection = BeautifulSoup(front.text,'html.parser')
names=collection.find_all("li","media list-group-item p-0 character")

linkx = []
for i in range(0,len(names)):
    if 'Chirrut' in names[i].img.get('alt'):
        linkx.append('Chirrut Imwe')
    else:
        linkx.append(names[i].img.get('alt'))

sfront=session.get('https://swgoh.gg/ships')
collection = BeautifulSoup(sfront.text,'html.parser')
names=collection.find_all("h5")
names.pop(0)
for i in names:
    linkx.append(i.text)


dicti={key:[] for key in linkx}
    
file = open('csv\\guildstars.txt','w')
file2 = open('csv\\guildgearlevel.txt','w')
file.write('Member,')
file2.write('Member,')
for k in linkx:
    if 'Chirrut' in k:
        file.write('Chirrut Imwe,')
        file2.write('Chirrut Imwe,')
    else:
        file.write(k+',')
        file2.write(k+',')
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
    
    
    r = session.get('https://swgoh.gg'+q+'collection')
    # Translate the web page for use in BeautifulSoup
    collection = BeautifulSoup(r.text,'html.parser')
    mem = collection.find_all('a','no-decoration char-name')[1].text    
    
    print 'Collecting '+mem+'\'s characters.......'

    #Define needed lists 
    toons=[]
    gear_level=[]
    stars=[]
    gp=[]

    
    toonlist = collection.find_all('div','col-xs-6 col-sm-3 col-md-3 col-lg-2')
    for i in toonlist:
        starobj=[]
        if 'characters' in i.div.div.a.get('href'):
            pass
        else:
            if 'Chirrut' in i.div.div.img.get('alt'):
                toons.append('Chirrut Imwe')
                dicti['Chirrut Imwe'].append(mem)
                gear_level.append(i.div.div.find_all('div','char-portrait-full-gear-level')[0].text)
                stars.append(starcount(i.div.div.find_all('div')))

                    
            else:
                toons.append(i.div.div.img.get('alt'))
                dicti[i.div.div.img.get('alt')].append(mem)
                gear_level.append(i.div.div.find_all('div','char-portrait-full-gear-level')[0].text)
                stars.append(starcount(i.div.div.find_all('div')))
 



   
    
    r = session.get('https://swgoh.gg'+q+'ships')
    # Translate the web page for use in BeautifulSoup
    collection = BeautifulSoup(r.text,'html.parser')
    ship_names=[]
    ship_stars=[]
    ships = collection.find_all('div','col-sm-6 col-md-6 col-lg-4')
    for i in ships:
        ship_names.append(i.find('a','collection-ship-name-link').text)
        #print i.find('a','collection-ship-name-link').text
        dicti[i.find('a','collection-ship-name-link').text].append(mem)
        if 'collection-ship-missing' in i.div.get('class'):
            ship_stars.append('0')
            #print '0'
        else:
            ship_stars.append(7-len(i.find_all('div','ship-portrait-full-star  ship-portrait-full-star-inactive')))
            #print 7-len(i.find_all('div','ship-portrait-full-star  ship-portrait-full-star-inactive'))
    # Write gear and other information to text files
    print 'Writing data.......'
    

    file=open('csv\\guildstars.txt','a+')
    file2=open('csv\\guildgearlevel.txt','a+')
    file.write(mem+',')
    file2.write(mem+',')
    for j in linkx:
        if mem in dicti[j]:
            try:
                place = [q for q,ax in enumerate(toons) if ax == j]
                place=place[0]
                #print j+str(stars[place])
                file.write(str(stars[place])+',')
                file2.write(str(gear_level[place])+',')
            except:
                place = [q for q,ax in enumerate(ship_names) if ax == j]
                place=place[0]
                #print j+str(ship_stars[place])
                file.write(str(ship_stars[place])+',')
                

        else:
            file.write(',')
            file2.write(',')
    file.write('\n')
    file2.write('\n')
    file.close()
    file2.close()







        
        


# print length the file took to run
print("--- %s seconds ---" % (time.time() - start_time))