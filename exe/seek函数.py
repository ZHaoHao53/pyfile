#seek用来移动指针
#文件对象.seek(偏移量，起始位置)

#0=开头 1=当前位置 2=结束位置

f = open('aaa.txt','r+')
f.seek(2,0)

con = f.read()
print(con)



