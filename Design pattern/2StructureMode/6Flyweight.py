#享元模式
'''
意图：
运用共享技术有效地支持大量细粒度的对象
适用性：
一个应用程序使用大量的对象
完全由于使用大量的对象，造成很大的存储开销。
对象的大多数状态都可以变为外部状态。
如果删除对象的外部状态，那么可以用相对较少的共享对象取代很多组对象。

'''

class FlyweightBase:
    '''享元基类'''
    def offer(self):
        pass
    

class Flyweight(FlyweightBase):
    '''共享享元类'''
    def __init__(self,name):
        self.name=name
    
    def get_price(self,price):
        print('产品类型:{}详情:{}'.format(self.name,price))


class FactoryFlyweight:
    '''享元工厂类'''

    def __init__(self):
        self.product={}
    
    def getProduct(self,key):
        if not self.product.get(key,None):
            self.product[key]=Flyweight(key)
        return self.product[key]


if __name__ == "__main__":
    test=FactoryFlyweight()
    a=test.getProduct('高端')
    a.get_price("香水:80")
    b=test.getProduct('高端')
    b.get_price('面膜:800')