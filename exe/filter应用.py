#filter（func，lst）函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，
# 如果要转换为列表，可以用list（）来转换

list1 = [1,2,3,4,5,6,7,8,9,10,11,21,22,34,25]

def func(x):
    return x%2 == 0

result = filter(func,list1)

print(list(result))
print(result)