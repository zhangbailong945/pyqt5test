'''
自定义Logger

一个系统只要一个Logger对象，并且该对象不能被直接实例化，没错，这里用到了单例模式，
获取Logger对象的方法为getLogger().
注意：
这里的单例模式并不是说只有一个Logger对象，而是整个app系统只有一个根Logger对象，
Logger对象在执行info()、error()等方法时实际上调用都是跟Logger对象对应的info()、error()

可以创造多个Logger对象，但是真正输出日志的是根Logger对象。每个Logger对象都可以
设置一个名字，如logger=logging.getLogger(__name__)，__name__是python中的一个特殊
内置变量，代表当前模块的名称。

Logger对象可以设置多个Handler对象和Filter对象，Handler对象有可以设置Formatter对象。
常用变量格式： 
变量      格式    变量描述
asctime   %(asctime)s  将日志的时间构造可读的形式,可指定datefmt 参数格式化
name      %(name)s   日志对象的名称
filename  %(filename)s 不包含路径的文件名
pathname  %(pathname)s 包含路径的文件名
funcName  %(funcName)s 日志记录所在的函数名
levelname %(levelname)s 日志的级别名称
message   %(message)s  具体的日志信息
lineno    %(lineno)d 日志记录所在的行号
process   %(process)d 当前进程ID
processName %(processName)s 当前进程名称
thread     %(thread)d 当前线程ID
threadName %(threadName)s 当前线程名称

Logger对象和Handler对象都可以设置节本，而默认Logger对象级别为30，即WARNING，
moreHandler对象级别为0，即NOTSET。logging模块这样设计师为了更好的灵活性，比如
有时我们即想在控制台输出DEBUG级别的日志，又想在文件中输出WARNING级别的日志，
可以只设置一个最低级别的Logger对象，两个不同级别的Handler对象。

'''
import logging
import logging.handlers


logger=logging.getLogger("logger")
handler1=logging.StreamHandler()
handler2=logging.FileHandler(filename="test.log")

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s %(name)s:%(levelname)s %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)


print(handler1.level) #10
print(handler2.level) #30
print(logger.level)  #10


logger.debug('This is a customer debug message')
logger.info('This is an customer info message')
logger.warning('This is a customer warning message')
logger.error('This is an customer error message')
logger.critical('This is a customer critical message')