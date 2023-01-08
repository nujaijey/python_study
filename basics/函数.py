#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 21:57
# @Author  : nujaijey
# @File    : 函数.py
# @Desc    :


# 函数定义
def func():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j}*{i}={j * i}', end=' ')
        print()


# 函数调用
func()
print('----------------------------')
func()
print('----------------------------')


# 参数的定义（形参）
def print_def(x):
    for i in range(x):
        for j in range(i + 1):
            print('* ', end='')
        print()


# 参数的传递（实参）
print_def(1)
print('----------------------------')
print_def(5)


def add(n, m):
    """
    函数功能说明注释
    :param n:
    :param m:
    :return:
    """
    print('n：', n)
    print('m：', m)
    print('n+m：', n + m)


add(11, 22)
add(m=22, n=11)


# 函数拆包
def func(a, b, c=99):
    print(a)
    print(b)
    print(c)


li = [11, 22, 33]
dic = {"a": "aa", "b": "bb", "c": "cc"}
# 调用函数的时候可以使用*对列表或者元组进行拆包，使用**对字典进行拆包
func(*li)  # 位置参数
func(**dic)  # 关键字参数


# 不定长参数求和
def func4(*args, **kwargs):
    li1 = [i for i in args] + [value for value in kwargs.values()]
    print(sum(li1))


func4(11, 22, n=33)


# return返回一个数据，返回对象
def add(a, b):
    c = a + b
    return c


res = add(11, 22)
print('add调用返回的参数：', res)


# return返回多个数据，返回元组
#
# 数据
def add1(a, b):
    c = a + b
    d = a - b
    return c, d


res1 = add1(11, 22)
print('add1调用返回的参数：', res1)

li = ["name", "python", "java", "php"]
res = enumerate(li)
print(list(res))

# 内置函数
# eval()：识别字符串中有效的python表达式
print(eval("11+22"))
print("------------------------")

# enumerate()：获取列表中的数据以及索引
for i, v in enumerate(li):
    print(i, v)

# zip()：数据的聚合打包
title = ["name", "age", "gender"]
data = ["小明", 18, "男"]
res1 = zip(title, data)
print(dict(res1))
print(list(res1))

# zip扩展：聚合多个列表，以数量最短的列表作为基准聚合
li1 = [1, 2, 3]
li2 = [11, 22, 33, 44]
li3 = [111, 222, 333, 444]
res2 = zip(li1, li2, li3)
print(list(res2))

# filter()：过滤器函数，批量过滤数据
li4 = [85, 95, 74, 35, 49, 84, 99]
res3 = filter(lambda x: x > 80, li4)
print(list(res3))

# 列表排序扩展
li5 = [(11, 22, 33), (3, 100, 55), (98, 78, 1)]
# def func(x):
#     return x[1]
# sort()函数默认用第一个元素进行排序，可以用key来指定排序规则
# li5.sort(key=func)
li5.sort(key=lambda x: x[1])
print(li5)

print('------------------------------------')

# 封装一个函数，调用函数可以完成以下数据格式转换
# 传入参数：
# cases = [
#     ['case_id', 'case_title', 'url', 'data', 'excepted'],
#     [1, '用例1', 'www.baidu.com', '001', 'ok'],
#     [2, '用例2', 'www.baidu.com', '002', 'ok'],
#     [3, '用例3', 'www.baidu.com', '003', 'ok'],
#     [4, '用例4', 'www.baidu.com', '004', 'ok'],
#     [5, '用例5', 'www.baidu.com', '005', 'ok']
# ]
# 返回结果
# cases01 = [{'case_id': 1, 'case_title': '用例1', 'url': 'www.baidu.com', 'data': '001', 'excepted': 'ok'},
#            {'case_id': 2, 'case_title': '用例2', 'url': 'www.baidu.com', 'data': '002', 'excepted': 'ok'},
#            {'case_id': 3, 'case_title': '用例3', 'url': 'www.baidu.com', 'data': '003', 'excepted': 'ok'},
#            {'case_id': 4, 'case_title': '用例4', 'url': 'www.baidu.com', 'data': '004', 'excepted': 'ok'},
#            {'case_id': 5, 'case_title': '用例5', 'url': 'www.baidu.com', 'data': '005', 'excepted': 'ok'}
#            ]

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baidu.com', '001', 'ok'],
    [2, '用例2', 'www.baidu.com', '002', 'ok'],
    [3, '用例3', 'www.baidu.com', '003', 'ok'],
    [4, '用例4', 'www.baidu.com', '004', 'ok'],
    [5, '用例5', 'www.baidu.com', '005', 'ok']
]
# 方法1
cases01 = []


def func01(data01):
    for x in range(1, len(data01)):
        res01 = dict(zip(data01[0], data01[x]))
        cases01.append(res01)
    return cases01


print(func01(cases))


# 方法2：列表推导式（原理等同于方法1）
# cases01 = [dict(zip(data01[0], data01[x])) for x in range(1, len(data01))]

# 方法3
# cases01 = []
# # enumerate()：获取列表中的索引以及数据
# for (k, v) in enumerate(data01):
#     if k > 0:
#         # zip()：数据的聚合打包
#         cases01.append(dict(zip(data01[0], v)))

# 字典推导式
dict01 = {i: i ** 2 for i in range(1, 11)}
print(dict01)