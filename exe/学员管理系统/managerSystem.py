from student import *

class StudentManager(object):

    def __init__(self):

        self.student_list = []


    def run(self):

        self.load_student() #加载学员信息

        while True:

            self.show_menu()

            menu_num = int(input('请输入功能序号:'))


            if menu_num == 1: #添加
                self.add_student()

            if menu_num == 2: #删除
                self.del_student()

            if menu_num == 3: #修改
                self.modify_student()

            if menu_num == 4: #查询
                self.search_student()

            if menu_num == 5: #显示
                self.show_student()

            if menu_num == 6: #保存
                self.save_student()

            if menu_num == 7: #退出
                exit_flag = input('确定要退出系统？ y or n')
                if exit_flag == 'y':
                    break


    @staticmethod
    def show_menu():
        print('1.添加')
        print('2.删除')
        print('3.修改')
        print('4.查询')
        print('5.显示')
        print('6.保存')
        print('7.退出')

    def add_student(self):
        name = input('请输入你的姓名：')
        sex = input('请输入你的性别：')
        tel = input('你的手机号：')

        student = Student(name,sex,tel)

        self.student_list.append(student)#添加
        #print(student)


    def del_student(self):
        del_name = input('请输入要删除的名字：')

        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print('该学员不存在！')



    def modify_student(self):
        modify_name = input('请输入要修改的学员姓名：')

        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('姓名')
                i.sex = input('性别:')
                i.tel = input('手机号：')
                print(f'修改成功,姓名为{i.name}，性别{i.sex}手机号为{i.tel}')
                break
            else:
                print('查无此人')
    def search_student(self):
        search_name = input('要查询的学员姓名：')

        for i in self.student_list:
            if i.name == search_name:
                print(f'{i.name},{i.sex},{i.tel}')
                break
            else:
                print('查无此人')

    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.sex}\t{i.tel}')

    def save_student(self):
        f = open('student.data','w')

        new_list = [i.__dict__ for i in self.student_list]

        f.write(str(new_list))
        f.close()
    def load_student(self):
        try:
            f = open('student.data','r')

        except:
            f = open('student.data','w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['sex'],i['tel']) for i in new_list ]

        finally:
            f.close()