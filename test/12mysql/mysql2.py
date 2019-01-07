import pymysql

#打开数据库
db=pymysql.connect('localhost',"root",'root','mytest')

#创建游标对象
cursor=db.cursor()
#execute() 方法执行sql

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print("Database Version:%s"% data)
'''
cursor.execute("DROP TABLE IF EXISTS employee")

#预处理语句创建表
sql=CREATE TABLE employee(
    id int auto_increment primary key,
    first_name char(20) not null,
    last_name char(20),
    age int,
    sex char(1),
    income float
)'''




sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""


try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[1]
      lname = row[2]
      age = row[3]
      sex = row[4]
      income = row[5]
       # 打印结果
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()


# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

#关闭数据库
db.close()