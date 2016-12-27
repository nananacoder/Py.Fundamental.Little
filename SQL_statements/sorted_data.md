##排序检索数据 

ORDER BY子句取一个或多个列的名字,据此对输出进行排序.

    mysql>SELECT prod_name 
          FROM Products 
          ORDER BY prod_name;

**_在指定一条ORDER BY子句时,保证这条子句是SELECT语句中最后一条语句._**

**_可以使用非检索的列排序数据._**

###按多个列进行排序
    mysql>SELECT prod_id,prod_price,prod_name 
          FROM Products 
          ORDER BY prod_price,prod_name;(首先按价格,然后按名称排序)
          
###按列位置排序
    mysql>SELECT prod_id, prod_price, prod_name
          FROM Products
          ORDER BY 2,3;
ORDER BY 2表示按SELECT清单中第二个列prod_price进行排序.
ORDER BY 2,3表示先按prod_price,再按prod_name进行排序.

**_不能对不出现在SELECT清单中的列进行排序._**

###指定排序方向
升序(A到Z) 降序(Z到A)
为了降序排序,必须指定DESC关键字.

以价格降序来排序产品(最贵的排在最前面):

    mysql>SELECT prod_id, prod_price, prod_name 
          FROM Products
          ORDER BY prod_price DESC;
          
          
多个列排:

    mysql>SELECT prod_id, prod_price, prod_name
          FROM Products
          ORDER BY prod_price DESC, prod_name;
DESC关键字只应用到直接位于其前面的列名.上例中,只对prod_price列指定DESC,对prod_name列不指定.
因此prod_price列以降序排序,而prod_name列(在每个价格内)仍然按标准的升序排序.

如果想在多个列上进行降序排序,必须对每一列指定DESC关键字.

_DESC= DESCENDING(降序)_
_ASC= ASCENDING(升序)(默认)_

