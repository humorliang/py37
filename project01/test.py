# -*- coding:utf-8 -*-

class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 将方法变成属性
    @property
    def name(self):
        return self._name

    # 对属性进行设置
    @name.setter
    def name(self, value):
        self._name = value

    # 类方法
    @classmethod
    def speak(cls, value=None):
        print('说出来!')

    # 静态方法
    @staticmethod
    def eat(value=None):
        print('吃')

    # 实例方法
    def run(self):
        print('run....')


def fib_func(max):
    '''
    含有yield关键字的函数变为 迭代对象generator
    每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，
    代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
    于是函数继续执行，直到再次遇到 yield。（遇到yield就返回一个迭代值，保存一个上下环境，下次就当前环境继续执行）
    :param max: 最大位数
    :return:
    '''
    n,a,b=0,0,1
    while n<max:
        # 返回当前对象 上下文
        yield b
        a,b=b,a+b
        n=n+1

for i in fib_func(8):
    print(i,end=' ')
# 1 1 2 3 5 8 13 21



if __name__ == '__main__':
    pass



    # per = Person('张三', 20)
    #
    # print(per.name)  # 张三
    # print(Person.name)  # <property object at 0x10f318958>
    # per.name = '李四'  # 实例对象设置属性
    # print(per.name)  #
    # # Person.name='李四2'  # 类对象设置属性 只有通过类对象设置的属性 类对象属性才能访问
    # # print(Person.name) # 李四2
    #
    # print('-' * 20)
    #
    # # 类方法 实例对象和类对象都可以访问
    # per.speak()
    # Person.speak()
    #
    # # 静态方法 实例对象和类对象都可以访问
    # per.eat()
    # Person.eat()
    #
    # # 实例方法 实力对象可以访问 类对象无法访问
    # per.run()
    # # Person.run()
