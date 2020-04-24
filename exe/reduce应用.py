#reduce（func,list） func每次计算的结果继续和下一个做计算

import functools

list1 = [1,3,5,7]

def func(a,b):
    return a+b

reuslt = functools.reduce(func,list1)
print(reuslt)