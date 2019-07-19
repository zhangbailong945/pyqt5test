#中介者模式

'''
将其他对象之间的交互装在中介者对象中，达到松耦合、隐式引用、独立变化，与代理模式有相似之感。
代理模式是结构型模式，侧重于对象调用的接口控制，而终结模式是行为模式，解决对象
与对象之间相互调用的行为问题。

生产者和消费者之间的销售作为一个中介者，用对象来表示生产和购买以及流通这个过程。


'''


class Consumer:
    '''消费者'''
    def __init__(self,product,price):
        self.name='消费者'
        self.product=product
        self.price=price
    
    def shopping(self,name):
        '''购买东西'''
        print("向{}购买{}价格内的{}产品".format(name,self.price,self.product))


class Producer:
    '''生产者'''
    def __init__(self,product,price):
        self.name='生产者'
        self.product=product
        self.price=price
    
    def sale(self,name):
        '''卖东西'''
        print("向{}销售{}价格的{}产品".format(name,self.price,self.product))

class Mediator:
    '''中介者'''
    def __init__(self):
        self.name='中介者'
        self.consumer=None
        self.producer=None
    
    def sale(self):
        '''进货'''
        self.consumer.shopping(self.producer.name)
    
    def shopping(self):
        '''进货'''
        self.producer.sale(self.consumer.name)
    
    def profit(self):
        print('中介净赚:{}'.format(self.consumer.price-self.producer.price))
    
    def complete(self):
        self.sale()
        self.shopping()
        self.profit()

if __name__ == "__main__":
    consumer=Consumer('手机',3000)
    producer=Producer('手机',2500)
    mediator=Mediator()
    mediator.consumer=consumer
    mediator.producer=producer
    mediator.complete()