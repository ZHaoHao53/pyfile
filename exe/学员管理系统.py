#定义功能界面
def info_print():
    print("--------请选择功能--------")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员")
    print("4.查询学员")
    print("5.显示全部学员")
    print("6.退出系统")
    print("-"*25)

#存储数据
info = []
#定义添加学员函数
def add_info():
    """添加学员"""
    #用户输入：学号、姓名、手机号
    new_id = input('请输入学号:')
    new_name = input('请输入姓名:')
    new_tel = input('请输入手机号:')
    #判断是否添加这个学员：如果姓名存在报错，不存在添加
    global info
    #不允许重名，判断输入的名字和字典中的name
    for i in info:
        if new_name == i['name']:
            print('该学员已存在！')
            return

    #添加时准备空字典 添加
    info_dict = {}

    #字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    #print(info_dict)

    #列表追加字典
    info.append(info_dict)
    print(info)

#删除学员
def del_info():
    """删除学员"""
    #输入要删除的学员信息
    del_name = input('请输入要删除的姓名：')
    #判断该学员是否存在
    global info

    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break

    else:
        print('该学员不存在！')
    print(info)

#修改学员信息
def modify_info():
    """修改信息"""
    modify_name= input('请输入要修改的学员姓名：')

    global info
    #判断学员是否存在
    for i in info:
        if modify_info == i['name']:
            i['tel'] =input('请输入新的手机号：')
            break
    else:
        print('该学员不存在！')



    print(info)

#查询学员信息
def search_info():
    '''查询信息'''
    #输入要查询的学员姓名
    search_name = input('请输入要查询的学员姓名：')
    global info
    #判断是否存在
    for i in info:
        if search_name == i['name']:
            print('-----该学员信息-----')
            print(f"该学员学号是{i['id']}，姓名是{i['name']}，手机号是{i['tel']}")
            break
    else:
        print('该学员不存在')

#显示全部学员信息
def print_all():
    '''显示全部信息'''
    print('学号\t姓名\t手机号')

    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")




while True:
    #显示功能界面
    info_print()


    #用户输入功能序号
    user_num = int(input('请输入功能序号：'))
    if user_num == 1:
        #print('添加')
        add_info()
    elif user_num ==2:
        #print('删除')
        del_info()
    elif user_num == 3:
        #print('修改')
        modify_info()
    elif user_num == 4:
        #print('查询')
        search_info()
    elif user_num == 5:
        #print('显示全部')
        print_all()
    elif user_num == 6:
        #print('退出系统')
        exit_flag = input('确定要退出系统？ y or n')
        if exit_flag == 'y':
            break
    else:
        print('输入有误！')



#输入不同序号，执行不同功能