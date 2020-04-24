#返回值+递归练习
#0-5累加
i = int(input('请输入数字：'))
def sum_num(i):
    if i == 1:
        return 1
    return  i+sum_num(i-1)

sum_result = sum_num(i)



print(sum_result)
