#定义父类，提供重写方法   定义子类，提供重写方法 传递子类对象给调用者

class Dog(object):
    def work(self):
        print('追击敌人')


class ArmyDog(Dog):
    def work(self):
        print('z追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self,dog):
        dog.work()

ad = ArmyDog()
dd = DrugDog()

daliu = Person()
daliu.work_with_dog(ad)
daliu.work_with_dog(dd)