
import itertools
import operator,re
'''
gearnum = open('gearnum.txt','r')
gearnum = map(str.strip,gearnum.readlines())
gearname = open('gearname.txt','r')
gearname = map(str.strip,gearname.readlines())
gearmats = open('gearmats.txt','r')
gearmats = map(str.strip,gearmats.readlines())

materials=[]
number=[]

for i in range(0,len(gearmats)):
	a=gearmats[i].split(', ')
	materials.append(a)
for i in range(0,len(gearnum)):
	a=gearnum[i].split(', ')
	number.append(a)

a='Mk 9 BlasTech Weapon Mod'
#main piece
def inputs(piece):
	if piece in gearname:
		place_i=[j for j,x in enumerate(gearname) if x == "%s" % piece]
		inputs_i = materials[place_i[0]]
		num_inputs_i = number[place_i[0]]
		inputs_a=[]
		#first inputs
		for i in range(0,len(inputs_i)):
			place_a=[j for j,x in enumerate(gearname) if x == "%s" % inputs_i[i]]
			if place_a==[]:
				inputs_a.append(inputs_i[i])
			else:
				if materials[place_a[0]][0]=='':
					inputs_a.append(inputs_i[i])
				else:
					inputs_a.append(materials[place_a[0]])
	else:
		print "This takes no inputs!"
	print inputs_a

inputs(a)
'''
