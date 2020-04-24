#一个参数
fn1 = lambda a:a
print(fn1('hi'))

#默认参数
fn2 = lambda a,b,c=100:a+b+c
print(fn2(20,30))

#可变参数*arge，返回值为元组
fn3 = lambda *args:args
print(fn3(10,20,30))

#可变参数**kwarge
fn4 = lambda **kwargs:kwargs
print(fn4(name='python'))
print(fn4(name='tim',age='10'))