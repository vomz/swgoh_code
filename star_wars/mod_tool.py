import requests
from bs4 import BeautifulSoup
import time
import sys
start_time = time.time()
# Start a session so we can have persistant cookies
session = requests.session()
sys.exit()
filex=open('data/mods.txt','w')

lookup = {'I':'1','II':'2','III':'3','IV':'4','V':'5'}

# Try accessing a page that requires you to be logged in
num = session.get('https://swgoh.gg/u/vomz/mods/')
num = BeautifulSoup(num.text,'html.parser')
page = num.find_all('ul','pagination m-t-0')[0].li.a.text[-1:]

for i in range(1,int(page)+1):
    mods=session.get('https://swgoh.gg/u/vomz/mods/?page='+str(i))
    mods=BeautifulSoup(mods.text,'html.parser')
    mod_data = mods.find_all('div','collection-mod')
    for j in mod_data:
        mod_level = j.find_all('span','statmod-level')[0].text        
        
        mod_sum = j.find_all('img','statmod-img')[0].get('alt')
        mod_pip = lookup[mod_sum.split(' ')[1][0:1]]
        if 'Critical Damage' in mod_sum:
            mod_group = 'Critical Damage'
        if 'Critical Chance' in mod_sum:
            mod_group = 'Critical Chance'
        else:
            mod_group = mod_sum.split(' ')[2]
        mod_slot = mod_sum.split(' ')[-1]

        main_stat_value = j.find_all('span','statmod-stat-value')[0].text[1:]
        main_stat_text = j.find_all('span','statmod-stat-label')[0].text

      
        
        try:
            secondary_stat_1_text = j.find_all('span','statmod-stat-label')[1].text
        except:
            secondary_stat_1_text = ''
        try:
            secondary_stat_2_text = j.find_all('span','statmod-stat-label')[2].text
        except:
            secondary_stat_2_text = ''
        try:
            secondary_stat_3_text = j.find_all('span','statmod-stat-label')[3].text
        except:
            secondary_stat_3_text = ''
        try:
            secondary_stat_4_text = j.find_all('span','statmod-stat-label')[4].text
        except:
            secondary_stat_4_text = ''
        try:
            secondary_stat_1_value = j.find_all('span','statmod-stat-value')[1].text[1:]
        except:
            secondary_stat_1_value = ''
        try:
            secondary_stat_2_value = j.find_all('span','statmod-stat-value')[2].text[1:]
        except:
            secondary_stat_2_value = ''
        try:
            secondary_stat_3_value = j.find_all('span','statmod-stat-value')[3].text[1:]
        except:
            secondary_stat_3_value = ''
        try:
            secondary_stat_4_value = j.find_all('span','statmod-stat-value')[4].text[1:]
        except:
            secondary_stat_4_value = ''
        
        filex.write(mod_level+','+mod_pip+','+mod_group+','+mod_slot+','+main_stat_value+','+main_stat_text+','+secondary_stat_1_text+','+secondary_stat_2_text+','+secondary_stat_3_text+','+secondary_stat_4_text+','+secondary_stat_1_value+','+secondary_stat_2_value+','+secondary_stat_3_value+','+secondary_stat_4_value+'\n')
        