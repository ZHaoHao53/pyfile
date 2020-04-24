#继承体验
#顶级类、基类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


#派生类/子类
class B(A):
    pass


result = B()

result.info_print()