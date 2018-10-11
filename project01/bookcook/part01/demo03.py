# -*-coding:utf-8 -*-
# 1.3 保留最后 N 个元素
'''
Q: 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
A: 使用collections.deque队列进行
'''
from collections import deque

def search(lines,pattern,history=5):
    '''
    查找并记录最后几行记录
    :param lines: 行
    :param pattern: 匹配项
    :param history: 历史记录
    :return: 记录
    '''
    # 创建一个固定大小的队列用于存储数据，并进行更新
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # yield关键字相当于 return 当前状态 但函数会变成迭代对象
            yield line,previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('test01.txt') as f:
        for line,previous in search(f,'python',5):
            for pline in previous:
                print(pline,end='')
            print(line,end='')
            print('-'*20)