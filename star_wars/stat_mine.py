def mod_dict_create():
    filex=open('data/stats.txt','r')
    stats=filex.readlines()
    filex.close()
    
    filex=open('data/toons.txt','r')
    toons=filex.readlines()
    filex.close()
    
    filex=open('data/mods.txt','r')
    mods=filex.readlines()
    filex.close()
    
    
    mod_dict={}
    #mod reference
    for z in range(0,len(mods)):
        mods[z]=mods[z].replace('\n','')
        level=mods[z].split(',')[0]
        star=mods[z].split(',')[1]
        group=mods[z].split(',')[2]
        shape=mods[z].split(',')[3]
        pri_stat=mods[z].split(',')[5]
        pri_value=mods[z].split(',')[4]
        if '%' in pri_value:
            pri_value = float(pri_value.replace('%',''))/100
        else:
            pri_value = int(pri_value)
        sec1=mods[z].split(',')[6]
        
        try:
            sec1_val=mods[z].split(',')[10]
            if '%' in sec1_val:
                sec1_val = float(sec1_val.replace('%',''))/100
            else:
                sec1_val = int(sec1_val)
        except:
            continue
        sec2=mods[z].split(',')[7]
        
        try:
            sec2_val=mods[z].split(',')[11]
            if '%' in sec2_val:
                sec2_val = float(sec2_val.replace('%',''))/100
            else:
                sec2_val = int(sec2_val)
        except:
            continue
        sec3=mods[z].split(',')[8]
        
        try:
            sec3_val=mods[z].split(',')[12]
            if '%' in sec3_val:
                sec3_val = float(sec3_val.replace('%',''))/100
            else:
                sec3_val = int(sec3_val)
        except:
            continue
        sec4=mods[z].split(',')[9]
        try:
            sec4_val=mods[z].split(',')[13]
            if '%' in sec4_val:
                sec4_val = float(sec4_val.replace('%',''))/100
            else:
                sec4_val = int(sec4_val)
        except:
            continue
            
        mod_dict['mod'+str(z)]={'level':level,'star':star,'group':group,'shape':shape,'primary':{pri_stat:pri_value},'secondary1':{sec1:sec1_val},'secondary2':{sec2:sec2_val},'secondary3':{sec3:sec3_val},'secondary4':{sec4:sec4_val}}   
        
set_bonus={'Critical':0.3,'Critical Chance':0.05,'Health':0.05,'Defense':0.05,'Tenacity':0.1,'Offense':0.1,'Potency':0.1,'Speed':0.1}
type_dict={'Square':'Transmitter','Arrow':'Receiver','Diamond':'Processor','Triangle':'Holo-Array','Circle':'Data-Bus','Cross':'Multiplexer'}
set_count={'Critical':4,'Critical Chance':2,'Health':2,'Defense':2,'Tenacity':2,'Offense':4,'Potency':2,'Speed':4}
prim_options = ['Speed','Critical Chance','Critical','Potency','Tenacity','Accuracy','Critical Avoidance','Defense','Health','Offense','Protection']
sec_options = ['Speed','Critical Chance','Offense %','Potency','Tenacity','Defense %','Protection %','Health %','Defense','Health','Offense','Protection']
type_list=['Holo-Array', 'Processor', 'Transmitter', 'Multiplexer', 'Data-Bus','Receiver']
global mod_dict1
mod_dict1 = {}
global sec_fil
sec_fil = {}

global taken1
global final1
taken1=[]
final1=[]





#
##def mod_assign(character,sets,set2,set3='None',circle,arrow,triangle,cross,sec_stat):
#place=[j for j,x in enumerate(toons) if x == "%s" % character+'\n']
#place = place[0]
#attributes = {}
#stat_text = stats[place].split('+')
#stat_text.pop(-1)
#for i in stat_text:
#    if '%' in i.split(':')[1]:
#        attributes[i.split(':')[0]] = float(i.split(':')[1].replace('%',''))/100
#    else:
#        attributes[i.split(':')[0]] = int(i.split(':')[1].replace(',',''))
#    



def findlargest(sets,sec_stat,mod_dict1):
    set6=[]
    sec_fil={}
    for j in mod_dict1:
        if mod_dict1[j]['group']==sets:
            set6.append(j)
    for k in set6:
        if sec_stat in mod_dict1[k]['secondary1'].keys():
            sec_fil[k]=mod_dict1[k]['secondary1'][sec_stat]
            continue
        if sec_stat in mod_dict1[k]['secondary2'].keys():
            sec_fil[k]=mod_dict1[k]['secondary2'][sec_stat]
            continue
        if sec_stat in mod_dict1[k]['secondary3'].keys():
            sec_fil[k]=mod_dict1[k]['secondary3'][sec_stat]
            continue
        if sec_stat in mod_dict1[k]['secondary4'].keys():
            sec_fil[k]=mod_dict1[k]['secondary4'][sec_stat]
            continue
    largest_sec = max(sec_fil,key=lambda f: sec_fil[f])
    return largest_sec
    
def topset(sets,sec_stat,prim_dict,tri_stat):
    debug = 1
    if sets in ['Critical','Speed','Offense']:
        choose = 4
        mod_dict1=mod_dict.copy()
        global newlargest
        newlargest=''
        for i in range(0,choose):
            print 'Starting set of 4' if debug else 0
            print newlargest if debug else 0
            if newlargest != '':
                print 'nothing' if debug else 0
                largest = newlargest
                print largest if debug else 0
            else:
                print 'This is number '+str(i) if debug else 0
                largest = findlargest(sets,sec_stat,mod_dict1)
                print largest if debug else 0
            try:
                print 'try #1' if debug else 0
                if mod_dict1[largest]['shape'] in taken1:
                    print '2.1' if debug else 0
                    contained=1
                    while contained:
                        print '2.2' if debug else 0
                        print 'Here' if debug else 0
                        del mod_dict1[largest]
                        print 'There' if debug else 0
                        newlargest = findlargest(sets,sec_stat,mod_dict1)
                        largest = newlargest
                        print '111' if debug else 0
                        if mod_dict1[newlargest]['shape'] not in taken1:
                            print '2.5' if debug else 0
                            contained = 0
                            print '2.6' if debug else 0
                    pass
            except:
                print '3' if debug else 0
                pass
            search=1
            if newlargest != '':
                largest = newlargest
            else:
                pass
            while search == 1:
                print 'Searching...' if debug else 0
                if mod_dict1[largest]['shape'] in taken1:
                    print '21' if debug else 0
                    contained=1
                    while contained:
                        print '22' if debug else 0
                        del mod_dict1[largest]
                        print '23' if debug else 0
                        newlargest = findlargest(sets,sec_stat,mod_dict1)
                        largest = newlargest
                        print largest+' in testing #1' if debug else 0
                        print '24' if debug else 0
                        if mod_dict1[newlargest]['shape'] not in taken1:
                            print '25' if debug else 0
                            contained = 0
                            print '26' if debug else 0
                    pass  
                if mod_dict1[largest]['primary'].keys()[0] in prim_dict[mod_dict1[largest]['shape']]:
                    print '5' if debug else 0
                    final1.append(largest)
                    print '6' if debug else 0
                    taken1.append(mod_dict1[largest]['shape'])
                    print '7' if debug else 0
                    del mod_dict1[largest]
                    print '8' if debug else 0
                    print largest+'was acceptable #2' if debug else 0
                    search = 0
                    newlargest=''
                    print '9' if debug else 0
                    continue
                elif mod_dict1[largest]['primary'].keys()[0] not in prim_dict[mod_dict1[largest]['shape']]:
                    print '10' if debug else 0
                    del mod_dict1[largest]
                    print 'There' if debug else 0
                    newlargest = findlargest(sets,sec_stat,mod_dict1)
                    largest=newlargest
                    print largest+' in testing #2' if debug else 0
                    print '11' if debug else 0
                else:
                    break
        
    else:
        choose = 2        
        mod_dict1=mod_dict.copy()
        newlargest=''
        for i in range(0,choose):
            print 'Starting set of 2' if debug else 0
            print newlargest if debug else 0
            if newlargest != '':
                print 'nothing' if debug else 0
                largest = newlargest
                print largest if debug else 0
            else:
                print 'This is number '+str(i) if debug else 0
                largest = findlargest(sets,sec_stat,mod_dict1)
                print largest if debug else 0
            try:
                print 'try #1' if debug else 0
                if mod_dict1[largest]['shape'] in taken1:
                    print '2.1' if debug else 0
                    contained=1
                    while contained:
                        print '2.2' if debug else 0
                        print 'Here' if debug else 0
                        del mod_dict1[largest]
                        print 'There' if debug else 0
                        newlargest = findlargest(sets,sec_stat,mod_dict1)
                        largest = newlargest
                        print largest+' is in testing' if debug else 0
                        if mod_dict1[newlargest]['shape'] not in taken1:
                            print '2.5' if debug else 0
                            contained = 0
                            print '2.6' if debug else 0
                    pass
            except:
                print '3' if debug else 0
                pass
            search=1
            if newlargest != '':
                largest = newlargest
            else:
                pass
            while search == 1:
                print 'Searching...' if debug else 0
                try:
                    if mod_dict1[largest]['shape'] in taken1:
                        print '21' if debug else 0
                        contained=1
                        while contained:
                            print '22' if debug else 0
                            del mod_dict1[largest]
                            print '23' if debug else 0
                            newlargest = findlargest(sets,sec_stat,mod_dict1)
                            largest = newlargest
                            print largest+' in testing #3' if debug else 0
                            print '24' if debug else 0
                            if mod_dict1[newlargest]['shape'] not in taken1:
                                print '25' if debug else 0
                                contained = 0
                                print '26' if debug else 0
                        pass
                except KeyError:
                    pass
#                    if prim_dict[list(set(type_list)-set(taken1))[0]]==sec_stat:
#                        newlargest = findlargest(sets,tri_stat,mod_dict)
#                        largest=newlargest
#                        final1.append(largest)
#                        taken1.append(mod_dict[largest]['shape'])
              
                if mod_dict1[largest]['primary'].keys()[0] in prim_dict[mod_dict1[largest]['shape']]:
                    print '5' if debug else 0
                    final1.append(largest)
                    print '6' if debug else 0
                    taken1.append(mod_dict1[largest]['shape'])
                    print '7' if debug else 0
                    del mod_dict1[largest]
                    print '8' if debug else 0
                    print largest+' was acceptable #4' if debug else 0
                    search = 0
                    newlargest=''
                    print '9' if debug else 0
                    continue
                elif mod_dict1[largest]['primary'].keys()[0] not in prim_dict[mod_dict1[largest]['shape']]:
                    print '10' if debug else 0
                    del mod_dict1[largest]
                    print 'There' if debug else 0
                    newlargest = findlargest(sets,sec_stat,mod_dict1)
                    largest=newlargest
                    print largest+' in testing #4' if debug else 0
                    print '11' if debug else 0
                else:
                    break   
    print final1
        
def delete(sets,sec_stat):
    print 'Here' if debug else 0
    del mod_dict1[largest]
    print 'There' if debug else 0
    newlargest = findlargest(sets,sec_stat,mod_dict1)
    print '11' if debug else 0
    return newlargest
    
character = 'Rey'
sets = ['Critical','Critical Chance']
circle = 'Protection'
arrow = 'Speed'
triangle = 'Critical Damage'
cross = 'Protection'
sec_stat = 'Speed'
prim_dict={'Transmitter':'Offense','Receiver':arrow,'Processor':'Defense','Holo-Array':triangle,'Data-Bus':circle,'Multiplexer':cross}
tri_stat='Critical Chance'

for each in sets:
    topset(each,sec_stat,tri_stat,prim_dict)