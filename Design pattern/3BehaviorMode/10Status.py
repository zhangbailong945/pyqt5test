#状态模式
'''
状态模式，当对象的状态改变的时候，允许对象执行不同的流程。
看起来就像改写了一个对象、核心的方法是把复杂状态变化情况下的流程抽象出来，
简化复杂情况状态的判断。
场景：当状态时CPU使用率，在不同状态洗的自动化运维脚本执行不同的操作。
'''

class Base:

    def executor(self,value):
        self.run(value)

class Low(Base):

    def __init__(self):
        self.name='较低占用率'
    
    def run(self,value):
        print("当前：{}值：{}".format(self.name,value))
        print('无应急情况执行')

class Height(Base):

    def __init__(self):
        self.name="较高占用率"
    
    def run(self,value):
        print("当前：{}值：{}".format(self.name,value))
        print('发邮件警告')


class Statu:

    def __init__(self):
        self.value=0.1
        self.low=Low()
        self.height=Height()
        self.statu=None
    
    def monitor(self):
        if self.value <0.5:
            self.statu=self.low
        else:
            self.statu=self.height
        self.statu.executor(self.value)


if __name__ == "__main__":
    test=Statu()
    test.monitor()
    test.value=0.9
    test.monitor()