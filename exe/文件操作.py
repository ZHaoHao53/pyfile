#打开open()
f = open('aaa.txt','w')


#操作 write() read()
f.write('aaa')


#关闭 close()
f.close()

#r:如果文件不存在，报错，不支持写入操作，表示只读
# f = open('aaa.txt','r')
# f.write('aa')
# f.close()




#w:只写，如果文件不存在，新建文件，执行写入，会覆盖原有内容
# f = open('1.txt','w')
# f.write('ab')
# f.close()




#a:追加，如果文件不存在，新建文件；在原有内容上，追加新内容
# f = open('2.txt','a')
# f.write('axyz')
# f.close()




#访问模式参数可以省略，如果胜率表示访问模式为r
# f = open('1.txt')
# f.close()