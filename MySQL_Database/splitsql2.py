#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Aim to split large sql file to multi small sql files within a folder.

This split file is specific for some sql files started with some format.

It can modified later to use.
"""

import sqlparse
import os
import sys

sql_file = sys.argv[1]
sql_file_name = sql_file.split("/")[-1].split(".")[0]
os.mkdir(sql_file_name)
home_dir = os.getcwd()
new_file_dir = home_dir + "/" + sql_file_name + '/'

sql = open(sql_file).read()
sql = sql.splitlines()

n1 = 0
n2 = 0
list_create = []
str_create = ''
sql_start = ''
sql_drop = ''
sql_record = ''
content = ''
name = ''
start_part_str = ''


def table_name(sql_part):
    parsed = sqlparse.parse(sql_part, encoding="utf-8")
    stmt = parsed[0]
    name = str(stmt.tokens[-2]).strip('`')
    return name

for i in range(len(sql)):
    if sql[i].find('SET FOREIGN_KEY_CHECKS') >= 0:
        start_part_list = sql[0:i+1]
        start_part_str = "\n".join(start_part_list)
    if sql[i].find('Table structure for') >= 0:
        sql_start = sql[i-1] + '\n' + sql[i] + '\n' + sql[i+1]
        sql_drop = sql[i+2]
        name = table_name(sql[i+2])
        n1 = i+3
    if sql[i].find('Records of') >= 0:
        sql_record = sql[i-1] + '\n' + sql[i] + '\n' + sql[i+1]
        n2 = i-1
        list_create = sql[n1:n2]
        str_create = "\n".join(list_create)
        content = start_part_str + '\n' + sql_start + '\n' + sql_drop + '\n' + str_create + '\n' + sql_record
        m = i+2
        try:
            while sql[m].find('INSERT INTO') >= 0:
                content = content + '\n' + sql[m]
                m += 1
        except IndexError:
            pass
        file_name = new_file_dir + name + '.sql'
        f = open(file_name, 'w+')
        f.write(content)
        f.close()




