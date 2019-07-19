'''
日志文件按照时间划分或者按照大写划分
将日志保存在一个文件中，那么时间一长，或者日志一多，
单个日志文件会很大，即不利于备份，也不利于查看。我们回想到能不能
按照时间或者大小对日志文件进行划分。
logging.handlers文件中提供了TimedRotatingFileHandler和RotatingFileHandler类
分别可以实现按时间和大小划分。

'''

import logging

#每个1024 Byte划分一个日志文件，备份文件为3个
file_handler1=logging.handlers.RotatingFileHandler(
    filename='test.log',
    mode='w',
    maxBytes=1024,
    backupCount=2,
    encoding='utf-8'
)

#每个一小时划分一个日志文件，interval是时间间隔,备份1个
file_handler2=logging.handlers.TimedRotatingFileHandler(
    filename='test.log',
    when='H',
    interval=1,
    backupCount=1,
    encoding='utf-8'
)