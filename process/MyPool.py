from multiprocessing import Pool
import os,time,random


def do_other_task(name):
    print('Run task %s(%s)'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s run %0.2f seconds.'%(name,(end-start)))

if __name__=="__main__":
    print('主进程 %s'% os.getpid())
    p=Pool(5)
    for i in range(5):
        p.apply_async(do_other_task,args=(i,))
    print('waiting for all subprocesses done ...')
    p.close()
    p.join()
    print('all subprocesses done.')