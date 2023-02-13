#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 21:14
# @Author  : nujaijey
# @File    : test_base.py
# @Desc    :
from basics.testcase.login import Login
from basics.utils.logger_utils import LoggerUtils


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
