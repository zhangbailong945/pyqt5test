import logging


'''
日志
日志级别：
1.notset(0)
2.debug(10)
3.info(20)
4.warning(30)
5.error(40)
6.critical(50)

基本用法：

logging.BasciConfig(filename,filemode,format,datefmt,sytle,level,steam,handles)
参数：
1.filename 日志文件名
2.filemode 日志文件读写模式 r[+] w[+] a[+]
3.format 日志输出格式
4.datefmt 日志附带日期时间的格式
5.style
6.level 设置日志输出级别
7.stream 定义输出流，不能filename一起使用
8.handles 定义处理器，不能和filename、stream参数使用

'''

logging.basicConfig(
    filename='test.log',
    filemode="w+",
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG
)

logging.info("info")
logging.debug('debug')
logging.error('error')
logging.warn('warning')
logging.critical('critical')







