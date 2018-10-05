import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import math
from collections import Counter

set_reqs={'critchance':2, 'tenacity':2, 'health':2, 'speed':4, 'critdamage':4,'potency':2, 'defense':2, 'offense':4}    
set_list=['critchance', 'tenacity', 'health', 'speed', 'critdamage','potency', 'defense', 'offense']
text=open('C:/Users/burkhr/Desktop/mod.txt','r').read()

def create_mod_data(text):
    collection = BeautifulSoup(text,'html.parser')
    collection = collection.find('div')
    
    mods=pd.DataFrame(columns=['pip','shape','set_type','level','primary','secondary1','secondary1_value','secondary2','secondary2_value','secondary3','secondary3_value','secondary4','secondary4_value'])
    count_id=0
    for x in collection:
        pips = len(x.find('span','pips'))
        shape = x.find('img','modImage').get('src').split('/')[-1].split('_')[0]
        set_type = x.find('img','modImage').get('src').split('/')[-1].split('_')[1].split('.')[0].lower()
        level = int(x.find('span','modLevel').text)
        primary = x.find('span','modPrimary').text.split(' ',maxsplit=1)[1].strip().lower()
        try:
            secondary1 = x.find_all('span','modSecondary')[0].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary1_value = float(x.find_all('span','modSecondary')[0].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary1 = 'not upgraded'
            secondary1_value = 0
        try:
            secondary2 = x.find_all('span','modSecondary')[1].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary2_value = float(x.find_all('span','modSecondary')[1].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary2 = 'not upgraded'
            secondary2_value = 0    
        try:
            secondary3 = x.find_all('span','modSecondary')[2].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary3_value = float(x.find_all('span','modSecondary')[2].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary3 = 'not upgraded'
            secondary3_value = 0   
        try:
            secondary4 = x.find_all('span','modSecondary')[3].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary4_value = float(x.find_all('span','modSecondary')[3].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary4 = 'not upgraded'
            secondary4_value = 0
        mod={
             'id':[count_id],
             'pip':[pips],
             'shape':[shape],
             'set_type':[set_type],
             'level':[level],
             'primary':[primary],
             'secondary1':[secondary1],
             'secondary1_value':[secondary1_value],
             'secondary2':[secondary2],
             'secondary2_value':[secondary2_value],
             'secondary3':[secondary3],
             'secondary3_value':[secondary3_value],
             'secondary4':[secondary4],
             'secondary4_value':[secondary4_value]
                }
        mod=pd.DataFrame.from_dict(mod)
        
        mods=mods.append(mod)
        count_id+=1
    
    return mods

def create_mod_data_v(text):
    collection = BeautifulSoup(text,'html.parser')
    collection = collection.find('div')
        
    mods=pd.DataFrame(columns=['pip','shape','set_type','level','primary','secondary','secondary_value'])
    
    count_id=0
    for x in collection:
        pips = len(x.find('span','pips'))
        shape = x.find('img','modImage').get('src').split('/')[-1].split('_')[0]
        set_type = x.find('img','modImage').get('src').split('/')[-1].split('_')[1].split('.')[0].lower()
        level = int(x.find('span','modLevel').text)
        primary = x.find('span','modPrimary').text.split(' ',maxsplit=1)[1].strip().lower()
        try:
            secondary1 = x.find_all('span','modSecondary')[0].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary1_value = float(x.find_all('span','modSecondary')[0].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary1 = 'not upgraded'
            secondary1_value = 0
        try:
            secondary2 = x.find_all('span','modSecondary')[1].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary2_value = float(x.find_all('span','modSecondary')[1].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary2 = 'not upgraded'
            secondary2_value = 0    
        try:
            secondary3 = x.find_all('span','modSecondary')[2].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary3_value = float(x.find_all('span','modSecondary')[2].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary3 = 'not upgraded'
            secondary3_value = 0   
        try:
            secondary4 = x.find_all('span','modSecondary')[3].text.split(' ',maxsplit=1)[1].strip().lower()
            secondary4_value = float(x.find_all('span','modSecondary')[3].text.split(' ',maxsplit=1)[0].replace('+','').replace('%',''))
        except ValueError:
            secondary4 = 'not upgraded'
            secondary4_value = 0
        mod1={
             'id':[count_id],
             'pip':[pips],
             'shape':[shape],
             'set_type':[set_type],
             'level':[level],
             'primary':[primary],
             'secondary':[secondary1],
             'secondary_value':[secondary1_value],
                }
        mod2={
             'id':[count_id],
             'pip':[pips],
             'shape':[shape],
             'set_type':[set_type],
             'level':[level],
             'primary':[primary],
             'secondary':[secondary2],
             'secondary_value':[secondary2_value],
                }
        mod3={
             'id':[count_id],
             'pip':[pips],
             'shape':[shape],
             'set_type':[set_type],
             'level':[level],
             'primary':[primary],
             'secondary':[secondary3],
             'secondary_value':[secondary3_value],
                }
        mod4={
             'id':[count_id],
             'pip':[pips],
             'shape':[shape],
             'set_type':[set_type],
             'level':[level],
             'primary':[primary],
             'secondary':[secondary4],
             'secondary_value':[secondary4_value],
                }
        mod1=pd.DataFrame.from_dict(mod1)
        mod2=pd.DataFrame.from_dict(mod2)
        mod3=pd.DataFrame.from_dict(mod3)
        mod4=pd.DataFrame.from_dict(mod4)
        
        mods=mods.append(mod1)
        mods=mods.append(mod2)
        mods=mods.append(mod3)
        mods=mods.append(mod4)
        count_id+=1

    return mods

def secondary_filter(mods,stat_type):
    sec = mods[mods['secondary'].isin(stat_type)]

    return sec

def primary_filter(mods,stat_type):
    primary = mods[mods['primary'].isin(stat_type)]

    return primary

def shape_filter(mods,shape):
    modshape = mods[mods['shape'].isin(shape)]

    return modshape
       
def set_filter(mods,set_type):
    modset = mods[mods['set_type'].isin(set_type)]
    
    return modset  

def del_shape(mods,shape):
    #deletes all mods of that shape from potential mods
    mods = mods[mods['shape']!=shape]
    return mods


def del_set(mods,mod_group_set,set_type):
    #checks counts of sets in group
    set_counts=Counter(mod_group_set.values[0])
    #deletes all mods of the set if set_type count has been made
    if set_reqs[set_type] == set_counts[set_type]:
        mods = mods[mods['set_type']!=set_type]
    return mods
	
	
def max_sec_all(mods,sec_stat,arrow_primary,triangle_primary,circle_primary,cross_primary,primary_firm):	
	#finds the maximum value for main secondary for each shape within each set
	if sec_stat == 'speed' and arrow_primary == 'speed':
		mods_highest = mods[(mods['secondary']==sec_stat)].groupby(by=['set_type','shape','primary','id']).max().reset_index()
		mods_highest_arrow = mods[(mods['primary']==sec_stat)].groupby(by=['set_type','shape','primary']).max().reset_index()
	else:
		mods_highest = mods[mods['secondary']==sec_stat].groupby(by=['set_type','shape','primary','id']).max().reset_index()
		mods_highest_arrow = ''
	if primary_firm:
		mods = mods_highest[(mods_highest['shape']=='square')|(mods_highest['shape']=='diamond')|((mods_highest['shape']=='circle')&(mods_highest['primary']==circle_primary))|((mods_highest['shape']=='arrow')&(mods_highest['primary']==arrow_primary))|((mods_highest['shape']=='triangle')&(mods_highest['primary']==triangle_primary))|((mods_highest['shape']=='cross')&(mods_highest['primary']==cross_primary))]
	else:
		mods = mods_highest
		
	return (mods,mods_highest_arrow)
	

def assign_mod(mods,sec_stat,arrows):
    if sec_stat == 'speed':
        mod_group={'square':[math.nan], 'diamond':[math.nan], 'triangle':[math.nan], 'circle':[math.nan], 'cross':[math.nan]}
        mod_group_set={'square':[math.nan], 'diamond':[math.nan], 'triangle':[math.nan], 'circle':[math.nan], 'cross':[math.nan]}  
        mod_group=pd.DataFrame.from_dict(mod_group)
        mod_group_set=pd.DataFrame.from_dict(mod_group_set)
    else:
        mod_group={'square':[math.nan], 'arrow':[math.nan], 'diamond':[math.nan], 'triangle':[math.nan], 'circle':[math.nan], 'cross':[math.nan]}
        mod_group_set={'square':[math.nan], 'arrow':[math.nan], 'diamond':[math.nan], 'triangle':[math.nan], 'circle':[math.nan], 'cross':[math.nan]}  
        mod_group=pd.DataFrame.from_dict(mod_group)
        mod_group_set=pd.DataFrame.from_dict(mod_group_set)
    while np.isnan(mod_group.values[0]).any():
        if len(mods) == 0:
            raise ValueError('There are no more mods to fit the requirements')
        mod=mods[mods['secondary_value']==mods['secondary_value'].max()]
        #assigns mod to group
        mod_group[mod['shape'].values[0]]=mod['id'].values[0]
        mod_group_set[mod['shape'].values[0]]=mod['set_type'].values[0]
        #deletes shape assigned
        mods=del_shape(mods,mod['shape'].values[0])
        #deletes set if necessary        
        mods=del_set(mods,mod_group_set,mod['set_type'].values[0])
        
    if len(mod_group.keys()) == 5:
        set_counts=Counter(mod_group_set.values[0])
        for i in np.unique(mod_group_set.values[0]):
            if set_reqs[i] != set_counts[i]:
                set_needed=i
        mod_group['arrow'] = arrows[arrows['set_type']==set_needed]['id'].values[0]
    return mod_group



def create_set(mods,sec_stat,arrow_primary,triangle_primary,circle_primary,cross_primary,set_types=set_list,primary_firm=1):
    mods=set_filter(mods,set_type=set_types)
    mods=max_sec_all(mods,sec_stat,arrow_primary,triangle_primary,circle_primary,cross_primary,primary_firm)
    mod_group=assign_mod(mods[0],sec_stat,mods[1])
    
    return mod_group

    


#sec_stat='protection'
#set_types=['critdamage','health']
#arrow_primary='speed'
#triangle_primary='critical damage'
#circle_primary='protection'
#cross_primary='offense'
##retrieve all mods of the defined set types
#mods=create_mod_data_v(text)
#
#group=create_set(mods,sec_stat,arrow_primary,triangle_primary,circle_primary,cross_primary,set_types=set_types,primary_firm=1)
#
#




