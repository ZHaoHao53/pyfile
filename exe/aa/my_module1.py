def testA(a,b):
    print(a+b)


#__name__ 是系统变量，是模块的标识符，值是，如果是自身模块值是__mian__,否则是当前模块的名字
if __name__ == '__main__':
    testA(1,1)