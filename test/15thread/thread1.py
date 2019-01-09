#多线程
'''
threading.currentThread(): 返回当前的线程变量
threading.enumrate(): 返回一个包含正在运行的线程的list.
threading.activeCount(): 返回正在运行的线程数量

#Thread类提供了一下方法：
run() :用以表示线程活动的方法
start() :启动线程活动
join(time): 等待至线程中止，这阻塞调用线程
直至线程的join()方法被调用中止-正常退出或者抛出未处理的异常
-或者是可选的超时发送。
isAlive(): 返回线程是否活动的
getName() : 返回线程的名称
setName() : 设置线程的名称

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
        print_time(self.name,self.counter,5)
        print('退出线程:'+self.name)
    
def print_time(name,delay,counter):
    while counter:
        if exitFlag:
            name.exit()
        time.sleep(delay)
        print("%s:%s"%(name,time.ctime(time.time())))
        counter-=1


thread1=MyThread(1,'TH1',1)
thread2=MyThread(2,'TH2',2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("退出主线程")