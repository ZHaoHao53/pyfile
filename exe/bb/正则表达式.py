import re

#match 从开头开始匹配不成功返回none   search找到一个就不往下找了


# a = '热巴娜扎佟丽娅'
# s = re.compile('佟丽娅')
# result = s.search(a)
# print(result)


msg = 'sada33d34f6y6g6787jh2j3hj32cfverve0'

result = re.findall('[a-z]',msg)

print(result)
