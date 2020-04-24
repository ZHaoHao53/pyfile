#用户输入目标文件

old_name = input('请输入要备份的文件名：')
#print(old_name)

#备份的文件名
index = old_name.rfind('.')

if index > 0 :
    postfix = old_name[index:]


#new_name = old_name[:index]+'[备份]'+old_name[index:]
new_name = old_name[:index]+'[备份]'+postfix
print(new_name)


#备份文件写入数据
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')

while True:
    con = old_f.read()
    if len(con) == 0:
        break

    new_f.write(con)


old_f.close()
new_f.close()