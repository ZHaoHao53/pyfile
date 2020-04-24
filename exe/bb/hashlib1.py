import hashlib

#md5加密算法是不可逆的

#base64可逆

msg = '我喜欢你'
md5 = hashlib.md5(msg.encode('utf-8'))

print(md5.hexdigest())