age = 20
print("your age is", age)
if age >= 18:
    print("adult")
else:
    print('teenager')
print('----------------------------------------')
height = 1.75
weight = 80.5
bmi = weight/(height*height)
print("你的bmi：",bmi)
if(bmi<18.5):
    print("过轻")
elif bmi>=18.5 and bmi<25:
    print('正常')
elif bmi>=25 and bmi<28:
    print('过重')
elif bmi>=28 and bmi<32:
    print('肥胖')
elif bmi>32:
    print('严重肥胖')