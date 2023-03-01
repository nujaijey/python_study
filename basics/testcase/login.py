#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 20:50
# @Author  : nujaijey
# @File    : login.py
# @Desc    : 登录
import requests
from basics.utils.logger_utils import LoggerUtils
from basics.config.requests_config import requests_config


class Login:
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_headers = ''
    backend_headers = ''

    client_login_data = {
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

    backend_login_data = {
        "username": "yejiajun",
        "password": "123456",
        "APP_ID": "1552274783265",
        "TIMESTAMP": "20230212151345",
        "SIGN_TYPE": "SHA256",
        "NONCE": "j5jwcb38gb",
        "SIGN": "9D4CE0D9F3345667EDB6573B16BFF6F08B53465019554B8AA9D89191D183C77C"
    }

    def __init__(self):
        self.client_headers = self.client_login()
        self.backend_headers = self.backend_login()

    def client_login(self):
        self.logger.info("客户端登录请求数据：" + str(self.client_login_data))
        res = requests.request(method='post', url=requests_config['client_host'] + '/malluser/user/verify/validateCode',
                               json=self.client_login_data)
        result_json = res.json()
        self.logger.info("客户端登录响应数据：" + str(result_json))
        access_token = result_json['data']['access_token']
        return {
            'cookie': 'token=' + access_token,
            'authorization': 'Bearer ' + access_token
        }

    def backend_login(self):
        self.logger.info("后台登录请求数据：" + str(self.backend_login_data))
        res = requests.request(method='post',
                               url=requests_config['backend_host'] + '/user/admin/login/token',
                               data=self.backend_login_data)
        result_json = res.json()
        self.logger.info("后台登录响应数据：" + str(result_json))
        access_token = result_json['data']['access_token']
        return {
            'cookie': 'token=' + access_token,
            'authorization': 'Bearer ' + access_token
        }
