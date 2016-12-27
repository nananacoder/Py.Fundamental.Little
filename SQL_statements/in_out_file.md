##导入.导出

###导出csv文件

    mysql>SELECT * FROM [TABLE]
          INTO OUTFILE '[FILE]'
          FIELDS TERMINATED BY ','
          OPTIONALLY ENCLOSED BY '"'
          LINES TERMINATED BY '\n';


secure_file_priv设置了指定目录，需要在指定的目录下进行数据导出


    mysql>show variables like '%secure%';

+--------------------------+-----------------------+
| Variable_name            | Value                 |
+--------------------------+-----------------------+
| require_secure_transport | OFF                   |
| secure_auth              | ON                    |
| secure_file_priv         | /var/lib/mysql-files/ |
+--------------------------+-----------------------+

