#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import hashlib

cookies = {
    'Hm_lvt_4216c57ef1855492a9281acd553f8a6e': '1459828808,1460081443',
    'BDTUJIAID': 'e5ee29a4bd30d8f158e1212b14cae816',
    '_ga': 'GA1.2.917797687.1459844132',
    'Hm_lpvt_4216c57ef1855492a9281acd553f8a6e': '1460081443',
}

headers = {
    'Host': 'm.cnbeta.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

IP = ['http://121.201.98.215/m.cnbeta.com/mobile/wap', 'http://117.172.6.131/m.cnbeta.com/mobile/wap', 'http://183.61.242.50', 'http://61.184.201.226', 'http://180.97.171.49']
#IP = 'http://121.201.98.215'
response_1 = requests.get(IP[0], headers=headers, cookies = cookies)
content_1 = response_1.content
m_1 = hashlib.md5(response_1.content)
md5_value_1 = m_1.hexdigest()
print len(content_1), md5_value_1
with open('IP1_content.html', 'w') as f1:
    f1.write(content_1)

response_2 = requests.get(IP[1], headers = headers, cookies = cookies)
content_2 = response_2.content
m_2 = hashlib.md5(response_2.content)
md5_value_2 = m_2.hexdigest()
print len(content_1), md5_value_2
with open('IP2_content.html', 'w') as f2:
    f2.write(content_2)



