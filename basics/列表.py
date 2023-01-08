#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 21:18
# @Author  : nujaijey
# @File    : 列表.py
# @Desc    :

# 添加元素
# li = [11, 22, 33, 44]
# append(元素)：往列表的结尾处添加一个元素
# li.append(99)
# li.append(999)
# print(li)
# insert(索引,元素)：往列表的指定索引位置插入元素
# li.insert(2, '123')
# print(li)
# extend([元素:可迭代对象])：往列表的结尾处一次性添加多个元素
# li.extend([9999, '456'])
# print(li)

# 删除元素
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 11]
# remove(元素)：指定元素进行删除
# li.remove(11)
# print(li)
# pop(索引)：指定索引进行删除
# res = li.pop(5)
# print(res)
# print(li)
# clear()：清空列表中的所有元素
# li.clear()
# print(li)

# 查询元素
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 11]
# list[索引] ：通过索引查询指定位置的元素
# res = li[3]
# print(res)
# index(元素)：通过元素的值获取元素的索引
# res1 = li.index(33)
# print(res1)
# count(元素)：统计某个元素的个数
# print(res2)

# reverse()：对列表进行反转
li = [11, 22, 33, 25, 14, 66, 59, 88, 99, 18, 23, 1]
li.reverse()
print(li)

# sort()：对列表进行排序，多用于列表中元素都为数字类型
li.sort()
print(li)
# 降序排序：sort(reverse=True)
li.sort(reverse=True)
print(li)
