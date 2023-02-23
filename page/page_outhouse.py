import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PageOuthouse(Base):
    # 登录
    # def __init__(self, driver):
    #     self.page_login = PageLogin(driver)
    #     self.page_login.page_login('admin01', '1234')
    #     self.driver = Base(self.page_login)
    # 输入用户名、密码
    def page_login_user(self):
        # 用户名
        self.base_input(page.username, "qltest", page.name_num)
        # 密码
        self.base_input(page.password, "123456", page.pwd_num)

    # 点击登录
    def page_login_btn(self):
        self.base_click(page.login)

    # 打开入出库管理
    def page_open_inhouse_outhouse(self):
        self.base_click(page.inhouse_outhouse, page.inhouse_outhouse_num)

    # 点击修改出库单
    def page_outhouse_modify(self):
        # 打开出库管理页面
        self.base_click(page.outhouse, page.outhouse_num)
        sleep(3)
        # 点击修改出库单
        self.base_click(page.modify_outhouse, page.modify_outhouse_num)

    # 修改申领数据
    def page_outhouse_data(self):
        self.save_time = time.strftime('%Y-%m-%d %H:%M')
        # 出库单确认
        self.base_click(page.outhouse_confirm1, page.outhouse_confirm1_num)
        sleep(1)
        self.base_finds_click(page.outhouse_confirm2, page.outhouse_confirm2_num, page.outhouse_confirm3, page.outhouse_confirm3_num)
        # 申领单保存
        # self.base_click(page.outhouse_save, page.outhouse_save_num)
        # # 申领单取消
        # self.base_click(page.outhouse_cancel, page.outhouse_cancel_num)
        sleep(1)
        return self.save_time

    # 获取断言
    def page_outhouse_pass(self):
        return self.base_finds_text(page.outhouse_text1, page.outhouse_text1_num, page.outhouse_text2, page.outhouse_text2_num)

    # 截图
    def page_outhouse_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_outhouse(self):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        # self.page_open_inhouse_outhouse()
        # sleep(1)
        self.page_outhouse_modify()
        sleep(2)
        self.save_time = self.page_outhouse_data()
        return self.save_time
