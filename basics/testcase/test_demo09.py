#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 22:29
# @Author  : nujaijey
# @File    : test_demo09.py
# @Desc    :
import pytest
import yaml
import requests

from basics.testcase.test_base import TestBase
from basics.utils.logger_utils import LoggerUtils
from basics.config.requests_config import requests_config


class TestDemo09(TestBase):
    logger = LoggerUtils.getLogger('testdemo09', 'logs')
    client_host = requests_config['client_host']
    backend_host = requests_config['backend_host']

    @pytest.mark.parametrize('add_success_data', yaml.safe_load(
        open(r'D:\PycharmProjects\python_study\basics\data\subject_category_data.yaml', encoding='utf-8'))['add_data'][
        'success'])
    def test_add_success(self, add_success_data):
        self.replace_formal_dict_2_actual(add_success_data)
        self.logger.info("新增请求数据：" + str(add_success_data))
        add_res = requests.request(method='post', url=self.backend_host + '/finance/subjectClassification/addOrUpdate',
                                   headers=self.backend_headers,
                                   json=add_success_data['data'])
        add_result_json = add_res.json()
        self.logger.info("新增响应数据：" + str(add_result_json))
        assert add_result_json['code'] == 0
        assert add_result_json['message'] == 'success'
        search_res = requests.request(method='post', url=self.backend_host + '/finance/subjectClassification/listPage',
                                      headers=self.backend_headers,
                                      json={
                                          'scName': add_success_data['data']['scName'],
                                          'scSort': None,
                                          'scStatus': None,
                                          'limit': 10,
                                          'page': 1
                                      })
        self.logger.info("查询请求数据：" + str(add_success_data))
        search_result_json = search_res.json()
        self.logger.info("查询响应数据：" + str(search_result_json))
        assert search_result_json['code'] == 0
        assert search_result_json['message'] == 'success'
        assert search_result_json['data']['records'][0]['scStatus'] == 1
        assert search_result_json['data']['records'][0]['scSort'] == add_success_data['data']['scSort']
        assert search_result_json['data']['records'][0]['scName'] == add_success_data['data']['scName']
