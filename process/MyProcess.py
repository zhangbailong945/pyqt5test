from multiprocessing import Process
import os

def run_proc(name):
    print('子进程 %s (%s)'%(name,os.getpid()))


if __name__=='__main__':
    print('主进程%s'% os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('child process wile start.')
    p.start()
    p.join()
    print('Chid process end.')