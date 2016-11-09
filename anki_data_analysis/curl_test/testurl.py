#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

import requests
import MySQLdb


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

proxies = {'http':'http://117.172.6.131'}
response = requests.get('http://m.cnbeta.com', headers=headers, cookies=cookies, proxies=proxies)




content = response.content
soup = BeautifulSoup(content)
content_selected=soup.select("li div a")
content_a = soup.find_all("a", {"data-transition":"slide"})


con = MySQLdb.connect("localhost","testuser","test623","testdb" )
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE Url_contents")
    cur.execute("CREATE TABLE IF NOT EXISTS \
        Url_contents(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(2500))")
    for aa in content_a:
        b = aa.get_text()
        cur.execute("INSERT INTO Url_contents(Name) VALUES('%s')"%b)