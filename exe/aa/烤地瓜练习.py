#定义类 ：初始化属性
class Potato():
    def __init__(self):
        #状态
        self.cook_state = '生的'

        #时间
        self.cook_time = 0
        #调料
        self.coodiments = []

    def cook(self,time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 10 :
            self.cook_state = '5分熟'
        elif 10 <= self.cook_time <13:
            self.cook_state = 'shu了'
        elif 13 <= self.cook_time <15:
            self.cook_state = 'kaohule'

    def add_coodiments(self,coodiment):
        self.coodiments.append(coodiment)

    def __str__(self):
        return f'这个地瓜焙烤时间是{self.cook_time},现在的状态是{self.cook_state},添加了{self.coodiments}'






digua1 = Potato()
print(digua1)
digua1.cook(13)
digua1.add_coodiments('lajiaomo')
digua1.add_coodiments('ziran')
print(digua1)