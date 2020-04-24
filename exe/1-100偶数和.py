result=0
for i in range(0,101,2):
    #result = result + i
    result += i
print(result)
#f1
a = 1
b = 0
while a <= 100 :
    if a%2 ==0:
        b += a
    a += 1

print(b)

#f2
c = 0
d = 0
while c <= 100:
    d += c
    c += 2

print(d)

i = 1
while i <= 3:

    if i == 3 :
        print('1111')
        continue
    print('222')
    i += 1
