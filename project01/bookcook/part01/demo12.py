# coding:utf-8
# 1.12 序列中出现次数最多的元素
'''
Q: 怎样找出一个序列中出现次数最多的元素呢？
A: collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。
F:
'''

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)  # 生成各个单词数量个数地址
print(word_counts)  # Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3,
#  'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})

print(word_counts.most_common(2))  # [('eyes', 8), ('the', 5)]

print(word_counts['look'])  # 4
