import mysql.connector
#连接mysql数据库
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database='mytest',
)

#创建游标
mycursor=mydb.cursor()
#查看数据库
#mycursor.execute("SHOW DATABASES")
#创建数据库
#mycursor.execute("CREATE DATABASE mytest")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mytest"
)
mycursor = mydb.cursor()
 
#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

#显示数据表
#mycursor.execute("SHOW TABLES")

#mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


#插入数据
sql="INSERT INTO sites(name,url)values(%s,%s)"
#单个插入
'''
val=("loachblog","https://www.loachblog.com")
mycursor.execute(sql,val)
'''
#批量插入
val1=[
    ('google','https://www.google.com'),
    ('Github','https://www.github.com'),
    ('taobao','https://www.taobao.com'),
]
mycursor.executemany(sql,val1)
mydb.commit()
print(mycursor.rowcount,"记录插入成功!")

#插入后获取id,mysursor.lastrowid

#查询数据
mycursor.execute("SELECT * FROM sites")
myresult=mycursor.fetchall() #获取素有记录

for row in myresult:
    print(row)


#查询指定字段
mycursor.execute("SELECT name,url FROM sites")
myresult=mycursor.fetchall() #获取素有记录

for row in myresult:
    print(row)


#查询一条数据
'''
mycursor.execute("SELECT * FROM sites")
myresult=mycursor.fetchone()#获取单条数据
print(myresult)
'''

#where 条件
#查询指定字段
mycursor.execute("SELECT * FROM sites where id=3")
myresult=mycursor.fetchall() #获取素有记录


for row in myresult:
    print(row)



#通配符
mycursor.execute("SELECT * FROM sites where url LIKE '%o%'")
myresult=mycursor.fetchall() #获取素有记录


for row in myresult:
    print(row)

#排序 ORDER BY ASC升序，DESC降序
mycursor.execute("SELECT * FROM sites ORDER BY name")
myresult=mycursor.fetchall() #获取素有记录


for row in myresult:
    print(row)


#指定读取数据量limit
mycursor.execute("SELECT * FROM sites limit 3")
myresult=mycursor.fetchall() #获取


for row in myresult:
    print(row)

#读取的起始位置OFFSET
mycursor.execute("SELECT * FROM sites limit 3 OFFSET 2")
myresult=mycursor.fetchall() #获取


for row in myresult:
    print(row)


#删除
'''
为了防止SQL依赖注入用%s占位符
'''
sql = "DELETE FROM sites WHERE name = 'google'"
 
mycursor.execute(sql)
 
mydb.commit()
 
print(mycursor.rowcount, " 条记录删除")

#更新
sql = "UPDATE sites SET name = 'tmall' WHERE name = 'taobao'"
 
mycursor.execute(sql)
 
mydb.commit()
 
print(mycursor.rowcount, " 条记录被修改")


#删除表

sql = "DROP TABLE IF EXISTS sites"
 
mycursor.execute(sql)

