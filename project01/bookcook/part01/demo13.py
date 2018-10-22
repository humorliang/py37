# coding:utf-8
# 1.13 通过某个关键字排序一个字典列表
'''
Q: 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
A: 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构
F: itemgetter函数接受多个条件
'''
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
#
row_by_fname = sorted(rows, key=itemgetter('fname'))
print(row_by_fname)

# 多个帅选条件
row_by_fname_lname = sorted(rows, key=itemgetter('fname', 'lname'))
print(row_by_fname_lname)
