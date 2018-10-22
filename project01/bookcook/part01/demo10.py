# coding：utf-8
# 1.10 删除序列相同元素并保持顺序
'''
Q: 怎样在一个序列上面保持元素顺序的同时消除重复的值？
A: 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。
F:
'''


def dedupe(items, key=None):
    # 创建一个集合
    seen = set()
    for item in items:
        # 对item进行判断 指定一个key函数
        val = item if key is None else key(item)
        if val not in seen:
            # 创建一个生成器
            yield val
            seen.add(val)


test_dict = [{'x': 1, 'y': 2}, {'x': 2, 'y': 3}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}]
if __name__ == '__main__':
    res = dedupe(test_dict, key=lambda s: (s['x'], s['y']))
    print(list(res))
