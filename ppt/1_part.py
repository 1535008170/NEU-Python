"""
for i in range(-1000,1000):
    a=i #直接将i赋给a
    b=int(i.__str__())
    if a is b: #判断a和b的地址是否相同
        print(i)

#这说明 -5到256都共享内存
"""

"""
name = input('What is your name?') #等待键盘输入
if 's' in name:
    print('Your name contains the letter "s".')
else:
    print('Your name does not contain the letter "s".')
"""

""" 断言
age = -1
assert 0 < age < 100
"""

''' 缝合zip() 函数
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
print(list(zip(names, ages)))
'''

'''
name = {'first name': 'Robin', 'last name': 'James'}
robin = name
name = None
print(robin)
'''

while True:
    try:
        x = int(input('Enter the 1st number: '))
        y = int(input('Enter the 2nd number: '))
        value = x / y
        print('x / y is', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break