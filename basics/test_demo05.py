#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 22:19
# @Author  : nujaijey
# @File    : test_demo05.py
# @Desc    :
import requests

from basics.utils.logger_utils import LoggerUtils


class TestDome05:
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    base_url = 'https://day.manage.qxdaojia.com/api'
    cookie = 'token=1544ed1a-1097-4c97-abb2-caef41e55738; JSESSIONID=NGVjY2UxOWEtMTZmZi00MjgwLTlkZTgtZTQzMGUxZjk4ZTFl'
    authorization = 'Bearer 1544ed1a-1097-4c97-abb2-caef41e55738'
    headers = {
        'cookie': cookie,
        'authorization': authorization
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
        add_res = requests.request(method='post', url=self.base_url + '/adb/promotionData/saveRecord',
                                   headers=self.headers,
                                   json=self.add_data)
        add_result_json = add_res.json()
        self.logger.info("响应数据：" + str(add_result_json))
        assert add_result_json['code'] == 0
        assert add_result_json['message'] == 'success'
        self.logger.info("请求数据：" + str(self.search_data))
        search_res = requests.request(method='post',
                                      url=self.base_url + '/adb/promotionData/promotionUrlClickRecordList',
                                      headers=self.headers, json=self.search_data)
        search_result_json = search_res.json()
        self.logger.info("响应数据：" + str(search_result_json))
        assert search_result_json['code'] == 0
        assert search_result_json['message'] == 'success'
        assert self.add_data['channelSource'].split('_')[1] in search_result_json['data']['records'][0]['urlUserInfo']
