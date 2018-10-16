# -*-coding:utf-8-*-
# 1.5 实现一个优先级队列
'''
Q: 怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
A: 利用headq模块
F:
'''
import heapq


class PriorityQueue():
    '''优先级队列类'''

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
