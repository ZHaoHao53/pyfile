# import time
# print(time.time())

def check_fermat(a,b,c,n):
    if n>2 :
        a**n + b**n != c**n
 #   if (a**n + b**n != c**n):
        print('Holy smokes,')
    else:
        print('请输入n的值大于2')

a = int(input("请输入a的值"))
b = int(input("请输入b的值"))
c = int(input("请输入c的值"))
n = int(input("请输入N的值"))
check_fermat(a,b,c,n)


def sum_1(x,y) :
    """

    :param a:
    :param b:
    :return:
    """
    return x+y

sum_1(1,2)
