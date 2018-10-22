# -*-coding:utf-8 -*-
# 1.8 字典的运算
'''
Q: 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
A: 通常需要使用 zip() 函数先将键和值反转过来,然后再使用min,max,sorted函数进行处理
F: 需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器，当最大值和最小值有相等多值时会等同实体返回
'''
# 股票价格
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_prices = min(zip(prices.values(), prices.keys()))
max_prices = max(zip(prices.values(), prices.keys()))
# 指定规则进行排序
sort_prices = sorted(prices, key=lambda key: prices[key], reverse=True)

if __name__ == '__main__':
    print(min_prices, max_prices, sort_prices)
