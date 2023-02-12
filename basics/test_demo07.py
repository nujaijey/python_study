#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 21:06
# @Author  : nujaijey
# @File    : test_demo07.py
# @Desc    : 连接数据库


import requests

from basics.test_base import TestBase
from basics.utils.database_conn import DatabaseConn
from basics.config.database_config import database_config
from basics.config.requests_config import requests_config


class TestDome07(TestBase):
    client_host = requests_config['client_host']
    backend_host = requests_config['backend_host']

    add_data = {
        "channelSource": "weixin_8000262_1_1_0_0_967026704323182592",
        "urlId": "967026704323182592",
        "userId": "659108"
    }
    search_data = {
        "userId": add_data['userId']
    }

    def test_add_and_record(self):
        self.logger.info("请求数据：" + str(self.add_data))
        add_res = requests.request(method='post', url=self.backend_host + '/adb/promotionData/saveRecord',
                                   headers=self.client_headers,
                                   json=self.add_data)
        add_result_json = add_res.json()
        self.logger.info("响应数据：" + str(add_result_json))
        assert add_result_json['code'] == 0
        assert add_result_json['message'] == 'success'
        # database_conn = DatabaseConn(database_config)
        # excuse_result = database_conn.excuse_sql(
        #     "SELECT * FROM promotion_url_click_record WHERE `user_id` = '659108' ORDER BY `gmt_create` DESC")
        # self.logger.info("执行返回数据：" + str(excuse_result))
        # database_conn.close_conn()
        # assert self.add_data['channelSource'].split('_')[1] in excuse_result[3]
