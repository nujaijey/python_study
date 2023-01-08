#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/26 9:11
# @Author  : nujaijey
# @File    : 字典.py
# @Desc    :

# # 添加元素
# dic1 = {"name": "yjj", "age": 24}
# # 通过键进行赋值
# dic1["sex"] = "女"
# # update()：一次性往字典中添加多个元素
# dic1.update({"a0": 00, "a1": 11, "a2": 22})
# print(dic1)

# # 修改元素
# # 通过键进行赋值
# dic2 = {"name": "yjj", "age": 24}
# dic2["age"] = 22
# print(dic2)

# 删除元素
# dic3 = {"name": "yjj", "age": 24}
# # pop(key)：指定键进行删除，返回的是删除元素对应的值
# res3 = dic3.pop("age")
# print(res3)
# print(dic3)
# dic3["a3"] = 33
# dic3["a1"] = 11
# dic3["a2"] = 22
# # popitem()：删除最后一个加入到字典中的元素，返回的是元组形式的删除的键和值
# res4 = dic3.popitem()
# print(res4)
# print(dic3)
# # clear()：清空字典
# dic3.clear()
# print(dic3)

# # 查询元素
# # 通过键进行查询
# dic4 = {"name": "yjj", "age": 24}
# res = dic4["age"]
# print(res)
# # get()：通过键进行查询
# res1 = dic4["name"]
# print(res1)

# dic5 = {"name": "yjj", "age": 24, "sex": "女"}
# res = dic5.keys()
# print(res)
# res1 = list(res)
# print(res1)
# res2 = dic5.values()
# print(res2)
# res3 = list(res2)
# print(res3)
# res4 = dic5.items()
# print(res4)

dic1 = dict([('name', 'yjj'), ('age', 24), ('sex', '女')])
print(dic1)

dic2 = dict(
    name='yjj',
    age=24,
    sex='女')
print(dic2)


