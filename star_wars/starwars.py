import requests
from bs4 import BeautifulSoup
import time

#Record beginning time
start_time = time.time()

# Start a session
session = requests.session()

# Try accessing a page that requires you to be logged in
r = session.get('https://swgoh.gg/u/vomz/collection')

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

	# gear needed and number of gear needed
	numneed=[]
	gearneed=[]		
	for j in range(0,len(character.find_all('div','pc-needed-gear-preview'))):
		gearneed.append(character.find_all('div','pc-needed-gear-preview')[j].span.get('title'))
		numneed.append(character.find_all('div','pc-needed-gear-count')[j].text)
	gear_needed.append(gearneed)
	number_needed.append(numneed)

	# close session
	page=page.close()

# Write gear and other information to text files
print 'Writing data.......'

file = open('Data/toons.txt','w')
for i in range(0,len(toons)):
	file.write(toons[i]+"\n")
file.close()

file = open('Data/gear_needed.txt','w')
for i in range(0,len(gear_needed)):
	if len(gear_needed[i])==0:
			file.write("\n")
	for j in range(0,len(gear_needed[i])):
		if j == len(gear_needed[i])-1:
			file.write(gear_needed[i][j]+"\n")
		else:
			file.write(gear_needed[i][j]+", ")
file.close()

file = open('Data/number_needed.txt','w')
for i in range(0,len(number_needed)):
	if len(number_needed[i])==0:
			file.write("None\n")
	for j in range(0,len(number_needed[i])):
		if j == len(number_needed[i])-1:
			file.write(number_needed[i][j]+"\n")
		else:
			file.write(number_needed[i][j]+", ")
file.close()



# # Collection of Mod data
# print 'Writing mod data.......'
# lookup = {'I':'1','II':'2','III':'3','IV':'4','V':'5'}

# # Try accessing a page that requires you to be logged in
# num = session.get('https://swgoh.gg/u/vomz/mods/')
# num = BeautifulSoup(num.text,'html.parser')
# page = num.find_all('ul','pagination m-t-0')[0].li.a.text[-1:]

# filex=open('data/mods.txt','w')

# # Collection of mod data for each character
# for i in range(1,int(page)+1):
#     mods=session.get('https://swgoh.gg/u/vomz/mods/?page='+str(i))
#     mods=BeautifulSoup(mods.text,'html.parser')
#     mod_data = mods.find_all('div','collection-mod')
#     for j in mod_data:
#         mod_level = j.find_all('span','statmod-level')[0].text        
        
#         if mod_level != '15':
#         	continue
#         else:

# 	        mod_sum = j.find_all('img','statmod-img')[0].get('alt')
# 	        mod_pip = lookup[mod_sum.split(' ')[1][0:1]]
# 	        mod_group = mod_sum.split(' ')[2]
# 	        mod_slot = mod_sum.split(' ')[-1]

# 	        main_stat_value = j.find_all('span','statmod-stat-value')[0].text[1:]
# 	        main_stat_text = j.find_all('span','statmod-stat-label')[0].text
# 	        try:
# 	            secondary_stat_1_text = j.find_all('span','statmod-stat-label')[1].text
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_2_text = j.find_all('span','statmod-stat-label')[2].text
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_3_text = j.find_all('span','statmod-stat-label')[3].text
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_4_text = j.find_all('span','statmod-stat-label')[4].text
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_1_value = j.find_all('span','statmod-stat-value')[1].text[1:]
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_2_value = j.find_all('span','statmod-stat-value')[2].text[1:]
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_3_value = j.find_all('span','statmod-stat-value')[3].text[1:]
# 	        except:
# 	            pass
# 	        try:
# 	            secondary_stat_4_value = j.find_all('span','statmod-stat-value')[4].text[1:]
# 	        except:
# 	            pass
	        
# 	        filex.write(mod_level+','+mod_pip+','+mod_group+','+mod_slot+','+main_stat_value+','+main_stat_text+','+secondary_stat_1_text+','+secondary_stat_2_text+','+secondary_stat_3_text+','+secondary_stat_4_text+','+secondary_stat_1_value+','+secondary_stat_2_value+','+secondary_stat_3_value+','+secondary_stat_4_value+'\n')
	        
# filex.close()

# print length the file took to run
print("--- %s seconds ---" % (time.time() - start_time))