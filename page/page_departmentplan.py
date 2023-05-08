import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PageDepartmentplan(Base):
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

    # 打开二级库房管理
    def page_open_secondary_warehouse(self):
        self.base_click(page.secondary_warehouse, page.secondary_warehouse_num)

    # 点击新增科室采购计划单
    def page_departmentplan_create(self):
        # 打开科室采购计划页面
        self.base_finds_click(page.secondary_warehouse_div, page.secondary_warehouse_div_num, page.departmentplan, page.departmentplan_num)
        sleep(1)
        # 点击新增计划单
        self.base_click(page.departmentplan_create, page.departmentplan_create_num)

    # 输入新增数据
    def page_departmentplan_cdata(self, wpmc1, wpmc2, jhsl, jhj):
        # 物品
        articles1 = self.base_find_elements(page.departmentplan_articles)[page.departmentplan_articles_num]
        self.base_double_click(articles1)
        sleep(1)
        self.base_active_input(wpmc1)
        sleep(1)
        self.base_active_input('Keys.ENTER')
        # 数量
        quantity1 = self.base_find_elements(page.departmentplan_quantity)[page.departmentplan_quantity_num]
        self.base_double_click(quantity1)
        sleep(1)
        self.base_active_input(jhsl)
        sleep(1)
        # 进货价
        price1 = self.base_find_elements(page.departmentplan_price)[page.departmentplan_price_num]
        self.base_double_click(price1)
        sleep(1)
        self.base_active_input(jhj)
        sleep(1)
        # 新增第二条数据
        self.base_click(page.two_departmentplan, page.two_departmentplan_num)
        # 第二条物品
        articles2 = self.base_find_elements(page.two_departmentplan_articles)[page.two_departmentplan_articles_num]
        self.base_double_click(articles2)
        sleep(1)
        self.base_active_input(wpmc2)
        sleep(1)
        self.base_active_input('Keys.ENTER')
        # 第二条数量
        quantity2 = self.base_find_elements(page.two_departmentplan_quantity)[page.two_departmentplan_quantity_num]
        self.base_double_click(quantity2)
        sleep(1)
        self.base_active_input(jhsl)
        sleep(1)
        # 第二条进货价
        price2 = self.base_find_elements(page.two_departmentplan_price)[page.two_departmentplan_price_num]
        self.base_double_click(price2)
        sleep(1)
        self.base_active_input(jhj)
        sleep(1)
        # 计划单单确认前最新时间
        self.save_time = time.strftime('%Y-%m-%d %H:%M')
        # 计划单确认
        self.base_click(page.departmentplan_confirm1, page.departmentplan_confirm1_num)
        sleep(1)
        self.base_finds_click(page.departmentplan_confirm2, page.departmentplan_confirm2_num, page.departmentplan_confirm3, page.departmentplan_confirm3_num)
        # 计划单保存
        # self.base_click(page.departmentplan_save, page.departmentplan_save_num)
        # 计划单取消
        # self.base_click(page.departmentplan_cancel, page.departmentplan_cancel_num)
        return self.save_time

    # 获取断言
    def page_departmentplan_pass(self):
        return self.base_finds_text(page.departmentplan_text1, page.departmentplan_text1_num, page.departmentplan_text2, page.departmentplan_text2_num)

    # 截图
    def page_departmentplan_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)


    # 组装新增业务方法
    def page_departmentplan(self, wpmc1, wpmc2, jhsl, jhj):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        self.page_open_secondary_warehouse()
        sleep(1)
        self.page_departmentplan_create()
        sleep(2)
        self.save_time = self.page_departmentplan_cdata(wpmc1, wpmc2, jhsl, jhj)
        return self.save_time
