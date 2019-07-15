from multiprocessing import Process,Queue
import os,time,random

#写数据执行的函数
def write(q):
    print('进程写数据:%s'% os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue....'% value)
        q.put(value)
        time.sleep(random.random())

#读数据执行的代码
def read(q):
    print('进程读数据：%s'% os.getpid())
    while True:
        value=q.get(True)
        print('读取 %s from queue.'% value)


if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子继承pr,读取
    pr.start()
    #等待pw结束
    pw.join()
    #等待pr结束
    pr.join()
    pr.terminate()