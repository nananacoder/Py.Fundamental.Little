##过滤数据


SELECT语句中,数据根据WHERE子句中的指定搜索条件进行过滤

    mysql>SELECT prod_name, prod_price
          FROM Products
          WHERE prod_price =3.49;
从Products表中检索两个列,但不返回所有行,只返回prod_price值为3.49的行


###WHERE子句操作符


|          操作            |        说明           |   |  
| -----------------------  |:--------------------: |: -----:|
|          =               | 等于                  |
|          <>              | 不等于                |
|          !=              | 不等于                |
|          <               | 小于                  |
|          <=              | 小于等于              |
|          !<              | 不小于                |
|          >               | 大于                  |
|          >=              | 大于等于              |
|          !>              | 不大于                |
|          BETWEEN         | 在指定的两个值之间    |
|          IS NULL         | 为NULL值              |



例子:

所有价格小于是10美元的产品:

    mysql>SELECT prod_name, prod_price 
          FROM Products
          WHERE prod_price < 10;
          
所有不是供应商DLL01制造的产品:

    mysql>SELECT vend_id, prod_name
          FROM Products
          WHERE vend_id <> 'DLL01';
_单引号用来限定字符串.如果将值与字符串类型的列进行比较,就需要限定引号.用来与数值列进行比较的值不用引号._


**范围值检查:**
    
    mysql>SELECT prod_name, prod_price
          FROM Products
          WHERE prod_price BETWEEN 5 AND 10;

**空值检查:**

    mysql>SELECT prod_name
          FROM Products
          WHERE prod_price IS NULL;


##组合where过滤

AND操作符:用在where子句中的关键字,用来指示检索满足所有给定条件的行.
    
    mysql>SELECT prod_id, prod_price, prod_name
          FROM Products
          WHERE vend_id = 'DLL01' AND prod_price <= 4;

OR操作符:检索匹配任一条件的行.(在第一个条件满足时,不管第二个条件是否满足,相应的行都将被检索出来.)

    mysql>SELECT prod_id, prod_price, prod_name
          FROM Products
          WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';