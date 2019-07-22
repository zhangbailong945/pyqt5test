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

post=col.find({},{"_id":0,"title":0})
for p in post:
    print(p)