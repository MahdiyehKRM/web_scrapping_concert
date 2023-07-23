import requests
from bs4 import BeautifulSoup 
url='https://www.honarticket.com/'
req=requests.get(url)
print(req)
