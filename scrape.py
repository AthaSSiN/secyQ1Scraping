import requests 
from bs4 import BeautifulSoup 
import csv 

records = []

for i in range(12):
  
    URL = f"https://summerofcode.withgoogle.com/archive/2019/projects/?page={i+1}"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib')
    
    table = soup.find('ul', attrs = {'class':'project-list-container'})

    for card in table.findAll('li'):
        record = {}
        vals = card.find('md-card').div.findAll()
        
        record['name'] = vals[0].a.text
        record['org'] = vals[3].text[14:]
        record['proj'] = vals[2].text
        records.append(record)

filename = 'result.csv'
with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['name', 'org', 'proj']) 
    w.writeheader() 
    for record in records: 
        w.writerow(record) 
