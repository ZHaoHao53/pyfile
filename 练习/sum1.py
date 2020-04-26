num = [2,3,7,11,15]
target = 9
x = 0

for i in num:
    a = target - i[x]
    if a in num:
        y =num.index(a)

        print(x,a)