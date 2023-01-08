#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 11:47
# @Author  : nujaijey
# @File    : utils.py
# @Desc    :

import random
import string


def random_int(sta, end):
    return random.Random().randint(sta, end)


def get_random_string(str_len: int) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len)
    )


