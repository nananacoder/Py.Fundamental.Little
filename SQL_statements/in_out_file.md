##导入.导出

##mysqldump > sql文件

    1导出數據库為dbname的表结构（其中用戶名為root,密码為dbpasswd,生成的脚本名為db.sql）
    mysqldump -uroot -pdbpasswd -d dbname >db.sql;

    2、导出數據库為dbname某张表(test)结构
    mysqldump -uroot -pdbpasswd -d dbname test>db.sql;

    3、导出數據库為dbname所有表结构及表數據（不加-d）
    mysqldump -uroot -pdbpasswd  dbname >db.sql;

    4、导出數據库為dbname某张表(test)结构及表數據（不加-d）
    mysqldump -uroot -pdbpasswd dbname test>db.sql;
    
###导出csv文件

    mysql>SELECT * FROM [TABLE]
          INTO OUTFILE '[FILE]'
          FIELDS TERMINATED BY ','
          OPTIONALLY ENCLOSED BY '"'
          LINES TERMINATED BY '\n';


secure_file_priv设置了指定目录，需要在指定的目录下进行数据导出


    mysql>show variables like '%secure%';


| Variable_name            | Value                 |
|:------------------------:|:---------------------:|
| require_secure_transport | OFF                   |
| secure_auth              | ON                    |
| secure_file_priv         | /var/lib/mysql-files/ |


