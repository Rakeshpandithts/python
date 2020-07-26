from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://jaaga.in")
bsObj = BeautifulSoup(html.read())

for link in bsObj.find_all('a'):
    print(link.get('href'))


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import requests
# import pprint
# # html = urlopen("https://www.lybrate.com/")
# url = "http://lybrate.com/bangalore/general-physician/mahalakshmi-layout-bangalore"
# # bsObj = BeautifulSoup(html.read())
# r = requests.get(url) 
# pprint.pprint(r.content) 
# # print(bsObj)

# # for link in bsObj.find_all('a'):
# #     print(link.get('href'))


