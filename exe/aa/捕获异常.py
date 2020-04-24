#捕获多个异常类型
try:
    print(1/0)

except (NameError,ZeroDivisionError):
    print('...')


#捕获异常描述信息

try:
    print(num)

except (NameError,ZeroDivisionError) as result:
    print(result)


#捕获所有异常
try:
    print(1/0)
except Exception as result:
    print(result)


#异常中的else
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有异常时执行的代码')

#异常的finally 无论异常有无都执行的代码
try:
    f = open('bbbb.txt','r')
except Exception as e:
    f =open('bbbb.txt','w')
else:
    print('没有yichang ')
finally:
    f.close()