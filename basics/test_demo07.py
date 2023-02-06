#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 21:06
# @Author  : nujaijey
# @File    : test_demo07.py
# @Desc    :


import requests

from basics.utils.logger_utils import LoggerUtils
from basics.utils.database_conn import DatabaseConn
from basics.utils.database_config import database_config


class TestDome07:
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_host = 'https://day.m.qxdaojia.com/api'
    backend_host = 'https://day.manage.qxdaojia.com/api'
    headers = ''

    login_data = {
        "mobile": "13226645549",
        "verifyCode": "11111",
        "type": "login",
        "thirdType": 3,
        "isShare": "",
        "cityCode": "4403",
        "cityName": "深圳市",
        "activeSource": "H5",
        "sign_params": "APP_ID=1577498216199&TIMESTAMP=20230114113438&SIGN_TYPE=SHA256&NONCE=60pqpnluw8e&SIGN=0F8B2B170C7627553914833B889CC1292DE7395E4CC44688BCE2A5150BB1DFF2"
    }

    def setup_class(self):
        """
        类前置
        """
        self.logger.info("请求数据：" + str(self.login_data))
        res = requests.request(method='post', url=self.client_host + '/malluser/user/verify/validateCode',
                               json=self.login_data)
        result_json = res.json()
        self.logger.info("响应数据：" + str(result_json))
        access_token = result_json['data']['access_token']
        self.headers = {
            'cookie': 'token=' + access_token,
            'authorization': 'Bearer ' + access_token
        }

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
                                   headers=self.headers,
                                   json=self.add_data)
        add_result_json = add_res.json()
        self.logger.info("响应数据：" + str(add_result_json))
        assert add_result_json['code'] == 0
        assert add_result_json['message'] == 'success'
        database_conn = DatabaseConn(database_config)
        excuse_result = database_conn.excuse_sql("SELECT * FROM promotion_url_click_record WHERE `user_id` = '659108' ORDER BY `gmt_create` DESC")
        self.logger.info("执行返回数据：" + str(excuse_result))
        database_conn.close_conn()
        assert self.add_data['channelSource'].split('_')[1] in excuse_result[3]
