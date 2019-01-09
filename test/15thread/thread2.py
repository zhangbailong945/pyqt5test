#多线程
'''
线程同步
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，
为了保证数据的正确性，需要对多个线程进行同步。

使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，
这两个对象都有 acquire 方法和 release 方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 
acquire 和 release 方法之间
'''

import threading,time

exitFlag=0

class MyThread(threading.Thread):

    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    
    def run(self):
        print('开始线程:'+self.name)
        #获取锁
        threadLock.acquire()
        print_time(self.name,self.counter,5)
        threadLock.release()
        #释放锁
        print('退出线程:'+self.name)
    
def print_time(name,delay,counter):
    while counter:
        if exitFlag:
            name.exit()
        time.sleep(delay)
        print("%s:%s"%(name,time.ctime(time.time())))
        counter-=1


threadLock=threading.Lock()
threads=[]


thread1=MyThread(1,'TH1',1)
thread2=MyThread(2,'TH2',2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("退出主线程")