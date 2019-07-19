#备忘录模式
'''
在不破坏封闭的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。
这样以后就可将该对象恢复到原先保存的状态，简单来说在运行过程中我们可以记录
某个状态，当遇到错误时回复当前状态，这在业务流程中是用来设计处理异常情况。

'''

import copy

class AddNumber:

    def __init__(self):
        self.start=1

    def add(self,number):
        self.start+=number
        print(self.start)


class Memorandum:
    '''备忘录'''
    def backups(self,obj=None):
        self.obj_dict=copy.deepcopy(obj.__dict__)
        print("备份数据：{}".format(self.obj_dict))
    
    def recovery(self,obj):
        '''
        恢复备份方法
        '''
        obj.__dict__.clear()
        obj.__dict__.update(self.obj_dict)
        return obj


if __name__ == "__main__":
    test=AddNumber()
    memorandum=Memorandum()
    for i in [1,2,3,'n',4]:
        if i==2:
            memorandum.backups(test)
        try:
            test.add(i)
        except TypeError as e:
            print(e)
            print(test.start)
    memorandum.recovery(test)
    print(test.start)