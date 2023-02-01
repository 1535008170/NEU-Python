#使用* 号收集参数，调用时可以传入多个参数
#收集的参数存在元组里

'''
def add(x, y):
    return x + y

params = (1, 2)
print(add(*params))
'''

def save_ranking(*args, **kwargs):
    print(args)     
    print(kwargs)
save_ranking('ming', 'alice', 'tom', four='wilson',five='roy')
# ('ming', 'alice', 'tom’)
# {'four': 'wilson', ‘five': 'roy'}

#关键字参数不能在位置参数前声明
