# -*-coding:utf-8-*-
# 解压序列赋值给多个变量
def sequnce_to_n_variable():
    '''
    Q: 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
    A: 通过解压赋值解决，但变量的数量必须跟序列元素的数量是一样的。
    F：这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器
    :return:
    '''
    # 序列对象
    str_a = 'hello'
    list_a = [1, 2, 3, 'a']
    set_a = ('a', 23, 2, 3)
    # 赋值拆包
    a, b, c, d, e = str_a
    print("str拆包：", a, b, c, d, e)
    l1, l2, l3, l4 = list_a
    print('list拆包：', l1, l2, l3, l4)
    se1, se2, se3, se4 = set_a
    print('set拆包：', se1, se2, se3, se4)
    # 站位丢弃 _符号相当于垃圾桶
    m, _, _, _, n = str_a
    print("m,n:", m, n)


if __name__ == '__main__':
    sequnce_to_n_variable()
