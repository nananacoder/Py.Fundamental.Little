#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import MySQLdb

DB = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '123456',
        'db': 'testDB',
        'charset': 'utf8',
        }

def execute_sql(sql):
    """ 执行sql语句 """

    conn = MySQLdb.connect(**DB)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    conn.close()

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



if __name__ == '__main__':

    # export_table_csv('Products', '/var/lib/mysql-files/Product.csv')

    import_csv_table('/var/lib/mysql-files/Product.csv',tb='product_2')