import time,threading

#线程执行任务
def loop():
    print('thread:%s is running...'%threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.'% threading.current_thread().name)

if __name__ == "__main__":
    t=threading.Thread(target=loop,name='LoopThread')
    t.start()
    t.join() #等子线程结束
    print('thread %s ended'% threading.current_thread().name)