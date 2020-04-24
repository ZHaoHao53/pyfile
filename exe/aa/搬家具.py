#定义家具类
class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具有{self.name},占地面积有{self.area}'



s = Furniture('shuangrenchaung',5)
a = Furniture('shafa',9)
print(s)
print(a)