import re
import requests
from pyquery import PyQuery as pq

date = input()

response = requests.get('https://www.officialcharts.com/charts/singles-chart/{}/7501/'.format(date.replace('/','')))
doc = pq(response.text)

info = []
singer = []
Pos = []
for each_tr in doc('.artist').items():
    singer.append(each_tr.text())
for each_tr in doc('.title').items():
    info.append(each_tr.text())
for each_tr in doc('.position').items():
    Pos.append(each_tr.text())

for i in range (5):
    print('{}.{} - {}'.format(Pos[i],info[i],singer[i]))
