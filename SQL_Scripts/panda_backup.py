#!/usr/bin/python2.7
# -*-coding:utf-8-*-

import os
import sys
import time
import shutil
import zipfile

import MySQLdb
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# tmp_dirpath = '/usr/local/bluedon/tmp'

tmp_dirpath = '.../SQL_Scripts'

DB = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'xxx',
        'db': 'xxx',
        'charset': 'utf8',
        }

# DB = {
#         'host': 'localhost',
#         'port': 3306,
#         'user': 'root',
#         'passwd': 'passwd',
#         'db': 'db',
#         'charset': 'utf8',
#         'use_unicode':True,
#         'unix_socket': 'xxxx.sock'
#         }

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

def fetchone_sql(sql):
    """
    执行sql语句
    args:
        sql: 查询的sql语句
    return:
        datas: 查询的记录集
    """

    conn = MySQLdb.connect(**DB)
    cur = conn.cursor()
    cur.execute(sql)
    datas = cur.fetchone()
    conn.close()
    return datas

def fetchall_sql(sql):
    """
    执行sql语句
    args:
        sql: 查询的sql语句
    return:
        datas: 查询的记录集Iterable对象
    """

    conn = MySQLdb.connect(**DB)
    cur = conn.cursor()
    cur.execute(sql)
    datas = cur.fetchall()
    conn.close()
    for res in datas:
        yield res



def zip_folder(output_zip, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, sub_dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)


def unzip_folder(zip_path):
    zipf = zipfile.ZipFile(zip_path, 'r')
    # If the output location does not yet exist, create it
    # if not os.path.isdir(path):
    #     os.makedirs(path)

    for each in zipf.namelist():

        # Check to see if the item was written to the zip file with an
        # archive name that includes a parent directory. If it does, create
        # the parent folder in the output workspace and then write the file,
        # otherwise, just write the file to the workspace.
        #
        if not each.endswith('/'):
            root, name = os.path.split(each)
            directory = os.path.normpath(os.path.join(tmp_dirpath, root))
            if not os.path.isdir(directory):
                os.makedirs(directory)
            file(os.path.join(directory, name), 'wb').write(zipf.read(each))

    return os.path.join(tmp_dirpath,os.path.split(zip_path)[-1].split('.')[0])


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

    if_exits_table = "SHOW TABLES LIKE '%{table_name}%';".format(table_name=table_name)
    exits_re = fetchone_sql(if_exits_table)

    if not exits_re:
        print "%s doesn't exits in database now." % table_name
        return

    new_col = show_columns(table_name,indx=csv_input.index)


    new_col_index =  new_col.columns
    old_col_index =  csv_input.columns

    for n_col in new_col_index:
        if n_col in old_col_index:
            new_col[n_col] = csv_input[n_col]


    return  new_col, table_name


def export_data(db,table_name,dir_path):

    conn = MySQLdb.connect(**db)
    sql = 'select * from `%s`;' % table_name
    df = pd.read_sql(sql, con=conn)
    conn.close()

    file_name = dir_path + '/' + table_name + '.csv'
    df.to_csv(file_name, index=False,sep=',',encoding='utf-8', quoting=1)
    return df

def export_multi(db):
    """
    backup all tables of one datebase to multi csv files
    the file path is ../bluedon/tmp

    :param db: database config
    """
    db_name = db['db']
    today = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    folder_name = db_name + today
    # current_path = os.getcwd()

    new_dir_path = os.path.join(tmp_dirpath,folder_name)
    if not os.path.isdir(new_dir_path):
        os.makedirs(new_dir_path)

    fet_sql = "select table_name from information_schema.tables where table_schema='%s';" % db['db']
    tables = fetchall_sql(fet_sql)
    for table in tables:
        table_name = str(table[0])
        # print table_name, type(table_name)
        export_data(db, table_name,dir_path=new_dir_path)
    else:
        if os.listdir(new_dir_path):
            zipfile = os.path.join(tmp_dirpath,folder_name+'.zip')
            zip_folder(output_zip=zipfile,source_dir=new_dir_path)

        if os.path.exists(new_dir_path):
            shutil.rmtree(new_dir_path,ignore_errors=True)



def import_sql(file_name):

    csv_result = rd_csv(file_name)
    if not csv_result:
        return

    new_col_pd, table_name = csv_result

    # new_col_pd.to_csv(file_name, index=False,sep=',',encoding='utf-8')


    if not new_col_pd.empty:
        truncate_sql = "TRUNCATE TABLE `%s`" % table_name
        execute_sql(truncate_sql)

        engine = create_engine('mysql+mysqldb://root:passwd@localhost/db?charset=utf8', encoding="utf-8")
        # engine = create_engine('mysql+mysqldb://root:passwd@localhost:port/db?charset=utf8',
        #                        connect_args={'unix_socket':'xxx.sock'},
        #                        encoding="utf-8")
        try:
            new_col_pd.to_sql(table_name, engine, if_exists='append', index=False)
        except OperationalError as error:
            # if error_info.find('1048') and error_info.find('cannot be null'):
            table_structure = fetchall_sql("describe `%s`" % table_name)
            tb_stc = [str(t[0]) for t in table_structure if str(t[2]) == 'YES']

            include_none_pd = pd.notnull(new_col_pd)
            # include_none_pd= new_col_pd.isnull().any()

            for ts in tb_stc:
                # include_none_pd.ts[include_none_pd.ts == False] = True
                include_none_pd[ts] = True
            new_col_pd = new_col_pd.astype(object).where(include_none_pd, "")
            new_col_pd.to_sql(table_name, engine, if_exists='append', index=False)

        # try:
        #     new_col_pd.to_sql(table_name,engine,if_exists = 'append', index=False)
        # except OperationalError as error:
        #     error_info = error.message
        #     if error_info.find('1048') and error_info.find('cannot be null'):
        #         err_column = error_info.split(',')[1].split()[1]
        #         import pytest
        #         pytest.set_trace()
        #         new_col_pd = new_col_pd.astype(object).where(pd.notnull(new_col_pd), "")
        #         new_col_pd.to_sql(table_name, engine, if_exists='append', index=False)

        print "%s import down." % table_name

    # engine = create_engine("mysql+pymysql://{user}:{passwd}@{localhost}/{db}",
    #                        connect_args=dict(unix_socket="/path/to/mysql.sock"))
    # engine = create_engine('mysql+mysqldb://{user}:{pword}@{host}/{port}')
    #

def import_multi(zip_path):
    backup_folder = unzip_folder(zip_path)

    if os.listdir(backup_folder):
        for root, dirs, files in os.walk(backup_folder):
            for file in files:
                try:
                    import_sql(os.path.join(root,file))
                except Exception as e:
                    print file


if __name__ == '__main__':

    # show_columns('m_tbconfig')
#
    # export_data(db=DB,table_name='m_tbaddress_list')

    # export_multi(db=DB)

    import_multi('aaare20170210_10:03:09.zip')
    # import_sql('.../SQL_Scripts/aaare20170210_10:03:09/m_tbndpi_protocol.csv')
    # import_sql('../SQL_Scripts/aaare20170210_10:03:09/m_tbfwsessionstatus.csv')
    # import_sql('tmp2.csv')

