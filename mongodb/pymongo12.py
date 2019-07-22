'''
修改多个文档
'''

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


query={'title':"这是一个测试"}
newvalue={"$set":{"title":"sssssssssssssss"}}
col.update_many(query,newvalue)