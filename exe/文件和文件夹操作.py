import os

# os.rename('aaa.txt','bbb.txt')
#
# os.remove('bbb.txt')

#os.mkdir(文件夹名字)创建文件夹
# os.rmdir()删除文件夹
# os.getcwd()获取当前目录
#os.chdir(目录)改变默认目录
#os.listdir(目录)获取目录列表


# os.getcwd()
# print(os.getcwd())
#os.mkdir('aa')
flag = 2
#rename --重命名文件夹

file_list = os.listdir()
print(file_list)
#
# #重新构造名字
for i in file_list:
    if flag == 1:

        new_name = 'python_'+i
    elif flag == 2:
        num = len('python_')
        new_name = i[num:]

    print(new_name)

#
# #重命名
    os.rename(i,new_name)


