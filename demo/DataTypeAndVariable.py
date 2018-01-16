# coding=utf-8
'''
字符串
'''
print('【字符串】')
#I'm OK.
print('I\'m OK.')
print('--------------------')
'''
I'm learning Python.
It's interesting!
'''
print('I\'m learning Python\nIt\'s interesting!')
print('--------------------')
'''
\	\
\\\t\\
'''
print('\\\t\\')
print(r'\\\t\\')
print('--------------------')
'''
line1
line2
line3
'''
print('''line1
line2
line3''')
print('----------------------------------------')

'''
布尔值
True
False
True
False
[and]
True
False
False
True
[or]
True
True
False
True
[not]
False
True
True
'''
print('【布尔值】')
print(True)
print(False)
print(3>2)
print(3>5)
#布尔值可以用and、or和not运算
print("[and]")
print(True and True)
print(True and False)
print(False and False)
print(5>3 and 3>1)
print("[or]")
print(True or True)
print(True or False)
print(False or False)
print(5>3 or 3>1)
print("[not]")
print(not True)
print(not False)
print(not 1>2)
print('----------------------------------------')

#空值是Python里的特殊值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的值

'''
变量

'''
print('【变量】')
a=1
t_007='T007'
Answer=True
print(a)
print(t_007)
print(Answer)
print('--------------------')
a = 'ABC'
b = a
a = 'XYZ'
print(a + "," + b)
print('----------------------------------------')
'''
常量
在Python中，通常用全大写的变量名表示变量
但事实上PI仍然是一个变量，Python没有任何机制保证PI不会被改变

除法的计算结果是浮点数，即使两个整数恰好整除，结果也是浮点数

还有一种除法是//，称为地板除，两个整数的除法仍然是整数

余数运算，求模：%
'''
print('【常量】')
PI = 3.14159265358972384626433
print(PI)
print(10/3)
print(9/3)
print(10//3)
print(10%3)
print('----------------------------------------')

print('【练习】')
# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)