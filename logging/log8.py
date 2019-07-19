from log7 import AppLogger


if __name__ == "__main__":
    appLogger=AppLogger(name='Value')
    ds={'a':1,'b':2,'c':3}
    

    app1=AppLogger(name='Model')
    app2=AppLogger(name='View')
    app1.info('test1')
    app2.info('test2')
    app1.info('哈哈哈')
    app1.warn('嘻嘻嘻')
    app1.critical('呃呃呃')
    app1.error('test3')
    app2.error('test4')
    print(app1)
    print(app2)

