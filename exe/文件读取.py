# f = open('aaa.txt','r')
#
# print(f.read(10))#10代表10个字节
#
# f.close()


#readlines()可以按照行的方式把整个文件中的内容进行一次性读取，并且返回一个列表，每一行的数据作为一个一个元素

f = open('aaa.txt')
content = f.readlines()

print(content)

f.close()


#readline 一次读取一行内容