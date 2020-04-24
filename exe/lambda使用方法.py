#体验lambda
# def fn1():
#     return 200
#
# print(fn1)
# print(fn1())

#匿名函数
#lambda 参数列表 ： 表达式
fn2 = lambda : 100
print(fn2)  #内存地址

print(fn2()) #值



fn1 = lambda a,b:a+b
print(fn1(1,2))