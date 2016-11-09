from datetime import datetime

import requests
import hashlib
import MySQLdb

IP = ['http://121.201.98.215', 'http://117.172.6.131', 'http://183.61.242.50', 'http://61.184.201.226', 'http://180.97.171.49']
IP_after_2 = '/list_latest_1.htm/'
IP_after_3 = '/mobile/wap/'

url_1 = 'm.cnbeta.com'
url_2 = 'm.cnbeta.com/list_latest_1.htm'
url_3 = 'm.cnbeta.com/mobile/wap'

cookies_1 = {
    'Hm_lvt_4216c57ef1855492a9281acd553f8a6e': '1459828808,1460081443',
    'BDTUJIAID': 'e5ee29a4bd30d8f158e1212b14cae816',
    '_ga': 'GA1.2.917797687.1459844132',
    'Hm_lpvt_4216c57ef1855492a9281acd553f8a6e': '1460081443',
}

cookies_2 = {
    'Hm_lvt_4216c57ef1855492a9281acd553f8a6e': '1459828808,1460081443',
    'BDTUJIAID': 'e5ee29a4bd30d8f158e1212b14cae816',
    '_ga': 'GA1.2.917797687.1459844132',
    'Hm_lpvt_4216c57ef1855492a9281acd553f8a6e': '1460531646',
    '_gat': '1',
}

cookies_3= {
    'Hm_lvt_4216c57ef1855492a9281acd553f8a6e': '1459828808,1460081443',
    'BDTUJIAID': 'e5ee29a4bd30d8f158e1212b14cae816',
    '_ga': 'GA1.2.917797687.1459844132',
    'Hm_lpvt_4216c57ef1855492a9281acd553f8a6e': '1460531638',
    '_gat': '1',
}

headers = {
    'Host': 'm.cnbeta.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}


i = IP[0]

IP_2 = i + IP_after_2
IP_3 = i + IP_after_3

response_1 = requests.get(i, headers = headers, cookies = cookies_1)
m_1 = hashlib.md5(response_1.content)
content_length_1 = len(response_1.content)
md5_value_1 = m_1.hexdigest()
content_1 = response_1.content
print content_length_1
print md5_value_1
with open('IP_host_content_1.html', 'w') as f1:
    f1.write(content_1)

response_2 = requests.get(IP_2, headers = headers, cookies = cookies_2)
m_2 = hashlib.md5(response_2.content)
content_length_2 = len(response_2.content)
md5_value_2 = m_2.hexdigest()
content_2 = response_2.content
print content_length_2
print md5_value_2
with open('IP_host_content_2.html', 'w') as f1:
    f1.write(content_2)


response_3 = requests.get(IP_3, headers = headers, cookies = cookies_3)
m_3 = hashlib.md5(response_3.content)
content_length_3 = len(response_3.content)
md5_value_3 = m_3.hexdigest()
content_3 = response_3.content
print content_length_3
print md5_value_3
with open('IP_host_content_3.html', 'w') as f1:
    f1.write(content_3)



m = IP [1]

IP_2 = m + IP_after_2
IP_3 = m + IP_after_3

response_1 = requests.get(i, headers = headers, cookies = cookies_1)
m_1 = hashlib.md5(response_1.content)
content_length_1 = len(response_1.content)
md5_value_1 = m_1.hexdigest()
content_1 = response_1.content
print content_length_1
print md5_value_1
if response_1.status_code == 404:
    print response_1.content
with open('IP1_content_1.html', 'w') as f1:
    f1.write(content_1)

response_2 = requests.get(IP_2, headers = headers, cookies = cookies_2)
m_2 = hashlib.md5(response_2.content)
content_length_2 = len(response_2.content)
md5_value_2 = m_2.hexdigest()
content_2 = response_2.content
print content_length_2
print md5_value_2
if response_2.status_code == 404:
    print response_2.content
with open('IP1_content_2.html', 'w') as f1:
    f1.write(content_2)

response_3 = requests.get(IP_3, headers = headers, cookies = cookies_3)
m_3 = hashlib.md5(response_3.content)
content_length_3 = len(response_3.content)
md5_value_3 = m_3.hexdigest()
content_3 = response_3.content
print content_length_3
print md5_value_3
if response_3.status_code == 404:
    print response_3.content
with open('IP1_content_3.html', 'w') as f1:
    f1.write(content_3)