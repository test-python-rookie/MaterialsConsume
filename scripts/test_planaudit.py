import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_planaudit import DataPlanaudit
from page.page_planaudit import PagePlanaudit
from time import sleep
from selenium.webdriver.common.keys import Keys



class TestRequest(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取登录页面对象
        cls.planaudit = PagePlanaudit(GetDriver().get_driver())

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        GetDriver().quit_driver()

    # 新建测试方法
    def test_request(self):
        # 调用测试方法
        self.planaudit.page_planaudit()
        sleep(3)
        # 获取断言
        text_type = self.planaudit.page_planaudit_pass()
        try:
            self.assertEqual(text_type, '已审计')
            self.planaudit.page_planaudit_assertionview(data.join_path, DataPlanaudit().successname)
            print('采购计划单审计成功！！！')
        except AssertionError:
            self.planaudit.page_planaudit_assertionview(data.join_path, DataPlanaudit().errorname)
            print('采购计划单审计失败！！！')
            # raise AssertionError(e)

    if __name__ == '__main__':
        unittest.main()