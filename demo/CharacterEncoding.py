print('包含中文的str')
print('----------------------------------------')
'''
ord()函数获取字符串的整数表示
chr()函数把编码转换为对应的字符
若知道整数编码，可用十六进制写
'''
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
print('--------------------')
print('ABC')
print(b'ABC')
print('----------------------------------------')
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))