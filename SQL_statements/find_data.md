##检索

表名:Products

###检索某列:

    mysql>>SELECT prod_name FROM Products;

###检索多个列:
    mysql>>SELECT prod_id, prod_name, prod_price FROM Products;

###检索所有列(通配符*)
    mysql>>SELECT * FROM Products;

###检索不同的值
    mysql>>SELECT DISTINCT vend_id FROM Products;
     (不能部分使用DISTINCT)
 
###检索 最多返回多少行
    mysql>>SELECT prod_name FROM Products LIMIT 5;(前5行数据)
    mysql>>SELECT prod_name FROM Products LIMIT 5 OFFSET 5;(从第5行开始的5行数据)

LIMIT指定返回的行数,LIMIT带的OFFSET指定从哪儿开始.

MySQL和MariaDB支持简化版的LIMIT 4 OFFSET 3语句,即LIMIT3,4.逗号之前的值对应OFFSET,逗号之后的值对应LIMIT.

###注释
行内注释: `--`
多行注释: `/*......*/`

