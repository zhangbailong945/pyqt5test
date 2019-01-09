'''
queue 队列
Python 的 Queue 模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，
和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，
可以使用队列来实现线程间的同步
qsize() 返回队里大小
empty() 队列为空，返回True
full() 队列满了，返回True
full 大小
get(block,timeout) 获取队列，timeout等待时间
get_nowwait() 相当于get(False)
put(item) 写入队列
put_nowait(item) 相当于put(False)
task_done() 对已完成的队列放一个信号
join() 等到队列为空，再进行别的操作

'''

import queue,threading,time

exitFlag=0

class MyThread(threading.Thread):

    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q
    
    def run(self):
        print('开启线程:'+self.name)
        process_data(self.name,self.q)
        print('退出线程'+self.name)

queueLock=threading.Lock()
workQueue=queue.Queue(10)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=q.get()
            queueLock.release()
            print("%s processing %s"%(threadName,data))
        else:
            queueLock.release()
        time.sleep(1)

threadList=['Thread-1','Thread-2','Thread-3']
nameList=['One','Two','Three','Four','Five']

threads=[]
threadID=1

#创建新线程
for tName in threadList:
    thread=MyThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

#等待队列清空
while not workQueue.empty():
    pass

#通知线程是时候退出
exitFlag=1

for t in threads:
    t.join()

print('退出主线程')
