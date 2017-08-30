import json
import random

with open('C:/Users/ryburk/Google Drive/Coding/Text Analysis/bom.json', 'r') as fp:
    bom = json.load(fp)
y=random.randrange(1,262)   
g=0
for i in bom:
    for j in bom[i]:
            g=g+1
            if g == y:
                print i
                print j