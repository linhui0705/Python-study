classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
for i in range(3):
    print('classmates[' + i.__str__() + ']=' + classmates[i])

'''
取最后一个元素，-1做索引，直接获取最后一个元素
以此类推，可获取倒数第2个、倒数第3个
'''
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
'''
list追加到末尾
list.append()
list插入到指定位置
list.insert(index, x)
list删除元素（无参则默认末尾元素）
list.pop()
'''
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
classmates.append('Tom')
print(classmates)
classmates.pop()
classmates.pop(1)
print(classmates)
print('--------------------')
# List里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)
# 若List中一个元素也没有，就是空的list，长度为0
M = []
print(len(M))
print('----------------------------------------')
'''
tuple
另一种有序列表叫元组：tuple
tuple一旦初始化就不能修改
只有1个元素的tuple定义时必须加一个逗号，以消除歧义
'''
classmates2 = ('Michael', 'Bob', 'Tracy')
print('----------------------------------------')
N = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(N[0][0])
print(N[1][1])
print(N[2][2]) # Or print(N[-1][-1])