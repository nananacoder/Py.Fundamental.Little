#!/usr/bin/python2.7
# -*-coding:utf-8-*-

import pandas as pd
import MySQLdb
from sqlalchemy import create_engine

DB = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'xxx',
        'db': 'xxx',
        'charset': 'utf8',
        }

def execute_sql(sql):
    """ 执行sql语句 """

    conn = MySQLdb.connect(**DB)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    #except:
    #    conn.rollback()
    #debug
    except Exception as e:
        print e
        conn.rollback()
    conn.close()

def show_columns(table_name,indx):
    '''
    :return: a list of this table's columns
    '''
    conn = MySQLdb.connect(**DB)
    sql = 'desc `%s`;' % table_name

    cl_df = pd.read_sql(sql,con=conn)

    new_col = pd.DataFrame(data=None,index=indx,columns=cl_df['Field'])
    conn.close()

    return new_col

def rd_csv(file_name):
    csv_input = pd.read_csv(file_name, header=0,sep=',',encoding='utf-8',engine='c',  quoting=1)

    table_name = file_name.split('/')[-1].split('.')[0]

    new_col = show_columns(table_name,indx=csv_input.index)

    new_col_index =  new_col.columns
    old_col_index =  csv_input.columns

    for n_col in new_col_index:
        if n_col in old_col_index:
            new_col[n_col] = csv_input[n_col]


    return  new_col, table_name


def export_data(table_name):

    conn = MySQLdb.connect(**DB)
    sql = 'select * from `%s`;' % table_name
    df = pd.read_sql(sql, con=conn)
    conn.close()

    file_name = table_name + '.csv'
    df.to_csv(file_name, index=False,sep=',',encoding='utf-8', quoting=1)
    return df

def import_sql(file_name):
    # conn = MySQLdb.connect(**DB)
    new_col_pd, table_name = rd_csv(file_name)


    # new_col_pd.to_csv(file_name, index=False,sep=',',encoding='utf-8')

    if not new_col_pd.empty:
        engine = create_engine('mysql+mysqldb://root:passwd@localhost/db?charset=utf8',encoding="utf-8")
        new_col_pd.to_sql(table_name,engine,if_exists = 'append', index=False)
        print "data import down."

    # engine = create_engine("mysql+pymysql://{user}:{passwd}@{localhost}/{db}",
    #                        connect_args=dict(unix_socket="/path/to/mysql.sock"))
    # engine = create_engine('mysql+mysqldb://{user}:{pword}@{host}/{port}')
    #

if __name__ == '__main__':
    import_sql('.../SQL_Scripts/xxx.csv')

