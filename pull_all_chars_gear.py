from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Start a session
session = requests.session()

# Try accessing a page that requires you to be logged in
site = session.get('https://swgoh.gg/')

# Translate the web page for use in BeautifulSoup
units = BeautifulSoup(site.text,'html.parser')

print('Collecting characters.......')
# collect and organize the characters that are unlocked
chars=units.find_all("li","media list-group-item p-0 character")

characters=[]
for i in chars:
    characters.append(i.find("a").get("href"))


dict={}
    
for i in characters:
    # print('https://swgoh.gg'+i+'gear')
    gear_site=session.get('https://swgoh.gg'+i+'gear')
    gear = BeautifulSoup(gear_site.text,'html.parser')
    dict[gear.h3.text.split(' ·')[0]]={}
    alpha=gear.find('ul','list-group media-list media-list-stream')
    beta=alpha.find_all('li','media list-group-item p-0 character')
    lvl=0
    item=1
    for j in range(0,len(beta)):
            if j//6 == lvl:
                if lvl+1<13:
                    dict[gear.h3.text.split(' ·')[0]][float(str(lvl+1)+'.'+str(item))]=beta[j].a.get('title').split(' - ')[0]
                    item+=1
                else:
                    x=1
            else:
                lvl+=1
                if lvl+1<13:
                    item=1
                    dict[gear.h3.text.split(' ·')[0]][float(str(lvl+1)+'.'+str(item))]=beta[j].a.get('title').split(' - ')[0]
                    item+=1
                else:
                    x=1
            
dfall = pd.DataFrame(data=dict)            
#dfall.to_csv(os.getcwd()+'\\all.csv')