class Washer():
    def __init__(self,w,h):
        self.w = w
        self.h = h


    def print_info(self):
        print(f'aaaaaaaa{self.w}')
        print(f'nnnnnnn{self.h}')
        


haier1 = Washer(10,20)
haier1.print_info()


haier2 = Washer(20,30)
haier2.print_info()