#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 22:29
# @Author  : nujaijey
# @File    : test_subject_category.py
# @Desc    : 科目类别测试用例
import pytest
import yaml

from basics.api.subject_category import SubjectCategory
from basics.testcase.test_base import TestBase


class TestSubjectCategory(TestBase):
    sc = SubjectCategory()

    # @pytest.mark.parametrize('add_success_data', yaml.safe_load(
    #     open(r'D:\PycharmProjects\python_study\basics\data\subject_category_data.yaml', encoding='utf-8'))['add_data'][
    #     'success'])
    # def test_add_success(self, add_success_data):
    #     self.replace_formal_dict_2_actual(add_success_data)
    #     self.logger.info("新增请求数据：" + str(add_success_data))
    #     add_res = requests.request(method='post', url=self.backend_host + '/finance/subjectClassification/addOrUpdate',
    #                                headers=self.backend_headers,
    #                                json=add_success_data['data'])
    #     add_result_json = add_res.json()
    #     self.logger.info("新增响应数据：" + str(add_result_json))
    #     assert add_result_json['code'] == 0
    #     assert add_result_json['message'] == 'success'
    #     add_search_data = {
    #                                       'scName': add_success_data['data']['scName'],
    #                                       'scSort': None,
    #                                       'scStatus': None,
    #                                       'limit': 10,
    #                                       'page': 1
    #                                   }
    #     self.logger.info("查询请求数据：" + str(add_search_data))
    #     add_search_res = requests.request(method='post', url=self.backend_host + '/finance/subjectClassification/listPage',
    #                                   headers=self.backend_headers,
    #                                   json=add_search_data)
    #     add_search_result_json = add_search_res.json()
    #     self.logger.info("查询响应数据：" + str(add_search_result_json))
    #     assert add_search_result_json['code'] == 0
    #     assert add_search_result_json['message'] == 'success'
    #     assert add_search_result_json['data']['records'][0]['scStatus'] == 1
    #     assert add_search_result_json['data']['records'][0]['scSort'] == add_success_data['data']['scSort']
    #     assert add_search_result_json['data']['records'][0]['scName'] == add_success_data['data']['scName']

    def test_scene(self):
        add_data = {
            'desc': '新增场景',
            'data': {
                'scName': 'ye${random(5)}',
                'scSort': 1,
                'scStatus': None
            }
        }
        self.replace_formal_dict_2_actual(add_data)
        self.logger.info("说明：" + str(add_data['desc']))
        add_result_json = self.sc.add(**add_data['data'])
        assert add_result_json['code'] == 0

        add_search_data = {
            'scName': add_data['data']['scName']
        }
        self.logger.info("说明：新增查询")
        add_search_result_json = self.sc.search(**add_search_data)
        add_search_result_records = add_search_result_json['data']['records'][0]
        assert add_search_result_records['scStatus'] == 1
        assert add_search_result_records['scSort'] == add_data['data']['scSort']
        assert add_search_result_records['scName'] == add_data['data']['scName']

        add_log_data = {
            'desc': '新增日志场景',
            'data': {
                'id': str(add_search_result_records['id'])
            }
        }
        self.logger.info("说明：" + str(add_log_data['desc']))
        add_log_result_records = []
        while not add_log_result_records:
            add_log_result_json = self.sc.log(**add_log_data['data'])
            add_log_result_records = add_log_result_json['data']['records']
        assert add_log_result_records[0]['businessId'] == str(add_log_data['data']['id'])
        assert '新增' in add_log_result_records[0]['operationTypeName']

        edit_data = {
            'desc': '编辑场景',
            'data': {
                'id': add_search_result_records['id'],
                'scName': 'ye${random(5)}',
                'scSort': 2,
                'scStatus': None
            }
        }
        self.replace_formal_dict_2_actual(edit_data)
        self.logger.info("说明：" + str(edit_data['desc']))
        edit_result_json = self.sc.edit(**edit_data['data'])
        assert edit_result_json['code'] == 0

        edit_search_data = {
            'scName': edit_data['data']['scName']
        }
        # 修改前数据查询
        # 断言数据查询结果无数据（名字不重复的情况）
        self.logger.info("说明：修改前数据查询")
        bf_edit_search_result_json = self.sc.search(**add_search_data)
        assert bf_edit_search_result_json['data']['records'] == []
        # 修改后数据查询
        self.logger.info("说明：修改后数据查询")
        af_edit_search_result_json = self.sc.search(**edit_search_data)
        edit_search_result_records = af_edit_search_result_json['data']['records'][0]
        assert edit_search_result_records['scStatus'] == 1
        assert edit_search_result_records['scSort'] == edit_data['data']['scSort']
        assert edit_search_result_records['scName'] == edit_data['data']['scName']

        edit_log_data = {
            'desc': '编辑日志场景',
            'data': {
                'id': edit_data['data']['id']
            }
        }
        self.logger.info("说明：" + str(edit_log_data['desc']))
        edit_log_result_records = []
        while '修改' not in str(edit_log_result_records):
            edit_log_result_json = self.sc.log(**edit_log_data['data'])
            edit_log_result_records = edit_log_result_json['data']['records']
        assert edit_log_result_records[0]['businessId'] == add_log_data['data']['id']
        assert '修改' in edit_log_result_records[0]['operationTypeName']

    @pytest.mark.parametrize('add_success_data', yaml.safe_load(
        open(r'D:\PycharmProjects\python_study\basics\data\subject_category_data.yaml', encoding='utf-8'))
    ['add_data']['success'])
    def test_add_success(self, add_success_data):
        self.replace_formal_dict_2_actual(add_success_data)
        self.logger.info("说明：" + str(add_success_data['desc']))
        add_result_json = self.sc.add(**add_success_data['data'])
        assert add_result_json['code'] == 0
        assert add_result_json['message'] == 'success'
        add_search_data = {
            'scName': add_success_data['data']['scName'],
            'scSort': None,
            'scStatus': None
        }
        add_search_result_json = self.sc.add_search(**add_search_data)
        assert add_search_result_json['code'] == 0
        assert add_search_result_json['message'] == 'success'
        assert add_search_result_json['data']['records'][0]['scStatus'] == 1
        assert add_search_result_json['data']['records'][0]['scSort'] == add_success_data['data']['scSort']
        assert add_search_result_json['data']['records'][0]['scName'] == add_success_data['data']['scName']
