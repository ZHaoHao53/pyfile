stu = [
    {'name':'tom','age':18},
    {'name':'jean','age':19},
    {'name':'jack','age':22}
]


stu.sort(key=lambda x:x['name'])
print(stu)


stu.sort(key=lambda x:x['name'],reverse=True)
print(stu)

stu.sort(key=lambda x:x['age'])
print(stu)


stu.sort(key=lambda x:x['age'],reverse=True)
print(stu)