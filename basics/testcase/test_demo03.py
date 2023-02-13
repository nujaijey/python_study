#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 17:02
# @Author  : nujaijey
# @File    : test_demo03.py
# @Desc    :
import requests
from basics.utils.utils import get_random_string


class TestDome03:
    base_url = 'https://day.manage.qxdaojia.com/api'
    cookie = 'token=1544ed1a-1097-4c97-abb2-caef41e55738; JSESSIONID=NGVjY2UxOWEtMTZmZi00MjgwLTlkZTgtZTQzMGUxZjk4ZTFl'
    authorization = 'Bearer 1544ed1a-1097-4c97-abb2-caef41e55738'
    headers = {
        'cookie': cookie,
        'authorization': authorization
    }

    add_data = {
        "createBy": 1326497106551934978,
        "createName": "叶嘉俊",
        "id": "",
        "marketToolsType": 1,
        "modifiedBy": 1326497106551934978,
        "modifiedName": "叶嘉俊",
        "name": get_random_string(4),
        "sort": 0,
        "status": 1,
        "type": 1
    }

    search_data = {
        "name": add_data['name'],
        "type": add_data['type']
    }

    def test_add_and_search_group(self):
        add_res = requests.request(method='post', url=self.base_url + '/promotionServer/proDirectSellGroup/add',
                                   headers=self.headers, json=self.add_data)
        add_result_json = add_res.json()
        assert add_result_json['code'] == 0
        assert add_result_json['message'] == 'success'
        search_res = requests.request(method='post', url=self.base_url + '/promotionServer/proDirectSellGroup/list',
                                      headers=self.headers, json=self.search_data)
        search_result_json = search_res.json()
        assert search_result_json['code'] == 0
        assert search_result_json['data']['records'][-1]['name'] == self.add_data['name']
