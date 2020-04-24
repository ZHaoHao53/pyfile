import random

teacher = ['aa','bb','cc','dd','ee','ff','gg','hh','kk']
offices = [[],[],[]]

for name in teacher:

    num = random.randint(0,2)
    offices[num].append(name)

i = 1
for office in offices:
        print(f'办公室{i}的人数是{len(office)}，老师分别是{name}')

        for name in office:
            print(name)

        i += 1



        #index len append pop remove insert