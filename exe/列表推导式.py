# 0-10创建列表
# 1.循环实现  2.列表推导式实现
# while
# list=[]
# i = 0
# while i<=10:
#     list.append(i)
#     i+=1
# print(list)


# for
# list = []
# for i in range(11):
#     list.append(i)
# print(list)

# 列表推导式
# list1 = [i for i in range(0, 11)]
# print(list1)

#
# list1 = [i for i in range(10) if i%2==0]
# print(list1)

list1=[(i,j) for i in range(1,3) for j in range(3)]
print(list1)