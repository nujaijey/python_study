#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/10 23:19
# @Author  : nujaijey
# @File    : 元组.py
# @Desc    :

# 元组拆包
# 创建元组t1
t1 = 1, 2
# 将t1拆包到a和b
a, b = t1
# 创建元组t2
t2 = 3, 4, t1
# t3 和 t1 是同一个对象，即元组(1, 2)
c, d, t3 = t2
print(a)
print(b)
print(c)
print(d)
print(t3)