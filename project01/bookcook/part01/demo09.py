# coding:utf-8
# 1.9 查找两字典的相同点
'''
Q: 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
A: 集合操作，字典dict的keys(),values()返回集合，利用集合特点进行差，补，余
F:
'''
dict_a = {
    'x': 1,
    'y': 2,
    'z': 3
}
dict_b = {
    'x': 2,
    'y': 2,
    'w': 6
}
# 相同的健值
key_common = dict_a.keys() & dict_b.keys()
# 时间差
poor_common = dict_a.keys() - dict_b.keys()
# 值相等
value_common = dict_a.items() & dict_b.items()
# 筛选
remove_common = {key: dict_a[key] for key in dict_a.keys() - {'x', 'w'}}

if __name__ == '__main__':
    print(key_common)
    print(poor_common)
    print(value_common)
    print(remove_common)
