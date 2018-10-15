# -*-coding：utf-8 -*-
# 1.4 查找最大或最小的 N 个元素
'''
Q：怎样从一个集合中获得最大或者最小的 N 个元素列表？
A：heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。

'''
import heapq

num_list = [22, 3, 23, 14, 12, 5, 34, 23, 11, 10]
num_dict = [{'name': '张三', 'age': 20}, {'name': '张三', 'age': 22}, {'name': '张三', 'age': 15}, {'name': '张三', 'age': 14},
            {'name': '张三', 'age': 13}]


def get_N_max_min(iter_ele, num, me_type=None, key=None):
    '''
    返回列表中最大或最小的N个元素
    :type max or min
    :num   n
    :return:
    '''
    if me_type is None:
        return None
    elif me_type == 'max':
        if isinstance(num, int):
            return heapq.nlargest(num, iter_ele, key=lambda s: s[key])
        else:
            raise TypeError('请输入正确的num类型')
    elif me_type == 'min':
        if isinstance(num, int):
            return heapq.nsmallest(num, iter_ele, key=lambda s: s[key])
        else:
            raise TypeError('请输入正确的num类型')
    else:
        raise TypeError('请输入正确的me_type类型')


if __name__ == '__main__':
    # print(get_N_max_min(num_list, 3, 'max'))
    # print(get_N_max_min(num_list, 3, 'min'))
    print(get_N_max_min(num_dict, 3, 'min', 'age'))
    print(get_N_max_min(num_dict, 3, 'max', 'age'))
