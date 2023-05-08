import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_departmentplan import DataDepartmentplan
from page.page_departmentplan import PageDepartmentplan
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_data():
    return [(DataDepartmentplan().wpmc1, DataDepartmentplan().wpmc2, DataDepartmentplan().jhsl, DataDepartmentplan().jhj)]

class TestRequest(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取登录页面对象
        cls.departmentplan = PageDepartmentplan(GetDriver().get_driver())

    # 结束方法
    # @classmethod
    # def tearDownClass(cls):
    #     # 关闭浏览器
    #     GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_request(self, wpmc1, wpmc2, jhsl, jhj):
        # 调用测试方法
        save_time = self.departmentplan.page_departmentplan(wpmc1, wpmc2, jhsl, jhj)
        sleep(3)
        # 获取断言
        text_time = self.departmentplan.page_departmentplan_pass()
        s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))
        t_time = time.mktime(time.strptime(text_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertTrue(t_time >= s_time)
            self.departmentplan.page_departmentplan_assertionview(data.join_path, DataDepartmentplan().successname)
            print('新增科室计划单成功！！！')
        except AssertionError as e:
            self.departmentplan.page_departmentplan_assertionview(data.join_path, DataDepartmentplan().errorname)
            print('新增科室计划单失败！！！')
            raise AssertionError(e)

    if __name__ == '__main__':
        unittest.main()