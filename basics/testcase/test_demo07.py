#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 21:06
# @Author  : nujaijey
# @File    : test_demo07.py
# @Desc    : 连接数据库
import pytest
import requests
import yaml

from basics.testcase.test_base import TestBase
from basics.config.requests_config import requests_config


class TestDome07(TestBase):
    client_host = requests_config['client_host']
    backend_host = requests_config['backend_host']

    @pytest.mark.parametrize('add_data', yaml.safe_load(
        open(r'D:\PycharmProjects\python_study\basics\data\record_data.yaml', encoding='utf-8'))['add_data'])
    @pytest.mark.parametrize('search_data', yaml.safe_load(
        open(r'D:\PycharmProjects\python_study\basics\data\record_data.yaml', encoding='utf-8'))['search_data'])
    def test_add_and_search_record(self, add_data, search_data):
        self.logger.info("新增请求数据：" + str(add_data))
        add_res = requests.request(method='post', url=self.client_host + '/adb/promotionData/saveRecord',
                                   headers=self.client_headers,
                                   json=add_data['data'])
        add_result_json = add_res.json()
        self.logger.info("新增响应数据：" + str(add_result_json))
        assert add_result_json['code'] == add_data['expect']['code']
        assert add_result_json['message'] == add_data['expect']['message']
        # database_conn = DatabaseConn(database_config)
        # excuse_result = database_conn.excuse_sql(
        #     "SELECT * FROM promotion_url_click_record WHERE `user_id` = '659108' ORDER BY `gmt_create` DESC")
        # self.logger.info("执行返回数据：" + str(excuse_result))
        # database_conn.close_conn()
        # assert add_data['data']['channelSource'].split('_')[1] in excuse_result[3]

        search_data['data']['userId'] = add_data['data']['userId']
        self.logger.info("查询请求数据：" + str(search_data))
        search_res = requests.request(method='post',
                                      url=self.backend_host + '/adb/promotionData/promotionUrlClickRecordList',
                                      headers=self.backend_headers,
                                      json=search_data['data'])
        search_result_json = search_res.json()
        self.logger.info("查询响应数据：" + str(search_result_json))
        assert search_result_json['code'] == search_data['expect']['code']
        assert search_result_json['message'] == search_data['expect']['message']
        assert add_data['data']['channelSource'].split('_')[1] in search_result_json['data']['records'][0]['urlUserInfo']
