from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Start a session
session = requests.session()

# Try accessing a page that requires you to be logged in
r = session.get('https://swgoh.gg/db/gear/')

# Translate the web page for use in BeautifulSoup
collection = BeautifulSoup(r.text,'html.parser')
gear=collection.find_all("div","col-md-4 gear")
small = re.compile('.*gear-icon-small.*')

links=[]
for i in gear:
    links.append(i.a.get('href'))

links.append(collection.find_all('a',{'class':'gear-tooltip g12-finisher__character','data-character':'ARC Trooper'})[0].get('href'))
links.append(collection.find_all('a',{'class':'gear-tooltip g12-finisher__character','data-character':'Admiral Ackbar'})[0].get('href'))
links.append(collection.find_all('a',{'class':'gear-tooltip g12-finisher__character','data-character':'Ahsoka Tano'})[0].get('href'))
    
material_dict={}


for i in range(0,len(links)):
    page=session.get('https://swgoh.gg'+links[i])
    piece=BeautifulSoup(page.text,'html.parser')
    if 'materials' in piece.find_all('h4','m-a-0')[0].text.lower():
        if piece.find_all('div','pull-left')[0].img.get('alt')=='Power Cell Injector (Ionic) - Ahsoka Tano':
            label='Power Cell Injector (Ionic)'
        elif piece.find_all('div','pull-left')[0].img.get('alt')=='Power Cell Injector (Fusion) - Admiral Ackbar':
            label='Power Cell Injector (Fusion)'
        elif piece.find_all('div','pull-left')[0].img.get('alt')=='Power Cell Injector (Plasma) - ARC Trooper':
            label='Power Cell Injector (Plasma)'
        else:
            label=piece.find_all('div','pull-left')[0].img.get('alt')
            
        material_dict[label]={}
        mats=piece.find_all('li','media list-group-item p-0')
        for j in mats:
            if len(j.find_all('span',small))>0:
                mult=int(j.div.text.split('x')[0])
                submats=j.find_all('span',small)
                amts=j.p.text.split('\n')
                amts=[int(a.split('x')[0]) for a in amts if 'x' in a]
                for k in range(0,len(submats)):
                    material_dict[label][submats[k].get('title')]=mult*amts[k]
            else:
                try:
                    mult=int(j.div.text.split('x')[0])
                    material_dict[label][j.a.get('title')]=mult*1
                except:
                    continue

dmats = pd.DataFrame(data=material_dict)
# for i in material_dict:
#     for j in material_dict[i]:
#         print(i+":"+j+":"+str(material_dict[i][j]))