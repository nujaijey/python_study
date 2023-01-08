#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/20 9:31
# @Author  : nujaijey
# @File    : 文件.py
# @Desc    :

# 内置函数open()
# 操作文件的步骤：
# 1、打开文件：内置函数open()
# 2、进行操作（读/写）
#     read()：默认读取文件中所有的内容
#     readline()：读取一行内容
#     readlines()：按行读取所有的内容，返回一个列表
# 3、关闭文件：close()

# 打开文件，返回文件的句柄
f = open(file='biji.txt', mode='r', encoding='utf-8')
# 读取文件的内容
res = f.read()
print(res)

# 打开文件，返回文件的句柄
f = open(file='biji001.txt', mode='a', encoding='utf-8')
# 追加写入内容
f.write("\n" + "python001")

# 打开文件，返回文件的句柄
f = open(file='biji001.txt', mode='w', encoding='utf-8')
# 覆盖写入内容
f.write("\n" + "python002")

# 关闭文件
f.close()

# 上下文管理器with
with open('biji.txt', 'r') as file:
    print(file.read())
