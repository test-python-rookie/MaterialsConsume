import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_outhouse import DataOuthouse
from page.page_outhouse import PageOuthouse
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_data():
    return 0

class TestOuthouse(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.outhouse = PageOuthouse(GetDriver().get_driver())

    # 结束方法
    def tearDown(self):
        # 关闭浏览器
        GetDriver().quit_driver()

    # 新建测试方法
    # @parameterized.expand(get_data())
    def test_outhouse(self):
        # 调用测试方法
        save_time = self.outhouse.page_outhouse()
        sleep(3)
        # 获取断言
        text_time = self.outhouse.page_outhouse_pass()
        s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertNotEqual(text_time, '')
            try:
                t_time = time.mktime(time.strptime(text_time, '%Y-%m-%d %H:%M'))
                self.assertTrue(t_time >= s_time)
                self.outhouse.page_outhouse_assertionview(data.join_path, DataOuthouse().successname)
                print('审核申领单成功！！！')
            except AssertionError:
                self.outhouse.page_outhouse_assertionview(data.join_path, DataOuthouse().errorname)
                print('审核申领单失败！！！')
        except AssertionError:
            self.outhouse.page_outhouse_assertionview(data.join_path, DataOuthouse().errorname)
            print('审核申领单失败！！！')

    if __name__ == '__main__':
        unittest.main()