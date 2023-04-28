import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PageRequest(Base):
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

    # 打开二级库房管理
    def page_open_secondary_warehouse(self):
        self.base_click(page.secondary_warehouse, page.secondary_warehouse_num)

    # 点击新增请领单
    def page_request_create(self):
        # 打开请领管理页面
        self.base_finds_click(page.secondary_warehouse_div, page.secondary_warehouse_div_num, page.request, page.request_num)
        sleep(1)
        # 点击新增请领单
        self.base_click(page.create_request, page.create_request_num)

    # 输入新增数据
    def page_request_data(self, wpmc1, wpmc2, qlsl):
        # 请领物品
        articles1 = self.base_find_elements(page.request_articles)[page.request_articles_num]
        self.base_double_click(articles1)
        sleep(1)
        self.base_active_input(wpmc1)
        self.base_active_input('Keys.ENTER')
        # 数量
        quantity1 = self.base_find_elements(page.request_quantity)[page.request_quantity_num]
        self.base_double_click(quantity1)
        sleep(1)
        self.base_active_input(qlsl)
        sleep(1)
        # 新增第二条数据
        self.base_click(page.two_request, page.two_request_num)
        sleep(1)
        # 第二条请领物品
        articles2 = self.base_find_elements(page.two_request_articles)[page.two_request_articles_num]
        self.base_double_click(articles2)
        sleep(1)
        self.base_active_input(wpmc2)
        self.base_active_input('Keys.ENTER')
        # 第二条数量
        quantity2 = self.base_find_elements(page.two_request_quantity)[page.two_request_quantity_num]
        self.base_double_click(quantity2)
        sleep(1)
        self.base_active_input(qlsl)
        sleep(1)
        # 请领确认前最新时间
        self.save_time = time.strftime('%Y-%m-%d %H:%M')
        # 请领单确认
        self.base_click(page.request_confirm1, page.request_confirm1_num)
        sleep(2)
        self.base_finds_click(page.request_confirm2, page.request_confirm2_num, page.request_confirm3, page.request_confirm3_num)
        # 请领单保存
        # self.base_click(page.request_save, page.request_save_num)
        # 请领单取消
        # self.base_click(page.request_cancel, page.request_cancel_num)
        return self.save_time

    # 获取断言
    def page_request_pass(self):
        return self.base_finds_text(page.request_text1, page.request_text1_num, page.request_text2, page.request_text2_num)

    # 截图
    def page_request_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_request(self, wpmc1, wpmc2, qlsl):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        self.page_open_secondary_warehouse()
        sleep(1)
        self.page_request_create()
        sleep(2)
        self.save_time = self.page_request_data(wpmc1, wpmc2, qlsl)
        return self.save_time
