#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MyFen.py
@Time    :   2019/04/04 16:56:51
@Author  :   Loach 
@Version :   1.0
@Contact :   1207549344@qq.com
@License :   (C)Copyright 2017-2019, loachblog.com
@Desc    :   None
'''

# here put the import lib
import random,time,queue

from multiprocessing.managers import BaseManager


#发送任务的队列
task_queue=queue.Queue()

#接受任务的队列
result_queue=queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

if __name__ == "__main__":
    #把两个Queue都注册到网络上,callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=lambda:task_queue)
    QueueManager.register('get_result_queue',callable=lambda:result_queue)
    #绑定端口号
    manager=QueueManager(address=('127.0.0.1',9000),authkey=b'loachblog')

    #启动Queue
    manager.start()

    #获得 通过网络访问的Queue对象
    task=manager.get_task_queue()
    result=manager.get_result_queue()

    #放任务
    for i in range(10):
        n=random.randint(0,10000)
        print('Put task %d...'% n)
        task.put(n)

    #result队列读取结果
    print('Try get results....')
    for i in range(10):
        r=result.get(timeout=10)
        print('Result:%s'% r)

    #关闭
    manager.shutdown()
    print('master exit.')