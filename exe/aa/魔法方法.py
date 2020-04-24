#-__init__()   __xx__()

#__init__() 初始化对象
class Washer():
    def __init__(self):
        self.w = 300
        self.h = 300

    def print_info(self):
        print(f'aaaaaa{self.w}')
        print(f'bbbbb{self.h}')



haier = Washer()

haier.print_info()
