import requests
from bs4 import BeautifulSoup
import time

#Record beginning time
start_time = time.time()

# Start a session
session = requests.session()

# Try accessing a page that requires you to be logged in
r = session.get('https://swgoh.gg/meta-report/10/#leaders')

# Translate the web page for use in BeautifulSoup
collection = BeautifulSoup(r.text,'html.parser')
rows=collection.find_all('tr')



print("--- %s seconds ---" % (time.time() - start_time))