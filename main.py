import json
import pprint
import requests
from pyquery import PyQuery as pq
url = 'http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx'
payload = {'ctl00$ctl02':'ctl00$cphMain$ctl00|ctl00$cphMain$cboSearch',
            'ctl00_ctl02_HiddenField':';;AjaxControlToolkit, Version=3.0.20820.16598, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:zh-TW:707835dd-fa4b-41d1-89e7-6df5d518ffb5:411fea1c:865923e8:77c58d20:91bd373d:14b56adc:596d588c:8e72a662:acd642d2:269a19ae',
            '__EVENTTARGET':'ctl00$cphMain$cboSearch',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            '__VIEWSTATE':'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',
            '__VIEWSTATEGENERATOR':'5967A80E',
            'ctl00$cphMain$cboSearch':'所有水庫',
            '__ASYNCPOST':'false'}

r = requests.post(url,data=payload).text

d = []
q = pq(r)
aa = q('#frame').text().split(' ',24)[-1].split('% ')
for x in aa:
    y = x.split(' ')
    name = y[0]
    if name == '附註':
        break
    capavailable = y[1]
    caplevel = y[9]
    currcap = y[10]
    currcapper = y[11]
    row = dict(name=name,capavailable=capavailable,caplevel=caplevel,currcap=currcap,currcapper=currcapper)
    d.append(row)

pprint.pprint (d)