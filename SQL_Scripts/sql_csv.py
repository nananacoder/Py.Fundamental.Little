#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
os.chdir('/home/ankiy/ankiprojects')
if '/home/ankiy/ankiprojects' not in sys.path:
    sys.path.append('/home/ankiy/ankiprojects')

import MySQLdb
from dbconfig1 import execute_sql,fetchall_sql

DB = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'xxxx',
        'db': 'xxxx',
        'charset': 'utf8',
        }

def export_table_csv(tb, _path):
    # give mysql permission to write
    p = os.path.split(_path)[0]
    # os.system('chmod a+w %s' % p)
    export_sql = 'SELECT * FROM {table} INTO OUTFILE "{path}" FIELDS TERMINATED BY "," LINES TERMINATED BY "\n"'
    print ('backup {table} to {path}'.format(table=tb, path=_path))
    execute_sql(export_sql.format(table=tb, path=_path))

def import_csv_table(csvfile, tb, tb_type=None):
    import_sql = 'LOAD DATA INFILE "{path}" INTO TABLE `{table}` FIELDS TERMINATED BY "," LINES TERMINATED BY "\n"'
    execute_sql(import_sql.format(path=csvfile, table=tb))


def show_columns(table_name):
    '''
    :param table_name: table'name in database
    :return: a list of this table's columns
    '''

    # execute_sql("""desc %s""" % table_name)
    results = fetchall_sql("""desc %s""" % table_name)
    column_list = []
    for r in results:
        column_list.append(r[0])
    return column_list


def writer_csv(table_name):
    import csv

    sql = "SELECT * FROM %s " % table_name
    lines = fetchall_sql(sql)
    list_data = [list(line) for line in lines]
    print list_data

    column_list = show_columns(table_name)
    path = './OrderItems.csv'
    with open(path, 'wb') as csvfile:
        # table_writer = csv.writer(csvfile, delimiter=' ')
        table_writer = csv.writer(csvfile)
        table_writer.writerow(column_list)

        for data in list_data:
            table_writer.writerow(data)


if __name__ == '__main__':
    # writer_csv('OrderItems')
    print show_columns('OrderItems')
    # export_table_csv('OrderItems', '/var/lib/mysql-files/OrderItems.csv')

    # import_csv_table('/var/lib/mysql-files/Product.csv',tb='product_2')