file=open('C:/Users/ryburk/Google Drive/Loc_ENG_US.txt')
swtext = file.readlines()
sw2=[]


for i in swtext:
    if 'UNIT_' in i and '_NAME' in i and 'SHIPMENT_' not in i and 'SUPPORT' not in i or 'CONTEXTUALMSG_CHAR_DIALOG_STORY' in i:
        sw2.append(i)
    else:
        pass


file=open('C:/Users/ryburk/Google Drive/Coding/Projects/star_wars/current.txt','r')
old = file.readlines()
file.close()

file=open('C:/Users/ryburk/Google Drive/Coding/Projects/star_wars/current.txt','w')
for i in sw2:
    if 'Promotion' in i or 'Training' in i or 'Generator' in i:
        pass
    else:
        cut=i.find('|')
        parsed = i[cut+1:-1].lower()+'\n'
        if parsed in old:
            file.write(parsed)
        else:
            print'********'+parsed
            file.write(parsed)

file.close()

print 'No New Characters...'

file=open('C:/Users/ryburk/Google Drive/Loc_ENG_USold.txt')
swtextold = file.readlines()

if swtextold == swtext:
    print "It's TRUE they are the same..."
else:
    print "\nTHERE IS SOMETHING NEW:\n"
    for i in swtext:
        if i in swtextold:
            continue
        else:
            print i