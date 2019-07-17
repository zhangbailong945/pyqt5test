class CheryCar:
    '''
    奇瑞模具
    '''

    def __init__(self):
        self.car_name='奇瑞'
    
    def create(self):
        print('生产'+self.car_name)

class GeelyCar:
    '''
    吉利模具
    '''

    def __init__(self):
        self.car_name='吉利'
    
    def create(self):
        print('生产'+self.car_name)


class CarFactory:
    '''
    造车工厂 \n
    工程模式接口函数 \n
    @param ctype 车模具
    '''
    @staticmethod
    def createCar(ctype):
        cars=dict(Chery=CheryCar,Geely=GeelyCar)
        try:
            return cars[ctype]()
        except KeyError:
            print('没有找该到[%s]的车模具,不能生产！'% ctype)


if __name__ == "__main__":
    #生产奇瑞
    car1=CarFactory.createCar('Chery')
    car1.create()
    #生产吉利
    car2=CarFactory.createCar('Geely')
    car2.create()