#coding:utf8

'''
抽象工厂模式
意图：提供一个创建一系列相关或相互依赖对象的接口，而无需指定他们具体的类。
'''

class CarShop:
    '''
    汽车商城
    '''

    def __init__(self,car_factory=None):
        self.car_factory=car_factory
    
    def show_car(self):
        car=self.car_factory.get_car()
        print('一辆',str(car))


class Chery:

    def __str__(self):
        return '奇瑞'


class Geely:

    def __str__(self):
        return '吉利'


class CheryFactory:
    '''
    奇瑞工厂
    '''

    def get_car(self):
        '''
        提供奇瑞接口
        '''
        return Chery()
    
    def get_type(self):
        return 'x3'

class GeelyFactory:
    '''
    吉利工厂
    '''

    def get_car(self):
        '''
        提供吉利接口
        '''
        return Geely()
    
    def get_type(self):
        return "x3"

if __name__ == "__main__":
    shop=CarShop()
    shop.car_factory=CheryFactory()
    shop.show_car()