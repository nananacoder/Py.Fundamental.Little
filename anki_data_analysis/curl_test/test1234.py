#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb as mdb
import csv

con = mdb.connect('localhost', 'testuser',
        'test623', 'testdb');

with con:

    cur = con.cursor(mdb.cursors.DictCursor)

    #cur.execute("DROP TABLE URL_RESULT")

    cur.execute("SELECT * FROM URL_1")
    numrows = int(cur.rowcount)
    data = cur.fetchall()

    start_numb = 0
    end_numb = 15

    print numrows

    URL_error_num = [0, 0, 0]
    URL1_IP_num = [0, 0, 0, 0]
    URL2_IP_num = [0, 0, 0, 0]
    URL3_IP_num = [0, 0, 0, 0]


    with open('url_result_2.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        while end_numb < numrows:
            for i in range(start_numb, end_numb):
                dic = data[i]
                if 'm.cnbeta.com' in dic.values() and 'http://121.201.98.215' in dic.values():
                    length_host_1 = dic['LENGTH']
                    md5_host_1 = dic['MD5']
                elif 'm.cnbeta.com/list_latest_1.htm' in dic.values() and 'http://121.201.98.215' in dic.values():
                    length_host_2 = dic['LENGTH']
                    md5_host_2 = dic['MD5']
                elif 'm.cnbeta.com/mobile/wap' in dic.values() and 'http://121.201.98.215' in dic.values():
                    length_host_3 = dic['LENGTH']
                    md5_host_3 = dic['MD5']


            for i in range(start_numb, end_numb):
                dic = data[i]
                if 'm.cnbeta.com' in dic.values() and (dic['LENGTH'] != length_host_1 or dic['MD5'] != md5_host_1):
                    URL_error_num[0] += 1
                    spamwriter.writerow([dic['TIME'], dic['URL'], dic['IP']])
                    cur.execute("INSERT INTO URL_RESULT(TIME, IP, URL) VALUES('%s', '%s', '%s')"%(dic['TIME'], dic['URL'], dic['IP']))
                    if dic['LENGTH'] != length_host_1:
                        spamwriter.writerow([dic['TIME'], dic['URL'], dic['IP'], dic['']])
                    if dic['IP'] == 'http://117.172.6.131':
                        URL1_IP_num[0] += 1
                    if dic['IP'] == 'http://183.61.242.50':
                        URL1_IP_num[1] += 1
                    if dic['IP'] == 'http://61.184.201.226':
                        URL1_IP_num[2] += 1
                    if dic['IP'] == 'http://180.97.171.49':
                        URL1_IP_num[3] += 1
                elif 'm.cnbeta.com/list_latest_1.htm' in dic.values() and (dic['LENGTH'] != length_host_2 or dic['MD5'] != md5_host_2):
                    URL_error_num[1] += 1
                    spamwriter.writerow([dic['TIME'], dic['URL'], dic['IP']])
                    cur.execute("INSERT INTO URL_RESULT(TIME, IP, URL) VALUES('%s', '%s', '%s')"%(dic['TIME'], dic['URL'], dic['IP']))
                    if dic['IP'] == 'http://117.172.6.131':
                        URL2_IP_num[0] += 1
                    if dic['IP'] == 'http://183.61.242.50':
                        URL2_IP_num[1] += 1
                    if dic['IP'] == 'http://61.184.201.226':
                        URL2_IP_num[2] += 1
                    if dic['IP'] == 'http://180.97.171.49':
                        URL2_IP_num[3] += 1
                elif 'm.cnbeta.com/mobile/wap' in dic.values() and (dic['LENGTH'] != length_host_3 or dic['MD5'] != md5_host_3):
                    URL_error_num[2] += 1
                    spamwriter.writerow([dic['TIME'], dic['URL'], dic['IP']])
                    cur.execute("INSERT INTO URL_RESULT(TIME, IP, URL) VALUES('%s', '%s', '%s')"%(dic['TIME'], dic['URL'], dic['IP']))
                    if dic['IP'] == 'http://117.172.6.131':
                        URL3_IP_num[0] += 1
                    if dic['IP'] == 'http://183.61.242.50':
                        URL3_IP_num[1] += 1
                    if dic['IP'] == 'http://61.184.201.226':
                        URL3_IP_num[2] += 1
                    if dic['IP'] == 'http://180.97.171.49':
                        URL3_IP_num[3] += 1
                else:
                    pass


            start_numb += 15
            end_numb += 15

            if end_numb > numrows:
                break