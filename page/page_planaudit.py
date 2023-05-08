import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PagePlanaudit(Base):
    # 登录
    # def __init__(self, driver):
    #     self.page_login = PageLogin(driver)
    #     self.page_login.page_login('admin01', '1234')
    #     self.driver = Base(self.page_login)
    # 输入用户名、密码
    def page_login_user(self):
        # 用户名
        self.base_input(page.username, "uitest", page.name_num)
        # 密码
        self.base_input(page.password, "123456", page.pwd_num)

    # 点击登录
    def page_login_btn(self):
        self.base_click(page.login)

    # 打开采购管理
    def page_open_purchase(self):
        self.base_click(page.purchase, page.purchase_num)

    # 点击查询采购计划单
    def page_planaudit_create(self):
        # 打开采购计划页面
        self.base_finds_click(page.purchase_div, page.purchase_div_num, page.planaudit, page.planaudit_num)
        sleep(1)
        # 点击确认日期
        self.base_click(page.confirm_date, page.confirm_date_num)
        sleep(1)
        # 点击搜索按钮
        self.base_click(page.planaudit_search, page.planaudit_search_num)

    # 采购计划审计
    def page_planaudit_cdata(self):
        # 点击第一条数据审计按钮
        self.base_finds_click(page.planaudit_audit1, page.planaudit_audit1_num, page.planaudit_audit2, page.planaudit_audit2_num)
        sleep(2)
        # 审计确认
        self.base_click(page.planaudit_confirm1, page.planaudit_confirm1_num)
        sleep(1)
        # 审计确认后关闭审计页面
        self.base_click(page.planaudit_confirm1, page.planaudit_confirm1_num)

    # 获取断言
    def page_planaudit_pass(self):
        return self.base_finds_text(page.planaudit_audit1, page.planaudit_audit1_num, page.planaudit_type, page.planaudit_type_num)

    # 截图
    def page_planaudit_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)


    # 组装业务方法
    def page_planaudit(self):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        self.page_open_purchase()
        sleep(1)
        self.page_planaudit_create()
        sleep(2)
        self.page_planaudit_cdata()
