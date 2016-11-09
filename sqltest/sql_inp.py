#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

import MySQLdb
import sqlparse

socket = ['/tmp/mysql3306.sock', '/tmp/mysql3307.sock']


def db_source(root_dir, db):
    if db == 3306:
        sock = socket[0]
    else:
        sock = socket[1]

    con = MySQLdb.connect(
        host="localhost", user="root", passwd="123456",
        db="testDB", charset="utf8",
    )
    with con:
        cur = con.cursor()
        for parent, dir_names, file_names in os.walk(root_dir):
            for filename in file_names:
                file_path = os.path.join(parent, filename)

                sql = open("%s" % file_path).read()
                sql_parts = sqlparse.split(sql)
                for sql_part in sql_parts:
                    if sql_part.strip() == '':
                        continue
                    cur.execute(sql_part)


if __name__ == "__main__":

    root_dir = sys.argv(2)
    db = sys.argv(3)
    #db = 3307
    #root_dir = "/home/ankiy/ankiprojects/sqltest/sql_folder" #批量sql文件的文件夹路径
    db_source(root_dir, db)