import time

ticks=time.time()
print('多少秒:%s',ticks)

#当前时间
localtime=time.localtime(time.time())
print('本地时间:',localtime)

#格式化日期
print(time.strftime('%Y-%m-%d %H:%M:S',time.localtime()))

