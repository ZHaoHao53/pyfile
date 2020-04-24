class Master(object):

    def __init__(self):
        self.kongfu = 'sss'

    def make_cake(self):
        print(f'运用{self.kongfu}zuofan')

class School(object):
    def __init__(self):
        self.kongfu = 'aaa'

    def make_cake(self):
        print(f'运用{self.kongfu}zhizuo')

class Prentice(School,Master):
    def __init__(self):
        self.kongfu = 'duchuang '
        self.__money = 2000000000 #私有属性前加__

    def get_money(self): #获取
        return self.__money

    def set_money(self): #修改
        self.__money = 5000000


    def __info_print(self): #私有方法函数名前加__
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__() #zilie也需要初始化
        print(f'运用{self.kongfu}做吃的')


    def make_master_cake(self):
        Master.__init__(self) #调用同名属性的方法要先初始化
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self) #调用同名属性的方法要先初始化
        School.make_cake(self)



class Tusun(Prentice):
    pass

# #默认使用第一个基类
#dai = Prentice()
#print(dai.set_money())
# #print(dai.kongfu)
# dai.make_cake()
# dai.make_master_cake()
# dai.make_school_cake()
# dai.make_cake()
xiaoqiu = Tusun()
print(xiaoqiu.get_money())
xiaoqiu.set_money()
print(xiaoqiu.get_money())
# xiaoqiu.make_cake()
# xiaoqiu.make_school_cake()
# xiaoqiu.make_master_cake()
