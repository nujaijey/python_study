#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 20:48
# @Author  : nujaijey
# @File    : 字符串.py
# @Desc    :

# s1 = ""
# s2 = "   "
# print("s1的长度：", len(s1))
# print("s2的长度：", len(s2))

# s3 = '1234567'
# res3 = s3[0:7:3]
# print(res3)

# s4 = '    python    '
# print(s4)
# res = s4.strip()
# print(res)


s5 = '***python***'
print(s5)
res = s5.strip('*')
print(res)


# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
# 提示：
# 1 <= s.length <= 104
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    # length = ''
    # if s.strip() == '':
    #     print('s不包含字母')
    # elif s.split()[-1] == ' ':
    #     strip_str = s.strip()
    #     length = len(strip_str.split()[-1])
    # else:
    #     length = len(s.split()[-1])
    # print(length)

    strip_s = s.strip()
    split_s = strip_s.split()
    length = len(split_s[-1]) if split_s else 0
    print(length)


lengthOfLastWord('   ')
lengthOfLastWord('Hello World')
lengthOfLastWord('   fly me   to   the moon  ')
