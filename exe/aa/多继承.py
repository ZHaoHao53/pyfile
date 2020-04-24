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

    def make_cake(self):
        self.__init__() #zilie也需要初始化
        print(f'运用{self.kongfu}做吃的')


    def make_master_cake(self):
        Master.__init__(self) #调用同名属性的方法要先初始化
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self) #调用同名属性的方法要先初始化
        School.make_cake(self)

#默认使用第一个基类
dai = Prentice()
#print(dai.kongfu)
dai.make_cake()
dai.make_master_cake()
dai.make_school_cake()
dai.make_cake()


#print(Prentice.__mro__)  #可以查看继承顺序