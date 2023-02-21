from selenium.webdriver.common.by import By

# url
url = r'http://47.92.237.67/materialsconsume/#/login'

# 用户名
username = By.CLASS_NAME, 'el-input__inner'
name_num = 0

# 密码
password = By.CLASS_NAME, 'el-input__inner'
pwd_num = 1

# 登录按钮
login = By.CLASS_NAME, 'el-button'

# # 异常信息
# error = By.CLASS_NAME, 'login-box-title'

# # 通过信息
# succeed = By.CLASS_NAME, 'login-box2'

# 入出库管理
inhouse_outhouse = By.CLASS_NAME, 'el-submenu__title'
inhouse_outhouse_num = 1

# 入库管理
inhouse = By.CLASS_NAME, 'el-menu-item'
inhouse_num = 3

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
pull_down1_num = 6

pull_down2 = By.CLASS_NAME, 'el-select-dropdown__item'
pull_down2_num = 1

# 选择物品
articles1 = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
articles1_num = 12

articles2 = By.CLASS_NAME, 'el-table__row'
articles2_num = 33

# 输入数量
quantity = By.CLASS_NAME, 'normal-padding'
quantity_num = 0

# 输入有效期
today = By.CLASS_NAME, 'normal-padding'
today_num = 7

# 新增入库单保存按钮
inhouse_save = By.CLASS_NAME, 'el-button--medium'
inhouse_save_num = 7

# 新增入库单确认按钮
inhouse_confirm1 = By.CLASS_NAME, 'el-button--medium'
inhouse_confirm1_num = 6

inhouse_confirm2 = By.CLASS_NAME, 'el-message-box'
inhouse_confirm2_num = 0

inhouse_confirm3 = By.CLASS_NAME, 'el-button--primary'
inhouse_confirm3_num = 0

# 入库管理列表最新一条数据的录入时间
text1 = By.CLASS_NAME, 'el-table__row'
text1_num = 0

text2 = By.CLASS_NAME, 'el-tooltip'
text2_num = 0

