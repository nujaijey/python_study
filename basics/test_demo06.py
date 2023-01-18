#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/12 21:39
# @Author  : nujaijey
# @File    : test_demo06.py
# @Desc    :
import time

import pytest
import requests

from basics.utils.logger_utils import LoggerUtils
from basics.utils.utils import get_random_string


class TestDome06:
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

    save_order_success_data = {
        # web网站抵用金购买保姆初体验
        "settlementCode": "",  # 结算码
        "uaId": "1553296906982715393",  # 用户地址Id
        "attributeBid": "",  # 商品规格定价Bid组,逗号分隔
        "toOrderWay": "normal",  # 下单页面进入方式(cart:购物车,normal:其他,group:拼团,后台:manage)
        "calcAmount": 0,
        "orderSource": "web",  # 订单渠道来源 对应source
        "adSourceNum": "",  # 网推账号序号
        "paymentMode": "wechatpay",  # 支付类别(wechatpay:微信支付,alipay:支付宝,bytedancepay:字节跳动)
        "balanceStatus": False,  # 是否使用余额
        "voucherStatus": False,  # 是否使用抵用金
        "orderSaveSaleRemarkDtos": [{  # 商品类型备注对象
            "remarks": "",  # 订单备注
            "categoryId": "17"  # 产品一级类ID
        }],
        "referralPhone": "",  # 推荐人电话
        "bookingOrderId": "1043579902781030400",
        "couponIds": "",  # 优惠劵Ids(逗号隔开)
        "goodsBids": "",  # 商品bid集合，多个商品，分隔
        "channelSource": "",  # 销售信息
        "timeSources": [],  # 预约时间列表
        "cityCode": "4403",  # 春节活动城市编码
        "latitude": "22.608095",  # 春节活动订单纬度
        "longitude": "113.844801",  # 春节活动订单经度
        "skills": [],  # 春节活动白班保姆技能
        "userId": "659108",  # 用户ID
        "goodsBid": "",  # 商品bid集合，多个商品，分隔
        "channelId": "",  # 渠道来源id
        "activityId": "",  # 活动ID
        "activityName": "",  # 活动名称
        "flowSource": "",  # 流量入口来源
        "clueOrder": "",
        "markCode": "HGtK_a1",  # 唯一标识
        "sourceType": "web",  # 来源类型(web:浏览器,android:安卓,ios:苹果,wxweb:微信内置浏览器,wxmini微信小程序,dymini抖音小程序,advert网络推广)
        "channelSourceTime": "",  # 销售信息生成时间
        "additionalGoodsDTOS": [],  # 加购商品列表
        "orderCouponReduceDTOS": [],  # 优惠券减钱列表
        "sign_params": "APP_ID=1577498216199&TIMESTAMP=20230114113214&SIGN_TYPE=SHA256&NONCE=2xxk7x3qubd&SIGN=797A86F0F642CFDD403956F9C5A60FD2B4A2D50AB0715794D25F950440BD175B"
    }

    save_order_diff_data = [
        {
            # web网站抵用金购买保姆初体验
            "settlementCode": get_random_string(8),
            "orderSource": "web",
            "sourceType": "web",
            "couponIds": "",  # 优惠劵Ids(逗号隔开)
            "balanceStatus": False,
            "voucherStatus": True,
            "attributeBid": "868549471703662592",
            "goodsBids": "840156700295036928",
            "goodsBid": "840156700295036928",
            "orderCouponReduceDTOS": [{  # 优惠券减钱列表
                "goodsAttributeBid": "868549471703662592",  # 规格bid
                "goodsBid": "840156700295036928",  # 商品bid
                "isCouponReduce": 1  # 优惠券是否减钱赠送 0:不减钱 1：减钱
            }],
        },
        {
            # wxmini微信小程序抵用金购买保姆初体验
            "settlementCode": get_random_string(8),
            "orderSource": "wxmini",
            "sourceType": "wxmini",
            "couponIds": "",  # 优惠劵Ids(逗号隔开)
            "balanceStatus": False,
            "voucherStatus": True,
            "attributeBid": "868549471703662592",
            "goodsBids": "840156700295036928",
            "goodsBid": "840156700295036928",
            "orderCouponReduceDTOS": [{  # 优惠券减钱列表
                "goodsAttributeBid": "868549471703662592",  # 规格bid
                "goodsBid": "840156700295036928",  # 商品bid
                "isCouponReduce": 1  # 优惠券是否减钱赠送 0:不减钱 1：减钱
            }],
        },
        {
            # web网站余额购买保姆初体验
            "settlementCode": get_random_string(8),
            "orderSource": "web",
            "sourceType": "web",
            "couponIds": "",  # 优惠劵Ids(逗号隔开)
            "balanceStatus": True,
            "voucherStatus": False,
            "attributeBid": "868549471703662592",
            "goodsBids": "840156700295036928",
            "goodsBid": "840156700295036928",
            "orderCouponReduceDTOS": [{  # 优惠券减钱列表
                "goodsAttributeBid": "868549471703662592",  # 规格bid
                "goodsBid": "840156700295036928",  # 商品bid
                "isCouponReduce": 1  # 优惠券是否减钱赠送 0:不减钱 1：减钱
            }],
        },
        {
            # web网站优惠券购买保姆单次
            "settlementCode": get_random_string(8),
            "orderSource": "web",
            "sourceType": "web",
            "couponIds": "1614262780794896385",  # 优惠劵Ids(逗号隔开)
            "balanceStatus": False,
            "voucherStatus": False,
            "attributeBid": "868548104972926976",
            "goodsBids": "840154743807410176",
            "goodsBid": "840154743807410176",
            "orderCouponReduceDTOS": [{  # 优惠券减钱列表
                "goodsAttributeBid": "868548104972926976",  # 规格bid
                "goodsBid": "840154743807410176",  # 商品bid
                "isCouponReduce": 1  # 优惠券是否减钱赠送 0:不减钱 1：减钱
            }],
        },
    ]

    @pytest.mark.parametrize('save_order_diff_data', save_order_diff_data)
    def test_save_success_and_search_order(self, save_order_diff_data):
        self.save_order_success_data['settlementCode'] = save_order_diff_data['settlementCode']
        self.save_order_success_data['orderSource'] = save_order_diff_data['orderSource']
        self.save_order_success_data['sourceType'] = save_order_diff_data['sourceType']
        self.save_order_success_data['couponIds'] = save_order_diff_data['couponIds']
        self.save_order_success_data['attributeBid'] = save_order_diff_data['attributeBid']
        self.save_order_success_data['goodsBids'] = save_order_diff_data['goodsBids']
        self.save_order_success_data['goodsBid'] = save_order_diff_data['goodsBid']
        self.save_order_success_data['balanceStatus'] = save_order_diff_data['balanceStatus']
        self.save_order_success_data['voucherStatus'] = save_order_diff_data['voucherStatus']
        self.save_order_success_data['orderCouponReduceDTOS'] = save_order_diff_data['orderCouponReduceDTOS']
        self.logger.info("请求数据：" + str(self.save_order_success_data))
        save_res = requests.request(method='post', url=self.client_host + '/orderbusiness/open/orderEdit/saveMallOrder',
                                    headers=self.headers, json=self.save_order_success_data)
        save_result_json = save_res.json()
        self.logger.info("响应数据：" + str(save_result_json))
        assert save_result_json['code'] == 0
        search_res = requests.request(method='post',
                                      url=self.client_host + '/orderbusiness/open/orderQuery/getAllOrder',
                                      headers=self.headers, json={
                "page": 1,
                "limit": 10,
                "sign_params": "APP_ID=1577498216199&TIMESTAMP=20230114113547&SIGN_TYPE=SHA256&NONCE=zm8xn95y9ps&SIGN=240DDE39B378289575F890D3AA40DD7318932FD6E705CFA80985BF42344540D3"
            })
        search_result_json = search_res.json()
        self.logger.info("响应数据：" + str(search_result_json))
        assert search_result_json['code'] == 0
        assert search_result_json['message'] == 'success'
        search_result_first_record = search_result_json['data']['records'][0]
        search_result_goods_item = search_result_first_record['orderGoodsItemVoList'][0]
        assert save_result_json['data']['orderMainId'] == search_result_first_record['mainOrderId']
        assert search_result_goods_item['goodBid'] in self.save_order_success_data['goodsBid']
        assert search_result_goods_item['attributeBid'] in self.save_order_success_data['attributeBid']
        if save_result_json['data']['noGoldPay']:
            assert search_result_first_record['payTotal'] == 0
            assert search_result_first_record['payTime'] is None
            assert search_result_first_record['orderTotal'] == search_result_first_record['discountTotal']
        assert search_result_first_record['status'] == 'PENDING_RESERVATION'
        assert self.save_order_success_data['orderSource'] == search_result_first_record['sources']
        time.sleep(5)
