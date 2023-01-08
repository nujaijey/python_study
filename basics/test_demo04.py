#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 19:58
# @Author  : nujaijey
# @File    : test_demo04.py
# @Desc    :
import pytest
import requests
from basics.utils.utils import random_int
from basics.utils.utils import get_random_string
from basics.utils.logger_utils import LoggerUtils


class TestDome04:
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    base_url = 'https://day.manage.qxdaojia.com/api'
    cookie = 'token=1544ed1a-1097-4c97-abb2-caef41e55738; JSESSIONID=NGVjY2UxOWEtMTZmZi00MjgwLTlkZTgtZTQzMGUxZjk4ZTFl'
    authorization = 'Bearer 1544ed1a-1097-4c97-abb2-caef41e55738'
    headers = {
        'cookie': cookie,
        'authorization': authorization
    }

    add_success_data = [
        {
            "createBy": 1326497106551934978,
            "createName": "叶嘉俊",
            "currentRate": random_int(0, 50),
            "id": "",
            "isDefault": 2,
            "modifiedBy": 1326497106551934978,
            "modifiedName": "叶嘉俊",
            "role": 1,
            "schemeName": "客户经理" + get_random_string(4),
            "superRate": random_int(0, 50),
            "supersRate": random_int(0, 50)
        },
        {
            "createBy": 1326497106551934978,
            "createName": "叶嘉俊",
            "currentRate": random_int(0, 50),
            "id": "",
            "isDefault": 2,
            "modifiedBy": 1326497106551934978,
            "modifiedName": "叶嘉俊",
            "role": 6,
            "schemeName": "渠道代理商" + get_random_string(4),
            "superRate": random_int(0, 50),
            "supersRate": random_int(0, 50)
        },
        {
            "createBy": 1326497106551934978,
            "createName": "叶嘉俊",
            "currentRate": random_int(0, 50),
            "id": "",
            "isDefault": 2,
            "modifiedBy": 1326497106551934978,
            "modifiedName": "叶嘉俊",
            "role": 8,
            "schemeName": "分公司经理" + get_random_string(4),
            "superRate": random_int(0, 50),
            "supersRate": random_int(0, 50)
        },
        {
            "createBy": 1326497106551934978,
            "createName": "叶嘉俊",
            "currentRate": random_int(0, 50),
            "id": "",
            "isDefault": 2,
            "modifiedBy": 1326497106551934978,
            "modifiedName": "叶嘉俊",
            "role": 9,
            "schemeName": "销售代表" + get_random_string(4),
            "superRate": random_int(0, 50),
            "supersRate": random_int(0, 50)
        }
    ]

    @pytest.mark.parametrize('add_success_data', add_success_data)
    def test_add_commission_success(self, add_success_data):
        self.logger.info("请求数据：" + str(add_success_data))
        res = requests.request(method='post', url=self.base_url + '/promotionServer/commission/add',
                               headers=self.headers, json=add_success_data)
        result_json = res.json()
        self.logger.info("响应数据：" + str(result_json))
        assert result_json['code'] == 0
        assert result_json['message'] == '添加成功！'
        role = add_success_data['role']
        # if role == 1 or role == 8 or role == 9:
        #     assert
        # if role == 6:
        #     pass
