<<<<<<< HEAD
# coding:utf-8
=======
# -*-coding:utf-8-*-
'''
1.6 字典中的键映射多个值
Q: 怎样实现一个键对应多个值的字典（也叫 multidict）？
A: 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。
F: 多值有序就用list, 去重就用set集合
'''

from collections import defaultdict


def multidict():
    '''创建一个多值字典'''
    # 多值为list  有序
    d_list = defaultdict(list)
    # 多值为set 去重
    d_set = defaultdict(set)
    # 添加
    d_list['key_01'].append(2)
    d_list['key_01'].append(3)
    d_list['key_02'].append(4)

    # 添加
    d_set['key_01'].add(2)
    d_set['key_01'].add(2)
    d_set['key_02'].add(3)

    print(d_list)
    print(d_set)


def multidict02():
    '''创建一个多值字典'''
    d = {}  # 创建一个空字典
    d.setdefault('key01',[]).append(1)
    d.setdefault('key01',[]).append(5)
    d.setdefault('key02',[]).append(12)

    print(d)


if __name__ == '__main__':
    multidict()
    multidict02()
>>>>>>> d9e0c442548bfe123cc15a23741455bb87759e71
