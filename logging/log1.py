import logging

#不带参数
'''
logging.basicConfig()
logging.debug('This is a debug message!')
logging.info('This is a info message!')
logging.warning('This is a warning message!')
logging.error('This is a error message!')
logging.critical('This is a critical message!')
'''


#带参数的
'''
logging.basicConfig(filename='test.log',filemode='w',format="%(asctime)s %(name)s:%(levelname)s:%(message)s",datefmt="%d-%M-%Y %H:%M:%S",level=logging.DEBUG)
logging.debug('This is a debug message!')
logging.info('This is a info message!')
logging.warning('This is a warning message!')
logging.error('This is a error message!')
logging.critical('This is a critical message')
'''

#当异常发生时，直接用无参数的debug(),info(),error(),warning(),critical()方法
#不能记录异常信息，需要设置exc_info参数为True才可以，或者使用exception()方法，
#还可以使用log()方法，但还要设置日志级别和exc_info参数。

logging.basicConfig(
    filename='test.log',
    filemode='w',
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    datefmt="%y-%M-%D %H:%M:%S",
    level=logging.DEBUG
)

a={"a":'a',"b":'b',"c":'c'}
try:
    print(a['d'])
except KeyError as e:
    logging.exception("{}".format(e))
    logging.error("{}".format(e),exc_info=True)
    logging.log(level=logging.DEBUG,msg="{}".format(e),exc_info=True)


