#组合模式
'''
意图：
将对象组合成树形结构以表示“部分-整体”的层次结构。Composite使得用户对当对象和组合对象
的使用具有一致性。
适用性：
你想表示对象的部分-整体层次结构
你希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。

例：
描述一家公司的层次结构，以办公室Wie节点。总经理办公室是根节点，人下面有
人事办公室，业务办公室，生产办公室，财务办公室。每个办公室还有更小的办公室。
每个办公室都有职责，人员数、人员薪资的属性。
'''

class CompoentBase:
    '''
    抽象办公室基类
    '''
    def __init__(self,name):
        self.name=name
    
    def add(self,obj):
        pass
    
    def remove(self,obj):
        pass
    
    def display(self,obj):
        pass


class Node(CompoentBase):

    def __init__(self,name,duty):
        self.name=name
        self.duty=duty
        self.children=[]
    
    def add(self,obj):
        self.children.append(obj)
    
    def remove(self,obj):
        self.children.remove(obj)
    
    def display(self,number=1):
        print("办公室：{},级别:{},职责：{}".format(self.name,number,self.duty))
        n=number+1
        for obj in self.children:
            obj.display(n)


if __name__ == "__main__":
    root=Node('总经理办公室',"总经理")
    node1=Node("财务部门","财务经理")
    root.add(node1)

    node2=Node('业务部门',"业务经理")
    root.add(node2)

    node3=Node('生产部门',"生产经理")
    root.add(node3)

    node4=Node('销售部门1',"销售1经理")
    node2.add(node4)

    node5=Node('销售部门2',"销售2经理")
    node2.add(node5)
    root.display()