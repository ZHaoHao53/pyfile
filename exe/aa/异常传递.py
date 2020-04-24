import time

try:
    f = open('aaa.txt')

    try:
        while True:
            content = f.readline()

            if len(content) == 0:
                break

            time.sleep(3)
            print(content)

    except:
        print('意外终止!')




except:
    print('该文件不存在')