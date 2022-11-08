import requests
from bs4 import BeautifulSoup
import html5lib


url="https://redwineclassification.herokuapp.com/"

req = requests.get(url)
#print(req.content)
sp = BeautifulSoup(req.content, 'html.parser')
#print(sp)

data = sp.find("div", {"class":"site-heading"})
print(data)

data1 = data.find("span")
data1=str(data1)
lst=data1.split(">")
lst=lst[1].split("<")
lst=lst[0]
print(lst)

d2 = sp.find('div', {"class": "small text-center text-muted fst-italic"})
d2 = str(d2)
d3 = (d2.split(">"))
d3 = (d3[1].split("<"))
print(d3[0])

