class Dog(object):
    __tooth = 10

    @classmethod            #装饰器
    def get_tooth(cls):
        return cls.__tooth


wangcai = Dog()
result = wangcai.get_tooth()
print(result)