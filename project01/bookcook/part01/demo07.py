# -*—coding:utf-8-*-
# 1.7 字典排序
'''
Q: 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
A: 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。
F: 使用OrderedDict会有字典两倍的内存开销。
'''
from collections import OrderedDict


def sort_dict():
    s_d = OrderedDict()
    s_d['bar'] = 11
    s_d['foo'] = 21
    s_d['tar'] = 13
    print(s_d)
    print('--------')
    for key in s_d:
        print(key, s_d[key])
    print('-------')
    print(s_d['bar'])


if __name__ == '__main__':
    sort_dict()
