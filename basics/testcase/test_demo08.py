import pytest
import requests
import yaml

from basics.testcase.test_base import TestBase
from basics.config.requests_config import requests_config
from basics.utils.logger_utils import LoggerUtils

class TestDome08(TestBase):
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_host = requests_config['client_host']
    backend_host = requests_config['backend_host']

    # 多个数据驱动：笛卡尔积，即数据驱动A每一组数据会和数据驱动B每一组数据匹配运行
    @pytest.mark.parametrize('member_data', yaml.safe_load(
        open(r'D:\PycharmProjects\python_study\basics\data\data.yaml', encoding='utf-8'))['member_data'])
    @pytest.mark.parametrize('search_data', yaml.safe_load(
        open(r'D:\PycharmProjects\python_study\basics\data\data.yaml', encoding='utf-8'))['search_data'])
    def test_join_success(self, member_data, search_data):
        # 如果不想修改源数据的话，可以定义一个运行数据来承接，修改时修改运行数据
        # run_data = {}
        # run_data.update(member_data)
        # run_data['data']['name'] = run_data['data']['accountName']
        self.replace_formal_dict_2_actual(member_data)
        member_data['data']['name'] = member_data['data']['accountName']
        self.logger.info('请求数据：' + str(member_data))
        join_res = requests.request(method='post',
                                    url=self.client_host + '/promotionClient/memberManage/supplementMemberInfo',
                                    json=member_data['data'])
        join_result_json = join_res.json()
        self.logger.info('响应数据：' + str(join_result_json))
        assert join_result_json['code'] == member_data['expect']['code']
        assert join_result_json['message'] == member_data['expect']['message']
        for i in range(2):
            self.logger.info('请求数据：' + str(search_data))
            search_res = requests.request(method='post',
                                          url=self.backend_host + '/promotionClient/memberManage/queryManagerTeamList/approvalList',
                                          headers=self.backend_headers, json=search_data['data'])
            search_result_json = search_res.json()
            self.logger.info('响应数据：' + str(search_result_json))
            self.search_data['page'] = int(search_result_json['data']['pages'])
        assert search_result_json['code'] == search_data['expect']['code']
        assert search_result_json['message'] == search_data['expect']['message']
        assert search_result_json['data']['records'][-1]['memberName'] == member_data['name']


def test_yaml():
    yaml_data = yaml.safe_load(open(r'/basics/data.yaml', encoding='utf-8'))
    print(yaml_data)
