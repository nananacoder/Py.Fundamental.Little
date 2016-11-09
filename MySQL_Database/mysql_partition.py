import MySQLdb


con = MySQLdb.connect(
        host="localhost", user="root", passwd="123456",
        db="testDB", charset="utf8",
    )
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS T1(ID INT PRIMARY KEY AUTO_INCREMENT, INFO VARCHAR(255))")
    cur.execute("CREATE TABLE IF NOT EXISTS T2(ID INT PRIMARY KEY AUTO INCREMENT, INFO VARCHAR(255))")
    cur.execute("INSERT INTO T1 (INFO) VALUES ('Testing'),('table'),('t1')")
    cur.execute("INSERT INTO T2 (INFO) VALUES ('Testing'),('table'),('t2')")
    cur.execute("CREATE TABLE IF NOT EXISTS TOTAL(ID INT PRIMARY KEY AUTO_INCREMENT, INFO VARCHAR(255)) ENGINE=MERGE UNION=(T1, T2) INSERT_METHOD=LAST")

con.close()