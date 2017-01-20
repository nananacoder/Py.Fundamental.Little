#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Usage:
   1. export db table to csv file:
       >python csv_to_table.py -e [table_name] -p [file path folder]

   2. import csv to db-new-table(table structure has been changed):
       >python csv_to_table.py -w [new table_name] -c [csv file path]


if one tries to use mysqlimport for files larger than 1 MB in size, one encounters errors.

Consequently, we need a program to import CSV files with the following functionality:
• The file is comma-separated (that is, not tab, space, or semi-colon)
• The file is written using the Excel dialect of CSV
• The user will indicate at runtime the filename as well as the database-table for the INSERT command
• The program will evaluate the file's size on disk and adapt its insertion strategy to fit within MySQL's defaults
'''

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb
import optparse
import os
import csv
import ast
import logging

logging.basicConfig(level=logging.INFO, filename='error.log')



opt = optparse.OptionParser()
opt.add_option("-e", "--export", action="store", type="string",
               help="table name which need to back up", dest="table_name")
opt.add_option("-p", "--exportpath", action="store", type="string", default= "./",
               help="the folder path of exported csv file", dest="export_path")
opt.add_option("-w", "--write", action="store", type="string",
               help="new table name that need data to insert", dest="new_table_name")
opt.add_option("-c", "--writepath", action="store", type="string",
               help="the csv file path that need insert to mysql", dest="csv_path")

options, args = opt.parse_args()

old_table_name = options.table_name
export_path = options.export_path

new_table_name = options.new_table_name
import_path = options.csv_path

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
    conn.escape_string()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print e
        logging.info("ERROR SQL: %s" % sql)
        conn.rollback()
    conn.close()

def executemany_sql(sql,args):
    """
        执行sql语句
        args:
            sql: 要重复执行的SQL语句
            args: 一个列表,列表中的元素为SQL语句的参数(Tuple)
    """
    if args == []:
        return
    conn = MySQLdb.connect(**DB)
    # conn.escape_string()
    cur = conn.cursor()
    try:
        affected = cur.executemany(sql,args)
        conn.commit()
        return affected
    except Exception as e:
        conn.rollback()
        print e
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

def show_tables():
    sql = "show tables"
    lines = fetchall_sql(sql)
    return [i[0] for i in lines]

def writer_csv(table_name,file_path):


    sql = "SELECT * FROM %s " % table_name
    lines = fetchall_sql(sql)

    list_data = [list(line) for line in lines]
    column_list = show_columns(table_name)

    export_path = file_path + '/' + table_name + '.csv'
    with open(export_path, 'wb') as csvfile:
        # table_writer = csv.writer(csvfile, delimiter=',', escapechar="'", quotechar='\'')
        # table_writer = csv.writer(csvfile, delimiter=',',lineterminator='/n')
        table_writer = csv.writer(csvfile, delimiter=',', doublequote=False, escapechar='\\', lineterminator='\n',
                                  quoting=csv.QUOTE_NONE)
        table_writer.writerow(column_list)

        for data in list_data:
            table_writer.writerow(data)

def export_all():
    tables = show_tables()

    for c in tables:
        writer_csv(c, './csvfile/')
        print c,"write down"


class ImportCsvTable(object):

    def __init__(self, file_path, new_table):

        self.file_path = file_path
        self.old_table = file_path.split('.')[0]
        self.new_table = new_table

        self.new_col = show_columns(new_table)

    def convert(self):
        """
        Processes contents of csv file
        :return: a dictionary for wanted column and each record
        """
        filehandle = open(self.file_path)
        first_line = filehandle.readline()

        old_col = first_line.split()[0].split(',')
        deleted_col = [n for n in old_col if n not in self.new_col]
        needed_col = [n for n in self.new_col if n in old_col]

        sheet = csv.DictReader(filehandle, old_col, delimiter=',')

        result_dic = []
        r = 1
        for old_dic in sheet:
            print r
            # if len(old_dic) != len(old_col):
            #     print old_dic
            #     continue
            for d in deleted_col:
                del old_dic[d]

            result_dic.append(old_dic)
            r+=1

        return result_dic, needed_col

    def main(self):
        """the main function creates the MySQL statement in accordance
        with the user's input and using  convert(), and os.path.getsize().

        """

        data, fields = self.convert()

        str_fields = ','.join(fields)
        file_size = os.path.getsize(self.file_path)

        values = []
        r = 0

        import pytest
        pytest.set_trace()
        for record in data:
            value = ''
            for column_no in xrange(0, len(fields)):
                if column_no == 0:
                    value = '"' + record[fields[column_no]]
                else:
                    value += '", "' + record[fields[column_no]]
            value += '"'

            if file_size <= 1000000:
                import pytest
                pytest.set_trace()
                # value = eval(value)
                value = ast.literal_eval(value)

                values.append(value)

            else:
                query = """INSERT INTO %s (%s) VALUES """ % (self.new_table, str_fields)

                statement = query + "(" + value + ")"
                # statement = query + str(value)

                execute_sql(statement)


            r += 1

        if file_size <= 1000000:
            query = "INSERT INTO " + self.new_table + "(" + str_fields + ") VALUES (%s"
            for i in xrange(0, len(fields)-1):
                query += ", %s"
            query += ")"
            query = str(query)
            #
            # import pytest
            # pytest.set_trace()
            affected = executemany_sql(query, values)
            print self.new_table,affected, "row affected.(file size<1MB)"
        else:
            print self.new_table,r, "row affected.(file size>1MB)"

def import_all():

    new_tables = show_tables()


    csv_folder = '..../csvfile'
    csv_path = lambda f:csv_folder + '/' + f + '.csv'

    for t in new_tables:
        c_path = csv_path(t)
        if os.path.exists(c_path):
            ict = ImportCsvTable(c_path, t)
            ict.main()
            


if __name__ == '__main__':
    if old_table_name and export_path:
        writer_csv(old_table_name, export_path)
    if new_table_name and import_path:
        ImportCT = ImportCsvTable(import_path, new_table_name)
        print "start import..."
        ImportCT.main()


