import requests
from basics.test_base import TestBase
from basics.config.requests_config import requests_config
from basics.utils.logger_utils import LoggerUtils
from basics.utils.utils import random_int, get_random_string


class TestDome08(TestBase):
    logger = LoggerUtils.getLogger('testdemo', 'logs')
    client_host = requests_config['client_host']
    backend_host = requests_config['backend_host']

    member_data = {
        'accountName': get_random_string(5),
        'name': get_random_string(5),
        'phone': '132000000' + str(random_int(10, 99)),
        'identityNo': '440111199507122222',
        'bankNo': str(random_int(10000, 99999)),
        'accountBankName': get_random_string(5),
        'accountBankAddress': get_random_string(5),
        'memberRole': 6,
        'specialInstructions': '',
        'teamId': '135',
        'sign_params': 'APP_ID=1577498216199&TIMESTAMP=20230212104706&SIGN_TYPE=SHA256&NONCE=k441xjumjvm&SIGN=CCDA99D576397F54C1D119E8BC0857ED58C817252C5BCEA0922F26615585E220'
    }

    search_data = {'page': 1, 'limit': 10, 'level': 2, 'APP_ID': '1552274783265', 'TIMESTAMP': '20230212152028',
                   'SIGN_TYPE': 'SHA256', 'NONCE': 'gdnm3yezflu',
                   'SIGN': 'A94684CD93F3F1419B8334CFF122E0B86EE10412B288E4BF3F5ADB0344B0D6E3'}

    def test_join_success(self):
        self.logger.info('请求数据：' + str(self.member_data))
        join_res = requests.request(method='post',
                                    url=self.client_host + '/promotionClient/memberManage/supplementMemberInfo',
                                    json=self.member_data)
        join_result_json = join_res.json()
        self.logger.info('响应数据：' + str(join_result_json))
        assert join_result_json['code'] == 0
        assert join_result_json['message'] == 'success'
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
