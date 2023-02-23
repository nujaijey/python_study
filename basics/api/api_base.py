#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:43
# @Author  : nujaijey
# @File    : api_base.py
# @Desc    : api文件父类
import requests

from basics.config.requests_config import requests_config
from basics.testcase.login import Login
from basics.utils.logger_utils import LoggerUtils


class ApiBase:
    def __init__(self):
        self.logger = LoggerUtils.getLogger('test_subject_category', 'logs')
        self.backend_headers = Login().backend_headers
        self.backend_host = requests_config['backend_host']

    def req(self, method, url, headers, **kwargs):
        self.logger.info("请求数据：" + kwargs.__str__())
        resp = requests.request(method=method, url=url, headers=headers, **kwargs)
        resp_json = resp.json()
        self.logger.info("响应数据：" + str(resp_json))
        return resp_json
