import pytest
import requests
import yaml

from basics.testcase.test_base import TestBase
from basics.config.requests_config import requests_config
from basics.utils.logger_utils import LoggerUtils
from basics.utils.utils import random_int, get_random_string


class TestDome08(TestBase):
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_host = requests_config['client_host']
    backend_host = requests_config['backend_host']
    search_data = {'page': 1, 'limit': 10, 'level': 2, 'APP_ID': '1552274783265', 'TIMESTAMP': '20230212152028',
                   'SIGN_TYPE': 'SHA256', 'NONCE': 'gdnm3yezflu',
                   'SIGN': 'A94684CD93F3F1419B8334CFF122E0B86EE10412B288E4BF3F5ADB0344B0D6E3'}

    @pytest.mark.parametrize('member_data', yaml.safe_load(open(r'D:\PycharmProjects\python_study\basics\data\member_data.yaml', encoding='utf-8'))['member_data'])
    def test_join_success(self, member_data):
        add_data = {}
        self.logger.info('请求数据：' + str(member_data))
        join_res = requests.request(method='post',
                                    url=self.client_host + '/promotionClient/memberManage/supplementMemberInfo',
                                    json=member_data['data'])
        join_result_json = join_res.json()
        self.logger.info('响应数据：' + str(join_result_json))
        assert join_result_json['code'] == member_data['expect']['code']
        assert join_result_json['message'] == member_data['expect']['message']
        for i in range(2):
            self.logger.info('请求数据：' + str(self.search_data))
            search_res = requests.request(method='post',
                                          url=self.backend_host + '/promotionClient/memberManage/queryManagerTeamList/approvalList',
                                          headers=self.backend_headers, json=self.search_data)
            search_result_json = search_res.json()
            self.logger.info('响应数据：' + str(search_result_json))
            self.search_data['page'] = int(search_result_json['data']['pages'])
        assert search_result_json['code'] == 0
        assert search_result_json['message'] == 'success'
        assert search_result_json['data']['records'][-1]['memberName'] == self.member_data['name']


def test_yaml():
    yaml_data = yaml.safe_load(open(r'/basics/member_data.yaml', encoding='utf-8'))
    print(yaml_data)
