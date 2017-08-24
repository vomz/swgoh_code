import requests
from bs4 import BeautifulSoup
import time

#Record beginning time
start_time = time.time()

# Start a session
session = requests.session()

#Collect guild members
x=session.get('https://swgoh.gg/g/602/empire-of-heroes/')

mlist = BeautifulSoup(x.text,'html.parser')

mlist2=mlist.find_all('td','footable-first-visible')

members=[]
for i in mlist2:
    members.append(i.a.get('href'))

for q in members:
    mem = q.split('/')[2]
    
    # Try accessing a page that requires you to be logged in
    r = session.get('https://swgoh.gg'+q+'collection')
    
    # Translate the web page for use in BeautifulSoup
    collection = BeautifulSoup(r.text,'html.parser')
    
    print 'Collecting characters.......'
    # collect and organize the characters that are unlocked
    toons=collection.find_all("div","col-xs-6 col-sm-3 col-md-3 col-lg-2")
    missing_light = len(collection.find_all("div","collection-char collection-char-missing collection-char-light-side"))
    missing_dark = len(collection.find_all("div","collection-char collection-char-missing collection-char-dark-side"))
    num_chars = len(toons) - missing_dark - missing_light
    
    # Create links for each character unlocked
    links = []
    for i in range(0,num_chars):
    	links.append(toons[i].find_all('a','char-portrait-full-link')[0].get('href'))
    
    # Define needed lists 
    toons=[]
    levels=[]
    gear_level=[]
    gear_needed=[]
    number_needed=[]
    stars=[]
    skills=[]
    skill_levels=[]
    category=[]
    
    print 'Gathering character data.......'
    
    # Collect information about each of the characters 
    for i in range(0,len(links)):
    	page=session.get('https://swgoh.gg/'+links[i])
    	character=BeautifulSoup(page.text,'html.parser')
    
    	# name
    	if 'Chirrut' in character.find_all('a','pc-char-overview-name')[0].text:
    		toons.append('Chirrut Imwe')
    	else:
    		toons.append(character.find_all('a','pc-char-overview-name')[0].text)
    
    # Write gear and other information to text files
    print 'Writing data.......'
    
    file = open('Data/guildtoons.txt','a+')
    file.write(mem+',')
    for i in range(0,len(toons)):
    	file.write(toons[i]+",")
    file.write('\n')
    file.close()
 
#    file = open('Data/guildstars.txt','a+')
#    file.write(mem+',')
#    for i in range(0,len(stars)):
#    	file.write(toons[i]+",")
#    file.write('\n')
#    file.close()

# print length the file took to run
print("--- %s seconds ---" % (time.time() - start_time))