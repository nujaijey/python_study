#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 21:47
# @Author  : nujaijey
# @File    : subject_category.py
# @Desc    : 科目类别api类
import requests

from basics.api.api_base import ApiBase
from basics.config.requests_config import requests_config
from basics.testcase.login import Login
from basics.utils.logger_utils import LoggerUtils


class SubjectCategory(ApiBase):

    def __init__(self):
        self.logger = LoggerUtils.getLogger('test_subject_category', 'logs')
        self.backend_headers = Login().backend_headers
        self.backend_host = requests_config['backend_host']

    def add(self, scName, scSort, scStatus):
        request_data = {
            'method': 'post',
            'url': self.backend_host + '/finance/subjectClassification/addOrUpdate',
            'headers': self.backend_headers,
            'json': {
                'scName': scName,
                'scSort': scSort,
                'scStatus': scStatus,
            }
        }
        return self.req(**request_data)

    def search(self, scName, scSort=None, scStatus=None, limit=10, page=1):
        request_data = {
            'method': 'post',
            'url': self.backend_host + '/finance/subjectClassification/listPage',
            'headers': self.backend_headers,
            'json': {
                'scName': scName,
                'scSort': scSort,
                'scStatus': scStatus,
                'limit': limit,
                'page': page
            }
        }
        return self.req(**request_data)

    def edit(self, id, scName, scSort, scStatus):
        request_data = {
            'method': 'post',
            'url': self.backend_host + '/finance/subjectClassification/addOrUpdate',
            'headers': self.backend_headers,
            'json': {
                'id': id,
                'scName': scName,
                'scSort': scSort,
                'scStatus': scStatus,
            }
        }
        return self.req(**request_data)

    def log(self, id):
        request_data = {
            'method': 'post',
            'url': self.backend_host + '/elastic/log/listLogById',
            'headers': self.backend_headers,
            'data': {
                'id': id,
                'index': 'salary_subject_classification_log'
            }
        }
        return self.req(**request_data)

    def update_status(self, id, status):
        request_data = {
            'method': 'get',
            'url': self.backend_host + '/finance/subjectClassification/updateStatus',
            'headers': self.backend_headers,
            'data': {
                'id': id,
                'status': status
            }
        }
        return self.req(**request_data)
