import pymongo
import time
from pymongo import MongoClient

dbname="test"

client=MongoClient("mongodb://localhost:27017")
dbHandler=client['test']
col=dbHandler['post']
dblist=client.list_database_names()
collist=dbHandler.list_collection_names()
if dbname not in dblist:
    print('数据库不存在!')

if 'post' not in collist:
    print('集合不存在！')

created_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
## 添加数据
plist=[
    {
        "title":'这是一个测试1',
        "content":"这是内容1",
        "create_time":created_time
    },
    {
        "title":'这是一个测试2',
        "content":"这是内容2",
        "create_time":created_time
    }
    ,
    {
        "title":'这是一个测试3',
        "content":"这是内容3",
        "create_time":created_time
    }
]
x=col.insert_many(plist)
print(x.inserted_ids)