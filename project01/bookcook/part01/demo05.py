# -*-coding:utf-8-*-
# 1.5 实现一个优先级队列
'''
Q: 怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
A: 利用headq模块
F: 堆是一种特殊的树形数据结构，每个节点都有一个值，通常我们所说的堆的数据结构指的是二叉树。
堆的特点是根节点的值最大（或者最小），而且根节点的两个孩子也能与孩子节点组成子树，亦然称之为堆。
 堆：大堆  小堆
'''
import heapq


class PriorityQueue():
    '''优先级队列类'''

    def __init__(self):
        self._queue = []  # 新建一个堆
        self._index = 0

    def push(self, item, priority):

        # 元组之间的大小比较类是于字符串的比较
        heapq.heappush(self._queue, (-priority, self._index, item))  # 往堆中插入一条新的值
        self._index += 1  #

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 从堆中弹出最小值


# 方法测试函数
def test_heapq():
    heap = []
    a=set()
