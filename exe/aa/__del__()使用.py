class Washer():
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def __del__(self):
        print(f'{self}对象已删除')



haier = Washer(10,20)

del haier