'''
try：
    可能发生的错误代码
except:
    如果出现异常执行的代码
'''
# try:
#     f = open('aaa.txt','r')
#
# except:
#     f = open('aaa.txt','w')


'''
try：
    可能发生的错误代码
except 异常类型:
    如果出现该异常类型执行的代码
'''

try:
    print(num)

except NameError:
    print('有错误')