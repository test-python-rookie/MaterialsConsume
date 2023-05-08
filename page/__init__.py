from selenium.webdriver.common.by import By

# url
url = r'http://39.98.72.93/materialsconsume/#/login'

# 用户名
username = By.CLASS_NAME, 'el-input__inner'
name_num = 0

# 密码
password = By.CLASS_NAME, 'el-input__inner'
pwd_num = 1

# 登录按钮
login = By.CLASS_NAME, 'el-button'

# 首页
login_text = By.CLASS_NAME, 'no-redirect'
login_text_num = 0

# 入出库管理
inhouse_outhouse = By.CLASS_NAME, 'el-submenu__title'
inhouse_outhouse_num = 1

# 二级库房管理
secondary_warehouse = By.CLASS_NAME, 'el-submenu__title'
secondary_warehouse_num = 6

# 入出库管理的div
inhouse_outhouse_div = By.CLASS_NAME, 'el-submenu'
inhouse_outhouse_div_num = 1

# 二级库房管理的div
secondary_warehouse_div = By.CLASS_NAME, 'el-submenu'
secondary_warehouse_div_num = 6

# 入库管理
inhouse = By.CLASS_NAME, 'el-menu-item'
inhouse_num = 0

# 新增入库单按钮
create_inhouse = By.CLASS_NAME, 'el-button--medium'
create_inhouse_num = 2

# 选择业务类型
business_type = By.CLASS_NAME, 'el-input__inner'
business_type_num = 8

# 选择往来单位
ealing_unit = By.CLASS_NAME, 'el-input__inner'
ealing_unit_num = 9

# 业务类型和往来单位下拉选项
pull_down1 = By.CLASS_NAME, 'el-select-dropdown__list'
pull_down1_num = 8

pull_down2 = By.CLASS_NAME, 'el-select-dropdown__item'
pull_down2_num = 0

# 选择入库物品
inhouse_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
inhouse_articles_num = 9

# 输入入库数量
inhouse_quantity = By.CLASS_NAME, 'normal-padding'
inhouse_quantity_num = 0

# 输入有效期
inhouse_today = By.CLASS_NAME, 'normal-padding'
inhouse_today_num = 4

# 新增第二行数据
two_inhouse = By.CLASS_NAME, 'el-button--small'
two_inhouse_num = 0

# 选择第二行入库物品
two_inhouse_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_inhouse_articles_num = 18

# 输入第二行入库数量
two_inhouse_quantity = By.CLASS_NAME, 'normal-padding'
two_inhouse_quantity_num = 8

# 新增入库单确认按钮
inhouse_confirm1 = By.CLASS_NAME, 'el-button--medium'
inhouse_confirm1_num = 9

inhouse_confirm2 = By.CLASS_NAME, 'el-message-box'
inhouse_confirm2_num = 0

inhouse_confirm3 = By.CLASS_NAME, 'el-button--primary'
inhouse_confirm3_num = 0

# 新增入库单保存按钮
inhouse_save = By.CLASS_NAME, 'el-button--medium'
inhouse_save_num = 10

# 新增入库单取消按钮
inhouse_cancel = By.CLASS_NAME, 'el-button--medium'
inhouse_cancel_num = 11

# 入库管理列表最新一条数据的录入时间
inhouse_text1 = By.CLASS_NAME, 'el-table__row'
inhouse_text1_num = 0

inhouse_text2 = By.CLASS_NAME, 'el-tooltip'
inhouse_text2_num = 0

# 请领管理
request = By.CLASS_NAME, 'el-menu-item'
request_num = 1

# 新增请领单按钮
create_request = By.CLASS_NAME, 'el-button--medium'
create_request_num = 2

# 选择请领物品
request_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
request_articles_num = 2

# 输入请领数量
request_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
request_quantity_num = 3

# 新增第二条请领数据
two_request = By.CLASS_NAME, 'el-button--small'
two_request_num = 0

# 选择第二条请领物品
two_request_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_request_articles_num = 4

# 输入第二条请领数量
two_request_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_request_quantity_num = 5

# 新增请领单确认按钮
request_confirm1 = By.CLASS_NAME, 'el-button--medium'
request_confirm1_num = 6

request_confirm2 = By.CLASS_NAME, 'el-message-box'
request_confirm2_num = 0

request_confirm3 = By.CLASS_NAME, 'el-button--primary'
request_confirm3_num = 0

# 新增请领单保存按钮
request_save = By.CLASS_NAME, 'el-button--medium'
request_save_num = 7

# 新增请领单取消按钮
request_cancel = By.CLASS_NAME, 'el-button--medium'
request_cancel_num = 8

# 请领管理列表最新一条数据的录入时间
request_text1 = By.CLASS_NAME, 'el-table__row'
request_text1_num = 0

request_text2 = By.CLASS_NAME, 'el-tooltip'
request_text2_num = 0

# 申领管理
agree = By.CLASS_NAME, 'el-menu-item'
agree_num = 2

# 修改申领单按钮
modify_agree = By.CLASS_NAME, 'el-button--mini'
modify_agree_num = 0

# 输入申领数量
agree_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
agree_quantity_num = 1

# 输入第二条申领数量
two_agree_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_agree_quantity_num = 2

# 申领单确认按钮
agree_confirm1 = By.CLASS_NAME, 'el-button--medium'
agree_confirm1_num = 5

agree_confirm2 = By.CLASS_NAME, 'el-message-box'
agree_confirm2_num = 0

agree_confirm3 = By.CLASS_NAME, 'el-button--primary'
agree_confirm3_num = 0

# 申领单保存按钮
agree_save = By.CLASS_NAME, 'el-button--medium'
agree_save_num = 6

# 申领单取消按钮
agree_cancel = By.CLASS_NAME, 'el-button--medium'
agree_cancel_num = 7

# 申领单返回主表
agree_master = By.CLASS_NAME, 'el-tabs__item'
agree_master_num = 0

# 申领管理列表最新一条数据的审核时间
agree_text1 = By.CLASS_NAME, 'el-table__row'
agree_text1_num = 0

agree_text2 = By.CLASS_NAME, 'el-tooltip'
agree_text2_num = 7

# 出库管理
outhouse = By.CLASS_NAME, 'el-menu-item'
outhouse_num = 1

# 新增出库单按钮
create_outhouse = By.CLASS_NAME, 'el-button--medium'
create_outhouse_num = 2

# 选择业务类型
outhouse_business_type1 = By.CLASS_NAME, 'el-dialog__body'
outhouse_business_type1_num = 0

outhouse_business_type2 = By.CLASS_NAME, 'el-input__inner'
outhouse_business_type2_num = 0

# 选择往来单位
outhouse_ealing_unit1 = By.CLASS_NAME, 'el-dialog__body'
outhouse_ealing_unit1_num = 0

outhouse_ealing_unit2 = By.CLASS_NAME, 'el-input__inner'
outhouse_ealing_unit2_num = 1

# 业务类型和往来单位下拉选项
outhouse_pull_down1 = By.CLASS_NAME, 'el-select-dropdown__list'
outhouse_pull_down1_num = 7

outhouse_pull_down2 = By.CLASS_NAME, 'el-select-dropdown__item'
outhouse_pull_down2_num = 0

# 选择入库物品
outhouse_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
outhouse_articles_num = 2

# 输入入库数量
outhouse_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
outhouse_quantity_num = 3

# 新增第二条数据
two_outhouse = By.CLASS_NAME, 'el-button--small'
two_outhouse_num = 0

# 选择第二条入库物品
two_outhouse_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_outhouse_articles_num = 4

# 输入第二条入库数量
two_outhouse_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_outhouse_quantity_num = 5

# 修改出库单按钮
modify_outhouse = By.CLASS_NAME, 'el-button--mini'
modify_outhouse_num = 0

# 出库单确认按钮
outhouse_confirm1 = By.CLASS_NAME, 'el-button--medium'
outhouse_confirm1_num = 6

outhouse_confirm2 = By.CLASS_NAME, 'el-message-box'
outhouse_confirm2_num = 0

outhouse_confirm3 = By.CLASS_NAME, 'el-button--primary'
outhouse_confirm3_num = 0

# 出库单保存按钮
outhouse_save = By.CLASS_NAME, 'el-button--medium'
outhouse_save_num = 7

# 出库单取消按钮
outhouse_cancel = By.CLASS_NAME, 'el-button--medium'
outhouse_cancel_num = 8

# 出库管理列表最新一条数据的确认时间
outhouse_text1 = By.CLASS_NAME, 'el-table__row'
outhouse_text1_num = 0

outhouse_text2 = By.CLASS_NAME, 'el-tooltip'
outhouse_text2_num = 8

# 科室采购计划
departmentplan = By.CLASS_NAME, 'el-menu-item'
departmentplan_num = 0

# 新增科室采购计划单按钮
departmentplan_create = By.CLASS_NAME, 'el-button--medium'
departmentplan_create_num = 2

# 选择科室计划物品
departmentplan_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
departmentplan_articles_num = 4

# 输入科室计划数量
departmentplan_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
departmentplan_quantity_num = 6

# 输入科室计划进货价
departmentplan_price = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
departmentplan_price_num = 7

# 新增第二条科室计划数据
two_departmentplan = By.CLASS_NAME, 'el-button--small'
two_departmentplan_num = 0

# 选择第二条科室计划物品
two_departmentplan_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_departmentplan_articles_num = 8

# 输入第二条科室计划数量
two_departmentplan_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_departmentplan_quantity_num = 10

# 输入第二条科室计划进货价
two_departmentplan_price = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
two_departmentplan_price_num = 11

# 新增科室计划单确认按钮
departmentplan_confirm1 = By.CLASS_NAME, 'el-button--medium'
departmentplan_confirm1_num = 6

departmentplan_confirm2 = By.CLASS_NAME, 'el-message-box'
departmentplan_confirm2_num = 0

departmentplan_confirm3 = By.CLASS_NAME, 'el-button--primary'
departmentplan_confirm3_num = 0

# 新增科室计划单保存按钮
departmentplan_save = By.CLASS_NAME, 'el-button--medium'
departmentplan_save_num = 7

# 新增科室计划单取消按钮
departmentplan_cancel = By.CLASS_NAME, 'el-button--medium'
departmentplan_cancel_num = 8

# 科室采购计划列表最新一条数据的制单时间
departmentplan_text1 = By.CLASS_NAME, 'el-table__row'
departmentplan_text1_num = 0

departmentplan_text2 = By.CLASS_NAME, 'el-tooltip'
departmentplan_text2_num = 0

# 采购管理
purchase = By.CLASS_NAME, 'el-submenu__title'
purchase_num = 0

# 采购管理的div
purchase_div = By.CLASS_NAME, 'el-submenu'
purchase_div_num = 0

# 计划审计
planaudit = By.CLASS_NAME, 'el-menu-item'
planaudit_num = 1

# 确认日期
confirm_date = By.CLASS_NAME, 'el-radio__inner'
confirm_date_num = 1

# 搜索
planaudit_search = By.CLASS_NAME, 'el-button--medium'
planaudit_search_num = 0

# 第一条数据审计
planaudit_audit1 = By.CLASS_NAME, 'el-table__row'
planaudit_audit1_num = 0

planaudit_audit2 = By.CLASS_NAME, 'el-button--mini'
planaudit_audit2_num = 1

# 审计确认
planaudit_confirm1 = By.CLASS_NAME, 'el-button--medium'
planaudit_confirm1_num = 4

# 获取计划单确认状态
planaudit_type = By.CLASS_NAME, 'el-tooltip'
planaudit_type_num = 2

