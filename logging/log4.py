'''
中文乱码

1.自定义Logger对象，需要写很多配置，设置encoding="utf-8"

2.默认配置方法,在其中的handler设置文件编码.
'''

import logging

#第一种
handler=logging.FileHandler(filename="test.log",encoding="utf-8")

#第二种
logging.basicConfig(
    handlers=[
        logging.FileHandler("test.log",encoding="utf-8")
    ],
    level=logging.DEBUG
)

#临时禁用日志输出
#默认配置 
'''
logging.disable()方法传入禁用的日志级别，就可以禁止设置级别以下的日志输出。
'''
logging.disable(logging.INFO)

#自定义Logger，将该对象disable属性设置为True,即可禁用。
logger.disabled=True