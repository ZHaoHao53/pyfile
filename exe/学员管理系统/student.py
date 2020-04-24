class Student(object):
    def __init__(self,name,sex,tel):
        self.name = name
        self.sex = sex
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.sex},{self.tel}'


# a = Student('s','d',111)
# print(a)