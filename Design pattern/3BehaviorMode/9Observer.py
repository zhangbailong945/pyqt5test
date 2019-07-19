'''
观察者模式
核心抽象对象管理所有依赖其他的其他类，并在设计中使其在发生变动时，
主动通知并更新其他类；也叫模型-视图模式，源-收听者模式，从属模式。
该模式必须包含两个橘色：观察者和被观察读写。
场景：
当客户减少到阈值时，销售通知工厂减少生产、人力资源开始裁人，反之增加。

'''

class Observer:
    '''挂穿着核心：西欧奥兽人员，被观察者number数据'''
    def __init__(self):
        self._number=None
        self._department=[]

    @property
    def number(self):
        return self._number
    @number.setter
    def number(self,value):
        self._number=value
        print('当前客户数：{}'.format(self._number))
        for obj in self._department:
            obj.change(value)
        print('--------')
    
    def notice(self,department):
        '''相关部门'''
        self._department.append(department)

class Hr:
    '''人事部门'''

    def change(self,value):
        if value<10:
            print('人事变动：裁员')
        elif value>20:
            print('人事变动：扩员')
        else:
            print("人事不受影响")


class Factory:
    '''工厂'''
    def change(self,value):
        if value<10:
            print('生产计划变动：减产')
        elif value>20:
            print('生产计划变动：增产')
        else:
            print("生产计划保持不变！")

if __name__ == "__main__":
    observer=Observer()
    hr=Hr()
    factory=Factory()
    observer.notice(hr)
    observer.notice(factory)
    observer.number=10
    observer.number=25
    observer.number=20
    observer.number=25
    observer.number=5