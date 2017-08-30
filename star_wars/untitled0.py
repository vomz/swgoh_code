import requests
from bs4 import BeautifulSoup
import time
import pandas
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


## Start a session
#session = requests.session()
#
## Try accessing a page that requires you to be logged in
##r = session.get('http://www.ranker.com/fact-lists/automobile-models/make')
#
#r = session.get('https://en.wikipedia.org/wiki/List_of_automobile_sales_by_model')
#
## Translate the web page forse in BeautifulSoup
#collection = BeautifulSoup(r.text,'html.parser')
#
## collect and organize the characters that are unlocked
#models=collection.find_all('tr')
#
#list=[]
#
#for gg in models:
#    try:
#        if gg.th.text == 'Image' or gg.th.text in list:
#            continue
#        else:
#            list.append(gg.th.text)
#    except AttributeError:
#        continue
#
#x=['\n\n\nv\nt\ne\n\n\nAutomotive industry\n','By country','Africa','Asia','Europe','North America','South America','Oceania','Data','History','Manufacturers','Organisations','Related topics']
#
#for i in x:
#    list.remove(i)
#    
#    
#make=[]
#model=[]
#
#for i in list:
#    try:
#        if 'Alfa Romeo' in i or 'De Tomaso' in i or 'Land Rover' in i or 'Range Rover' in i:
#            make.append(' '.join(i.split(' ')[:2]))
#            model.append(' '.join(i.split(' ')[2:]))
#        else:
#            make.append(i.split(' ')[0])
#            model.append(' '.join(i.split(' ')[1:]))
#    except:
#        make.append(i)
#        model.append(i)
#
#data = pandas.DataFrame(columns=['makes','models','year','price','trans','ac','keyless','mpg'])
#
#data['makes'].apply('str')
#data['models'].apply('str')
#
#n=100000
#
#data.price = np.random.choice(16000,5000000,size=n)
#
#np.random.seed(0)
#data.makes = np.random.choice(make,size=n)
#np.random.seed(0)
#data.models = np.random.choice(model,size=n)
#
#
#data.year = np.random.randint(1900,2017,size=n)
#data.mpg = np.random.randint(8,45,size=n)
#data.trans = np.random.randint(2,size=n)
#data.ac = np.random.randint(2,size=n)
#data.keyless = np.random.randint(2,size=n)
#
#
#makes_price = pandas.pivot_table(data,values='price',columns='makes',aggfunc=np.mean)
#years_price = pandas.pivot_table(data,values='price',columns='year',aggfunc=np.mean)
#
#pivot = pandas.pivot_table(data,values='price',columns='makes',aggfunc=np.mean)

#data.to_csv('house.csv',sep=',',encoding = 'utf-8',index=False,header=False)

#
#
#SKEW_PARAMS = [5]
#
#def skew_norm_pdf(x,e=0,w=1,a=0):
#    # adapated from:
#    # http://stackoverflow.com/questions/5884768/skew-normal-distribution-in-scipy
#    t = (x-e) / w
#    return 2.0 * w * stats.norm.pdf(t) * stats.norm.cdf(a*t)
#
## generate the skew normal PDF for reference:
#location = 2
#scale = 2.0
#x = np.linspace(0.0033,.2,10000) 
#
#plt.subplots(figsize=(12,4))
#for alpha_skew in SKEW_PARAMS:
#    p = skew_norm_pdf(x,location,scale,alpha_skew)
#    # n.b. note that alpha is a parameter that controls skew, but the 'skewness'
#    # as measured will be different. see the wikipedia page:
#    # https://en.wikipedia.org/wiki/Skew_normal_distribution
#    plt.plot(p)


def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for "+str(n)+" * factorial("+str(n-1)+"): "+str(res))
        return res	

print(factorial(5))