import requests
from bs4 import BeautifulSoup
import html5lib


url="https://redwineclassification.herokuapp.com/"

req = requests.get(url)
#print(req.content)
sp = BeautifulSoup(req.content, 'html.parser')
#print(sp)

data = sp.find("div", {"class":"site-heading"})
data1 = data.find("span")

data1=str(data1)

lst=data1.split(">")
lst=lst[1].split("<")
lst=lst[0]
print(lst)