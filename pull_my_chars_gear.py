from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os


# Start a session
session = requests.session()

# Try accessing a page that requires you to be logged in
site = session.get('https://swgoh.gg/p/139697192/characters')

# Translate the web page for use in BeautifulSoup
units = BeautifulSoup(site.text,'html.parser')

print('Collecting characters.......')
# collect and organize the characters that are unlocked
chars=units.find_all("div","col-xs-6 col-sm-3 col-md-3 col-lg-2")

characters=[]
for i in chars:
    characters.append(i.div.a.get('href'))


dict={}
    
for i in characters:
    # print('https://swgoh.gg'+i+'gear')
    gear_site=session.get('https://swgoh.gg'+i)
    gear = BeautifulSoup(gear_site.text,'html.parser')
    dict[gear.h1.a.text.split('\n')[1]]={}
    try:
        level=gear.find('li','media list-group-item').find('div','relic-portrait__tier').text
        dict[gear.h1.a.text.split('\n')[1]]['Relic Level']=gear.find('li','media list-group-item').find('div','relic-portrait__tier').text
        dict[gear.h1.a.text.split('\n')[1]]['Gear Level']=13
        dict[gear.h1.a.text.split('\n')[1]]['Star']=7
        
        categories=[]
        cats=gear.find_all('span','char-category')
        for i in cats:
            categories.append(i.text)
        dict[gear.h1.a.text.split('\n')[1]]['Categories']=categories
    except:
        dict[gear.h1.a.text.split('\n')[1]]['Relic Level']='0'
        dict[gear.h1.a.text.split('\n')[1]]['Gear Level']=int(gear.find('li','media list-group-item').find('div','pc-heading').get('title').split(' ')[1])

        star=re.compile('.*star-inactive.*')
        if int(gear.find('li','media list-group-item').find('div','pc-heading').get('title').split(' ')[1])<12:
            try:
                dict[gear.h1.a.text.split('\n')[1]]['Star']=int(gear.find('div',star).get('class')[1][-1])-1
            except:
                dict[gear.h1.a.text.split('\n')[1]]['Star']=7
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Star']=7
        slot1 = re.compile('.*pc-slot0.*')
        if 'pc-slot-obtained' in gear.find('div',slot1).get('class'):
            dict[gear.h1.a.text.split('\n')[1]]['Gear 1']='Complete'
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Gear 1']=gear.find('div',slot1).img.get('alt')
            
        slot2 = re.compile('.*pc-slot1.*')           
        if 'pc-slot-obtained' in gear.find('div',slot2).get('class'):
            dict[gear.h1.a.text.split('\n')[1]]['Gear 2']='Complete'
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Gear 2']=gear.find('div',slot2).img.get('alt')
            
        slot3 = re.compile('.*pc-slot2.*') 
        if 'pc-slot-obtained' in gear.find('div',slot3).get('class'):
            dict[gear.h1.a.text.split('\n')[1]]['Gear 3']='Complete'
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Gear 3']=gear.find('div',slot3).img.get('alt')
            
        slot4 = re.compile('.*pc-slot3.*')
        if 'pc-slot-obtained' in gear.find('div',slot4).get('class'):
            dict[gear.h1.a.text.split('\n')[1]]['Gear 4']='Complete'
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Gear 4']=gear.find('div',slot4).img.get('alt')

        slot5 = re.compile('.*pc-slot4.*')
        if 'pc-slot-obtained' in gear.find('div',slot5).get('class'):
            dict[gear.h1.a.text.split('\n')[1]]['Gear 5']='Complete'
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Gear 5']=gear.find('div',slot5).img.get('alt')
            
        slot6 = re.compile('.*pc-slot5.*')
        if 'pc-slot-obtained' in gear.find('div',slot6).get('class'):
            dict[gear.h1.a.text.split('\n')[1]]['Gear 6']='Complete'
        else:
            dict[gear.h1.a.text.split('\n')[1]]['Gear 6']=gear.find('div',slot6).img.get('alt')
        
        categories=[]
        cats=gear.find_all('span','char-category')
        for i in cats:
            categories.append(i.text)
        dict[gear.h1.a.text.split('\n')[1]]['Categories']=categories
        
dfmy = pd.DataFrame(data=dict)            
#dfmy.to_csv(os.getcwd()+'\\mine.csv')
