import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/currencies/bitcoin/"
data = requests.get(url)
dta = BeautifulSoup(data.content, "html5lib")

dt = dta.find("div", {"class": "priceValue"})
#print(dt)
a = dt.find("span")
a=str(a)
a=a.split("$")
a=a[1].split("<")
a=a[0]
print(a)