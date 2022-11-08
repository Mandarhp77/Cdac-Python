import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/new/"
data = requests.get(url)
dta = BeautifulSoup(data.content, "html5lib")

dt = dta.find("div", {"class": "pbu8wv-2 gvhMom"})
print(dt)

a = dt.find("div")
b = dt.find("p")

a=str(a)
b=str(b)

a=a.split(">")
a=a[1].split("<")
a=a[0]

b=b.split(">")
b=b[1].split("<")
b=b[0]

print(a, b)