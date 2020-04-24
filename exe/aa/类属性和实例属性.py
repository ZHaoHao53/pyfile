#设置和访问类属性
class Dog(object):  #定义类和类属性
    tooth = 10

wangcai = Dog()     #创建对象
xiaohei = Dog()


#修改类属性
# Dog.tooth = 30
#
# print(Dog.tooth)        #通过类对象访问
# print(wangcai.tooth)    #通过实例对象访问
# print(xiaohei.tooth)    #通过实例对象访问

wangcai.tooth = 200

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)