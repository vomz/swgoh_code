import pandas
import numpy as np

data = pandas.DataFrame(columns=['price','lotsize','rooms','sqft','bthrms','pool','fence','garage','basement'])

n=40000
array = np.random.gamma(shape=9,scale=.5,size=n)
array1 = np.random.gamma(shape=9,scale=.5,size=n)
array2 = np.random.gamma(shape=9,scale=.5,size=n)
array3 = np.random.gamma(shape=9,scale=.5,size=n)
array4 = np.random.gamma(shape=9,scale=.5,size=n)
array5 = np.random.gamma(shape=9,scale=.5,size=n)

data.price=array*125000
data.lotsize=array1*2000
data.rooms=array2*.8
data.sqft=array3*750
data.bthrms=array4*.7
data.garage=array5*.45

data.price = data.price.round(decimals=0)
data.lotsize = data.lotsize.round(decimals=0)
data.rooms = data.rooms.round(decimals=0)
data.sqft = data.sqft.round(decimals=0)
data.bthrms = data.bthrms.round(decimals=0)
data.garage = data.garage.round(decimals=0)
data.pool = np.random.randint(2,size=n)
data.fence = np.random.randint(2,size=n)
data.basement = np.random.randint(2,size=n)

data.price=data.price.round(decimals=0)
data.lotsize=data.lotsize.round(decimals=0)
data.rooms=data.rooms.round(decimals=0)
data.sqft=data.sqft.round(decimals=0)
data.bthrms=data.bthrms.round(decimals=0)
data.garage=data.garage.round(decimals=0)





#data.to_csv('house.csv',sep=',',encoding = 'utf-8',index=False,header=False)

#import numpy
## 1 dimension array of 1M random var's uniformly distributed between 1 and 2
## pass to poisson
#array = numpy.random.gamma(shape=9,scale=.5,size=40000)
#
#array=array*200000
#
#print max(array)
#print min(array)
#
#import matplotlib.pyplot as plt
#plt.hist(array)
#plt.show()



print array.mean()
print array1.mean()
print array2.mean()
print array3.mean()
print array4.mean()
print array5.mean()