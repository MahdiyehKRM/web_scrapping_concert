import requests
from bs4 import BeautifulSoup 
import pandas
from openpyxl import Workbookg

url='https://www.honarticket.com/'
req=requests.get(url)
print(req)
names=[]
places=[]
times=[]
soup=BeautifulSoup(req.text,'html.parser')
singer_name=soup.select('span.prefix small')
for name in singer_name : 
    s_n=name.text
    names.append(s_n)
place=soup.select('i.i i-location-light')
for p in place :
    pl=p.text
    places.append(pl)
time=soup.select('i.i i-calendar')
for t in time:
    ti=t.text
    times.append(ti)
concerts={'name':names,'place':places,'times':time}
data=pandas.DataFrame.from_dict(concerts,orient='index')
data=data.transpose()
write=pandas.ExcelWriter('concerts.xlsx')
data.to_excel(write)    
write.save()
