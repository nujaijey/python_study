#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 21:11
# @Author  : nujaijey
# @File    : 循环.py
# @Desc    :

import random

# print('---石头剪刀布游戏开始---')
# print('请按下面提示出拳')
# dic = {1: '石头', 2: '剪刀', 3: '布'}
# while True:
#     print('石头【1】  剪刀【2】  布【3】  结束游戏【4】')
#     # 用户输入的数字
#     user_num = int(input('请输入你的选项：'))
#     # 电脑随机生成数字
#     r_num = random.randint(1, 3)
#     if 1 <= user_num <= 3:
#         # if (user_num == 1 and r_num == 2) or (user_num == 2 and r_num == 3) or (user_num == 3 and r_num == 1):
#         if user_num - r_num == -1 or user_num - r_num == 2:
#             print('您出：{}，电脑出：{}，您赢了'.format(dic[user_num], dic[r_num]))
#         elif user_num == r_num:
#             print('您出：{}，电脑出：{}，平局'.format(dic[user_num], dic[r_num]))
#         else:
#             print('您出：{}，电脑出：{}，您输了'.format(dic[user_num], dic[r_num]))
#     elif user_num == 4:
#         print('游戏结束')
#         break
#     else:
#         print('您出拳有误，请按提示出拳')

# 遍历字符串
for i in 'qwertyuiop':
    print(i)

# 遍历列表
li = [98, 95, 58, 63, 75]
for score in li:
    if score >= 60:
        print('你的成绩是：{}，及格'.format(score))
    else:
        print('你的成绩是：{}，不及格'.format(score))

# 通过索引遍历值
for i in range(0, len(li)):
    print(li[i])

# 遍历列表的索引和值
for i, v in enumerate(li):
    print(f'{i}: {v}')
for i in range(0, len(li)):
    print('{}:{}'.format(i, li[i]))

# 遍历字典
# 默认遍历出来的是键
dic = {1: 'aa', 2: 'bb', 3: 'cc'}
for i in dic:
    print(i)

# 遍历字典的值
for i in dic.values():
    print(i)

# 遍历字典的键和值
for i in dic.items():
    # print(i, type(i))
    # k = i[0]
    # v = i[1]
    # print('key:', k, 'value:', v)
    # 扩展：元组拆包（多个变量接收元组内多个值）
    k, v = i
    print('key:', k, 'value:', v)

for k, v in dic.items():
    print('key:', k, 'value:', v)

# for循环指定循环n次
# 内置函数range()：可以用来生成一个指定长度的序列，序列类型支持遍历
# li = list(range(100))
# print(li)
for i in range(100):
    print('这是第{}遍hello python'.format(i + 1))

for i in range(4):
    for j in range(i + 1):
        print('* ', end='')
    print()

for i in range(4):
    for j in range(4 - i):
        print('* ', end='')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={j * i}', end=' ')
    print()
