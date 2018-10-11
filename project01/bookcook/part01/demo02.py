# -*-coding:utf-8-*-
# 1.2 解压可迭代对象赋值给多个变量
def iter_to_N_variable():
    '''
    Q: 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
    A: 星号* 表达式 理解为任意个数变量
    :return:
    '''
    grade = [100, 70, 80, 60, 30]
    g1, *arg, g2 = grade
    print('g1,g2:', g1, g2)


def get_N_phoneNum(value):
    '''
    获取用户不定长信息
    :param value: 包含不定数量电话号码的用户
    :return: 返回用户号码集合
    '''
    name, *arg = value
    return arg


def do_user_label(userInfo):
    '''
    根据标签进行用户处理
    :param userInfo: 带有标签的用户信息
    :return: None
    '''
    for tag, *arg in userInfo:
        if tag == 'vip':
            print('vip：', arg)
        elif tag == 'svip':
            print('svip：', arg)
        else:
            print('普通用户：', arg)


def ignor_var():
    '''
    数据忽略提取 *_: 垃圾存储器
    :param info: 数据
    :return: 提取数据
    '''
    info = ['naki', '123@123.com', 182, (10, 20, 2018)]
    name, *_, (*_, year) = info
    return "name:" + name + "    year:" + str(year)


def fib_sum(numList):
    '''
    *_和递归算法实现
    1 +(2,3,4)
        1+2+(3,4)
            1+2+3+(4)
                1+2+3+4+()
    1+2+3+4
    :param numList: 数据集
    :return: 和
    '''
    header, *arg = numList
    # 递归的思想需要一个终止条件 最后arg为None
    print(arg)
    # [2, 3, 4, 5]
    # [3, 4, 5]
    # [4, 5]
    # [5]
    # []
    return header + fib_sum(arg) if arg else header



if __name__ == '__main__':
    iter_to_N_variable()
    user = ['张三', '13612348888', '13826884399']
    print(get_N_phoneNum(user))  # ['13612348888', '13826884399']
    print('-' * 20)
    userInfo = [
        ('vip', '张三', 188),
        ('svip', '李四', 168),
        ('normal', '王五', 158)
    ]
    do_user_label(userInfo)
    print('-' * 20)
    print(ignor_var())
    print('-' * 20)
    print(fib_sum([1, 2, 3, 4, 5]))
