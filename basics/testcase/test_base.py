#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 21:14
# @Author  : nujaijey
# @File    : test_base.py
# @Desc    :
from basics.testcase.login import Login
from basics.utils.custom_str_utils import CustomStrUtils
from basics.utils.fake_utils import Fake
from basics.utils.logger_utils import LoggerUtils
from basics.utils.placeholder_utils import PlaceholderUtils


class TestBase:
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_headers = ''
    backend_headers = ''

    def setup_class(self):
        """
        类前置
        """
        self.client_headers = Login().client_headers
        self.backend_headers = Login().backend_headers

    # 将字典中的形参转换成实参
    def replace_formal_dict_2_actual(self, formal_data: dict):
        for key, value in formal_data.items():
            if type(value) is str:
                formal_data[key] = self.replace_formal_str_2_actual(value)
            elif type(value) is dict:
                self.replace_formal_dict_2_actual(value)
            elif type(value) is list:
                self.replace_formal_list_2_actual(value)

    # 将列表中的形参转成实参
    def replace_formal_list_2_actual(self, formal_list: list):
        for i in range(len(formal_list)):
            i_value = formal_list[i]
            if type(i_value) is str:
                formal_list.insert(i, self.replace_formal_str_2_actual(i_value))
            elif type(i_value) is list:
                self.replace_formal_list_2_actual(i_value)
            elif type(i_value) is dict:
                self.replace_formal_dict_2_actual(i_value)

    # 字符串形参替换
    def replace_formal_str_2_actual(self, formal_str):
        if "${random" in formal_str:
            self.logger.info(f'对 {formal_str} 进行占位符替换')
            formal_map = {}
            # 对随机数形参进行替换
            random_range = CustomStrUtils.get_random_num(formal_str)
            if type(random_range) is int:
                # 获取到了random范围 生成随机数
                random_num = Fake.get_random_string(random_range)
                # 将形参和实参存到map中
                formal_map['random(' + str(random_range) + ')'] = random_num
                return PlaceholderUtils.resolve_str(formal_str, formal_map)
            else:
                self.logger.error('随机数占位符替换失败：' + formal_str)
                return formal_str
        elif "${timeStamp}" in formal_str:
            # 获取时间戳
            ts = Fake.get_time_stamp()
            return PlaceholderUtils.resolve_str(formal_str, {'timeStamp': ts})
        else:
            return formal_str
