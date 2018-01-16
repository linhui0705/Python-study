#3,4,5,6,7
for i in range(3,8):
    print(i)
    continue
print('--------------------')

#0,1,2,3,4,5
for j in range(0,6):
    print(j)
    continue
print('--------------------')

'''
0 0
0 1
1 0
1 1
'''
x = range(2)
for i in x:
    for j in x:
        print(i,j)
print('--------------------')

#1,3,5,7,9
n=0
while n<10:
    n=n+1
    if(n%2==0):
        continue
    print(n)
print('--------------------')