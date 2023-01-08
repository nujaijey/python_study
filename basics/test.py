#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 10:24
# @Author  : nujaijey
# @File    : test.py
# @Desc    :
import pytest


class TestDemo:
    def setup_class(self):
        """
        类前置
        """
        self.area = 'aaaaa'
        print('this is setup_class fun')

    def setup(self):
        """
        用例前置
        :return:
        """
        print('this is setup fun')

    def test_demo01(self):
        assert 1 == 1

    def test_demo02(self):
        assert 1 == 2

    def teardown(self):
        """
        用例后置
        """
        print('this is teardown fun')

    def teardown_class(self):
        """
        类后置
        """
        print('this is teardown_class fun')


class TestBigCate(TestBase):
    obj_type = ObjectType()

    def setup_class(self):
        self.logger.info('删除测试数据')
        self.database.excuse_sql('delete from cleaning_object_type where name like "c%"')
        self.logger.info('新增测试数据')
        self.obj_type.add_big_cate('chnjx大类', 1)
        self.obj_type.add_big_cate('chnjx大类', 2)

    @pytest.mark.parametrize('desc,big_cate_name,business_type',
                             [('新增1字符的保洁大类', 'c', 1),
                              ('新增15字符的保洁大类', f'chnjx大类{Fake.get_random_string(8)}', 1),
                              ('新增1字符的绿化大类', 'c', 2),
                              ('新增15字符的绿化大类', f'chnjx大类{Fake.get_random_string(8)}', 2),
                              ])
    def test_success_add(self, desc, big_cate_name, business_type):
        self.logger.info(f'正常添加大类-{desc}')
        res = self.obj_type.add_big_cate(big_cate_name, business_type)
        select_res = self.obj_type.get_object_type_select(business_type=business_type)
        add_res = select_res['data']['data'][0]
        assert res['message'] == '成功'
        assert res['data']['id'] is not None
        assert add_res['name'] == big_cate_name
        assert add_res['id'] == res['data']['id']
        assert add_res['level'] == 1


class TestBaseArea(TestBase):
    area = WorkingArea()

    # def test_success_add_area(self):
    #     r = self.area.add_area(Common.PRO_10_CODE, [{"name":"auto_test2"}])
    #     print(r)

    fail_add_data = [
        {
            'name': 'auto_test2',
            'desc': '新增同名区域',
            'expect': '区域已存在'
        },
        {
            'name': '',
            'desc': '区域名称为空',
            'expect': '区域已存在'
        },
        {
            'name': 'chnjx的作业区域123456',
            'desc': '区域名称超过15个字符',
            'expect': "Data too long for column 'name' at row 1"
        }
    ]

    @pytest.mark.parametrize('fail_add_data', fail_add_data)
    def test_fail_add_area(self, fail_add_data):
        self.logger.info(f"添加区域失败用例： {fail_add_data['desc']}")
        r = self.area.add_area(Common.PRO_10_CODE, [{"name": fail_add_data['name']}])
        assert r['code'] == 1001
        assert fail_add_data['expect'] in r['message']


if __name__ == '__main__':
    pytest.main(["test_add_area.py", "-v", "-s"])

# requests.request(method=method, url=self.base_uri + url, headers=self.headers, **kwargs)
