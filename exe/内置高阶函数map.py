#map（func,lst）
list1 = [1,3,5,7,9]


def func(x):
    return x**2

result = map(func,list1)

print(result)
print(list(result))#list内置函数