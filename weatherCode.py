#pip install requests
#pip install beautifulsoup4
from os import write
import requests as req
from bs4 import BeautifulSoup
#import BeautifulSoup

f = open('output.txt','a')

url = req.get('http://www.jma.go.jp/bosai/common/const/area.json')

s = BeautifulSoup(url.text,'html.parser')
print(s)
bsObj = BeautifulSoup(url.text,'html.parser').text

for c in bsObj:
    f.write(c)
    if c=='}' or c=='{':
        f.write('\n')

print('complete')

#f.write(bsObj)