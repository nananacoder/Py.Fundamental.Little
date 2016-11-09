#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Aim to split large sql file to multi small sql files within a folder.

This split file is specific for some sql file started with some format.

It can modified later to use.
'''

import sqlparse

sql_file = "test.sql"

sql = open(sql_file).read()
sql_part = ''
sql_parts = sqlparse.split(sql, encoding="utf-8")

for i in range(len(sql_parts)):

    if sql_parts[i].find('DROP TABLE IF EXISTS ') >= 0:
        content = ''

        parsed = sqlparse.parse(sql_parts[i], encoding="utf-8")
        stmt = parsed[0]
        comments = str(stmt.tokens[0])

        table_name = str(stmt.tokens[-2]).strip('`')

        if comments.find('Records of') >= 0:
            comments_split = comments.splitlines()[-3:]
            start_comments = "\n".join(comments_split)
            del stmt.tokens[0]

            content = start_comments + "\n" + str(stmt) + sql_parts[i+1]

            # print content
        else:
            content = sql_parts[i] + sql_parts[i+1]

            # print content

        if sql_parts[i+2].find('Records of'):

            parsed_2 = sqlparse.parse(sql_parts[i+2], encoding="utf-8")
            stmt_2 = parsed_2[0]
            comments_2 = str(stmt_2.tokens[0])

            if sql_parts[i+2].find(';') < 0:
                content = content + sql_parts[i + 2]
            elif sql_parts[i+2].find('DROP') >= 0:
                comments_2_split = comments_2.splitlines()[0:2]
                end_comments = "\n".join(comments_2_split)

                # content = content + end_comments
            elif sql_parts[i+2].find('INSERT INTO') >=0:
                print sql_parts[i+2]


            # print comments_2


        # print comments.splitlines()
        # content = ''
        # content.append
