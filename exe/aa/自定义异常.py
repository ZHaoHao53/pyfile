#自定义异常返回的异常给用户 raise

class ShortInputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len


    def __str__(self):
        return f'你输出的长度是{self.length},不能少于{self.min_len}'



def main():
    try:
        con =input('qingshurumima')

        if len(con) < 4:
            raise ShortInputError(len(con),4)   #抛出异常

    except Exception as result:
        print(result)

    else:
        print('没有异常，输入完成')


main()