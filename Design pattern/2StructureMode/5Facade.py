# Facade 外观

'''
意图：
为子系统中的一组接口提供一个一致的界面，
Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

当你需要构建一个层次结构的子系统时，使用facade模式定义子系统中每层的入口点。
如果子系统之间相互依赖的，你可以让他们仅通过facade进行通信。
从而简化了他们之间的依赖关系。

'''


class Api1:

    def save(self):
        print('保存数据A')

    def delete(self):
        print('删除数据A')


class Api2:

    def save(self):
        print('保存数据B')
    
    def delete(self):
        print('删除数据B')


class Facade:
    '''
    外观模式，又作过程模式
    为子系统中的一组接口提供一个一致的界面。
    Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用
    '''

    def __init__(self):
        self._api1 = Api1()
        self._api2 = Api2()

    def saveAll(self):
        [obj.save() for obj in [self._api1, self._api2]]

    def deleteAll(self):
        [obj.delete() for obj in [self._api1, self._api2]]

if __name__ == "__main__":
    test=Facade()
    test.saveAll()
    test.deleteAll()
