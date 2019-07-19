import logging


log1=logging.getLogger()
log2=logging.getLogger()

print(str(log1))
print(str(log2))

#<RootLogger root (WARNING)>
#<RootLogger root (WARNING)>

log3=logging.getLogger(name='model')
log4=logging.getLogger(name='view')

print(str(log3))
print(str(log4))