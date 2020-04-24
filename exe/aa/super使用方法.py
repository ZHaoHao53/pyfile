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
        super().__init__()
        super().make_cake()

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

    def old_make(self):
        #F1
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        #F2
        # super(Prentice,self).__init__()
        # super(Prentice,self).make_cake()
        #无参数
        super().__init__()
        super().make_cake()


#默认使用第一个基类
lll = Prentice()
lll.old_make()

#print(Prentice.__mro__)  #可以查看继承顺序