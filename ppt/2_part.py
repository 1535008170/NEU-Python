''' list转换为str方法 使用str="".join(list)
dataList = ['1', '2', '3', '4' ]
str1 = "".join(dataList)
print (str1)
'''

''' 切片赋值(切片也可实现元素插入)
name=list('pro')
name[2:]=list('python')
print(name)
'''

'''
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

index : 在列表中查找指定值第一次出现的索引
insert : 在索引处插入对象到列表
pop : 从列表中删除一个元素，并返回此元素
remove : 删除第一个指定的元素
注意:remove修改列表但不返回值
    pop会返回值
'''

''' sort()
x=[1,4,6,2,3]
y=x.sort()
print(x)
print(y) #x已经排完序,y=none

方法sort接受两个可选参数:key和reverse
'''

''' sorted()
x=[1,4,6,2,3]
y=sorted(x)
print(x) x是原来的
print(y) y是新的生成的副本
'''

''' 字符串format方法
a="{1} {0} {1}".format("hello", "world")
print(a)
'''

#三种标志: !s （与原值一样）, !r（原值加引号）, !a（带引号的ascii编码） 格式说明符（冒号：）
#print("{pi!s} {pi!r} {pi!a}".format(pi="π"))

#'{:010.2f}'.format(pi)
# '0000003.14’
# 010.2f中，第一个0表示用0填充，10表示宽度

#find方法：查找子串，返回第一个字符索引，或-1
#str.find(str, start=0, end=len(string))
'''
a='With a moo-moo here, and a moo-moo there'.find('moo')
print(a)
'''
# 7
# 区别于成员资格检查：in（返回True/False）

#string='_33keyword' #33_keyword不符合命名规则
#print(string.isidentifier())

#标识符是由字符（A~Z 和 a~z）、下划线和数字组成，但第一个字符不能是数字。
#标识符不能和 Python 中的保留字相同。
#Python中的标识符中，不能包含空格、@、% 以及 $ 等特殊字符。

'''
s="To Be or Not to Be"
print(s.strip("To Be"))
#结果:r Not t
从两端开始 删除匹配上oeTB的字母
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
'''

'''
d = {'title': 'Python', 'url': 'http://www.python.org', 'time': 'Tuesday'}
x = {'title': 'Java'}
d.update(x)
print(d)
'''

#print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)) #3 1 4 2
#print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3)) # 3 2 4 1

'''
import math
tmp="The {mod.__name__} module defines the value {mod.pi} for π"
tmp=tmp.format(mod=math)
print(tmp)
'''

#列表推导
#print([x * x for x in range(10)])

'''
g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))
print(next(g))
print(next(g))
'''

'''
lst = ['1','2','3','4']
print(list(map(int,lst)))
'''


from functools import reduce
lst =[1, 2, 3, 4]
print(reduce(lambda x,y: x+y, lst))
