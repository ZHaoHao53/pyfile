#高阶函数abs（绝对值）， round（四舍五入）等
def sum_num(a,b,f):
    return f(a)+f(b)

result = sum_num(-1,2,abs)
print(result)


result = sum_num(1.4,2.9,round)
print(result)