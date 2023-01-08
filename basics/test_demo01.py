#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 10:37
# @Author  : nujaijey
# @File    : test_demo01.py
# @Desc    :
import pytest
import requests
from basics.utils.utils import random_int
from basics.utils.utils import get_random_string


class TestDemo01:
    url = "https://plan-test.ienjoys.com/api/v1/cleaning/addBigCate"
    headers = {"debug": "True", "userId": "3634555426785464790"}
    json_data_fail = {
        'businessType': 1,
        'name': '111'
    }
    json_data_success = [
        {
            'businessType': 1,
            'name': get_random_string(4)
        },
        {
            'businessType': 1,
            'name': get_random_string(4)
        },
        {
            'businessType': 1,
            'name': get_random_string(4)
        }
    ]

    def test_demo_fail(self):
        res = requests.request(method='post', url=self.url, json=self.json_data_fail)
        result_json = res.json()
        assert result_json['code'] == 401
        assert result_json['message'] == '授权失败'

    @pytest.mark.parametrize('json_data_success', json_data_success)
    def test_demo_success(self, json_data_success):
        res = requests.request(method='post', url=self.url, headers=self.headers, json=json_data_success)
        result_json = res.json()
        assert result_json['code'] == 200
        assert result_json['message'] == '成功'
        assert result_json['data']['id']
