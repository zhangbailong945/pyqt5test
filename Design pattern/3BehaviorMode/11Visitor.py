'''
访问者模式数据结构中保存着许多元素，当改变一种对元素的处理方式时，我们
避免重复的修改数据类的结构，那么在设计之初就将数据的处理分离，即数据类只提供
一个数据处理接口，而数据类的处理方法我们叫它访问者，那么相同结构的数据面临
不同的处理结果时，我们只需创建不同的访问者。
场景：
上市公司的原始财务数据，对于会计来说需要制作各种报表，对于财务总结来说需要分析公司业绩，
对于战略顾问来说需要分析行业变化。
'''


class Finance:

    def __init__(self):
        #销售额
        self.salesvolume=None
        #成本
        self.cost=None
        #历史销售额
        self.history_salesvolume=None
        #历史成本
        self.history_cost=None
    
    def set_salesvolume(self,value):
        self.salesvolume=value
    
    def set_cost(self,value):
        self.cost=value
    
    def set_history_salesvolume(self,value):
        self.history_salesvolume=value
    
    def set_history_cost(self,value):
        self.history_cost=value
    
    def accept(self,visitor):
        pass


class Finance_year(Finance):

    def __init__(self,year):
        Finance.__init__(self)
        self.work=[]
        self.year=year
    
    def add_work(self,work):
        self.work.append(work)
    
    def accept(self):
        for obj in self.work:
            obj.visit(self)
    

class Accounting:

    def __init__(self):
        self.ID="会计"
        self.Duty="计算报表"
    
    def visit(self,table):
        print('会计年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        print('本年度纯利润： {}'.format(table.salesvolume - table.cost))
        print('------------------')
    

class Audit:
    """财务总监类"""

    def __init__(self):
        self.ID = "财务总监"
        self.Duty = "分析业绩"

    def visit(self, table):
        print('会计总监年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if table.salesvolume - table.cost > table.history_salesvolume - table.history_cost:
            msg = "较同期上涨"
        else:
            msg = "较同期下跌"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Adviser:
    """战略顾问"""
    def __init__(self):
        self.ID = "战略顾问"
        self.Duty = "制定明年战略"

    def visit(self, table):
        print('战略顾问年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if table.salesvolume > table.history_salesvolume:
            msg = "行业上行，扩大生产规模"
        else:
            msg = "行业下行，减小生产规模"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')



class Work:
    """工作类"""

    def __init__(self):
        self.works = []  # 需要处理的年度数据列表

    def add_work(self, obj):
        self.works.append(obj)

    def remove_work(self, obj):
        self.works.remove(obj)

    def visit(self):
        for obj in self.works:
            obj.accept()


if __name__ == '__main__':
    work = Work()  # 计划安排财务、总监、顾问对2018年数据处理
    # 实例化2018年数据结构
    finance_2018 = Finance_year(2018)
    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(100)
    finance_2018.set_history_salesvolume(180)
    finance_2018.set_history_cost(90)
    accounting = Accounting()   # 实例化会计
    audit = Audit()  # 实例化总监
    adviser = Adviser()     # 实例化顾问
    finance_2018.add_work(accounting)   # 会计安排到2018分析日程中
    finance_2018.add_work(audit)    # 总监安排到2018分析日程中
    finance_2018.add_work(adviser)  # 顾问安排到2018分析日程中
    work.add_work(finance_2018) # 添加2018年财务工作安排
    work.visit()