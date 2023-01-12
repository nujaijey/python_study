#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 21:39
# @Author  : nujaijey
# @File    : test_demo06.py
# @Desc    :
import requests

from basics.utils.logger_utils import LoggerUtils


class TestDome06:
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_host = 'https://day.m.qxdaojia.com/api'
    backend_host = 'https://day.manage.qxdaojia.com/api'
    headers = ''

    login_data = {
        "mobile": "13226645549",
        "verifyCode": "1111",
        "type": "login",
        "thirdType": 3,
        "isShare": "",
        "cityCode": "4403",
        "cityName": "深圳市",
        "activeSource": "H5"
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

    save_order_data = {
        "settlementCode": "8vOLzaIm",
        "uaId": "1604740893219893250",
        "attributeBid": "868549471703662592",
        "toOrderWay": "normal",
        "calcAmount": 0,
        "orderSource": "web",
        "adSourceNum": "",
        "paymentMode": "wechatpay",
        "balanceStatus": False,
        "voucherStatus": True,
        "orderSaveSaleRemarkDtos": [{
            "remarks": "",
            "categoryId": "17"
        }],
        "referralPhone": "",
        "bookingOrderId": "1043579902781030400",
        "couponIds": "",
        "goodsBids": "840156700295036928",
        "channelSource": "",
        "timeSources": [],
        "cityCode": "4403",
        "latitude": "22.546768",
        "longitude": "114.086050",
        "skills": [],
        "userId": "659108",
        "goodsBid": "840156700295036928",
        "channelId": "",
        "activityId": "",
        "activityName": "",
        "flowSource": "",
        "clueOrder": "",
        "markCode": "9J3F_a1",
        "map": {
            "840156700295036928": "mp_1578927199357714434"
        },
        "sourceType": "web",
        "channelSourceTime": "",
        "additionalGoodsDTOS": [],
        "orderCouponReduceDTOS": [{
            "goodsAttributeBid": "868549471703662592",
            "goodsBid": "840156700295036928",
            "isCouponReduce": 1
        }]
    }

    def test_save_and_search_order(self):
        self.logger.info("请求数据：" + str(self.save_order_data))
        save_res = requests.request(method='post', url=self.client_host + '/orderbusiness/open/orderEdit/saveMallOrder',
                                    headers=self.headers, json=self.save_order_data)
        save_result_json = save_res.json()
        self.logger.info("响应数据：" + str(save_result_json))
        assert save_result_json['code'] == 0
        search_res = requests.request(method='post',
                                      url=self.client_host + '/orderbusiness/open/orderQuery/getAllOrder',
                                      headers=self.headers, json={
                                                                                "page": 1,
                                                                                "limit": 10
                                                                            })
        search_result_json = search_res.json()
        self.logger.info("响应数据：" + str(search_result_json))
        assert save_result_json['data']['orderMainId'] == search_result_json['data']['records'][0]['mainOrderId']
