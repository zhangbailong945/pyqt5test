class CheryCar:
    '''
    奇瑞模具
    '''

    def __init__(self):
        self.car_name='奇瑞'
    
    def create(self):
        print('生产'+self.car_name)

class GeelyCar():
    '''
    吉利模具
    '''

    def __init__(self):
        self.car_name='吉利'
    
    def create(self):
        print('生产'+self.car_name)


def Car(classname):
    '''
    造车 \n
    工程模式接口函数 \n
    @param classname 车模具
    '''
    product=dict(Chery=CheryCar,Geely=GeelyCar)
    return product[classname]()


if __name__ == "__main__":
    #生产奇瑞
    car1=Car('Chery')
    car1.create()
    #生产吉利
    car2=Car('Geely')
    car2.create()