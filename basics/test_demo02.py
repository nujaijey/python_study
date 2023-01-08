#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 15:14
# @Author  : nujaijey
# @File    : test_demo02.py
# @Desc    :
import pytest
import requests


class TestDemo02:
    base_url = 'https://day.manage.qxdaojia.com/api'
    cookie = 'token=1544ed1a-1097-4c97-abb2-caef41e55738; JSESSIONID=NGVjY2UxOWEtMTZmZi00MjgwLTlkZTgtZTQzMGUxZjk4ZTFl'
    authorization = 'Bearer 1544ed1a-1097-4c97-abb2-caef41e55738'
    headers = {
        'cookie': cookie,
        'authorization': authorization
    }

    search_data_name = [
        {
            "ruleName": "111"
        },
        {
            "ruleName": "222"
        }
    ]

    @pytest.mark.parametrize('search_data_name', search_data_name)
    def test_search_by_name(self, search_data_name):
        res = requests.request(method='post', url=self.base_url + '/promotionServer/performanceRule/getRulePage',
                               headers=self.headers, json=search_data_name)
        result_json = res.json()
        # print(result_json)
        assert result_json['code'] == 0
        assert result_json['message'] == 'success'
        # assert result_json['data']['records'][0]['ruleName'] == search_name_data['ruleName']
        for result_list in result_json['data']['records']:
            assert search_data_name['ruleName'] in result_list['ruleName']

    search_data_name_and_status = [
        {
            "ruleName": "111",
            "ruleStatus": 1
        },
        {
            "ruleName": "222",
            "ruleStatus": 0
        }
    ]

    @pytest.mark.parametrize('search_data_name_and_status', search_data_name_and_status)
    def test_search_by_name_and_status(self, search_data_name_and_status):
        res = requests.request(method='post', url=self.base_url + '/promotionServer/performanceRule/getRulePage',
                               headers=self.headers, json=search_data_name_and_status)
        result_json = res.json()
        assert result_json['code'] == 0
        assert result_json['message'] == 'success'
        for result_list in result_json['data']['records']:
            assert search_data_name_and_status['ruleName'] in result_list['ruleName']
            assert search_data_name_and_status['ruleStatus'] == result_list['ruleStatus']