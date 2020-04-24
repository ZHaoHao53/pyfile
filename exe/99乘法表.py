j = 1 #行号
while j <= 9:
    i = 1 #每行表达式个数
    while i <= j:
        print(f'{i}*{j}={i*j}' , end ='\t') #\t制表符用来对齐表达式
        i += 1
    print() #换行
    j += 1