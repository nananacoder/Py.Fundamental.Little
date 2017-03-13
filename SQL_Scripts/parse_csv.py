#!/usr/bin/python2.7
# -*-coding:utf-8-*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import csv
import MySQLdb

DB = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'xxxx',
        'db': 'xxxx',
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
    cur.close()
    conn.close()
    for res in datas:
        yield res

def show_columns(table_name):
    '''
    :return: a list of this table's columns
    '''
    # conn,cursor = connection()
    results = fetchall_sql("""desc %s""" % table_name)
    column_list = [r[0] for r in results]
    return column_list

def parse_modify(file_path):
    filehandle = open(file_path, 'rb')

    first_line = filehandle.readline()
    table_name = file_path.split('/')[-1].split('.')[0]

    new_col = show_columns(table_name)

    old_col = first_line.split()[0].split(',')
    deleted_col = [n for n in old_col if n not in new_col]
    needed_col = [n for n in new_col if n in old_col]

    deleted_index = [index for index, n in enumerate(old_col) if n not in new_col]
    added_col_index = [index for index, n in enumerate(new_col) if n not in old_col]
    # all_data = csv.reader(filehandle, old_col, delimiter=',')

    # filtered = (line.replace('\r', '') for line in filehandle)

    all_data = csv.reader(filehandle, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')

    if deleted_index == [] and added_col_index == []:
        pass
    else:
        with open(file_path, 'w') as newfile:
            spamwriter = csv.writer(newfile, delimiter=',',quoting=csv.QUOTE_NONE,quotechar='',escapechar='\\',
                                    lineterminator='\n')
            spamwriter.writerow(new_col)
    # #
            for data in all_data:
                for idx in deleted_index:
                    del data[idx]
                for num in added_col_index:
                    data.insert(num, '')
                spamwriter.writerow(data)


    # with open(file_path, 'w') as newfile:
    #     spamwriter = csv.writer(newfile, delimiter=',', lineterminator='\n')
    #     spamwriter.writerow(new_col)
    #
    #     for data in all_data:
    #         print data
    #         for ix in deleted_index:
    #             del data[ix]
    #         for num in added_col_index:
    #             data.insert(num, '')
    #         spamwriter.writerow(data)


    # import_sql = 'LOAD DATA LOCAL INFILE "%s" INTO TABLE `%s` CHARACTER SET UTF8 FIELDS TERMINATED BY "," LINES TERMINATED BY "\n" IGNORE 1 ROWS' % (file_path, table_name)

    # execute_sql(import_sql)

def export_table_csv(tb, _path):
    """
        SELECT * FROM [TABLE]
        INTO OUTFILE '[FILE]'
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
         LINES TERMINATED BY '\n'
    """
    # give mysql permission to write
    p = os.path.split(_path)[0]
    os.system('/usr/bin/chmod a+w %s' % p)
    export_sql = ('SELECT * FROM {table} INTO OUTFILE "{path}" '
                  'FIELDS TERMINATED BY "," '
                  'LINES TERMINATED BY "\n"')

    execute_sql(export_sql.format(table=tb, path=_path))

def writer_csv(table_name,file_path):


    sql = "SELECT * FROM %s " % table_name
    lines = fetchall_sql(sql)

    list_data = [list(line) for line in lines]
    column_list = show_columns(table_name)

    export_path = file_path + '/' + table_name + '.csv'

    with open(export_path, 'wb') as csvfile:
        # table_writer = csv.writer(csvfile, delimiter=',', quotechar='\'')
        table_writer = csv.writer(csvfile, delimiter=',', doublequote=False, escapechar='\\', lineterminator='\n',
                                  quoting=csv.QUOTE_NONE)
        table_writer.writerow(column_list)

        for data in list_data:
            table_writer.writerow(data)

if __name__ == '__main__':
    file_path = '.../SQL_Scripts/xxx.csv'
    parse_modify(file_path)
    # export_table_csv()

    # writer_csv('m_tbconfig', '/home/ankiy/ankiprojects/Scripts.Fundamental.Little/SQL_Scripts')
#