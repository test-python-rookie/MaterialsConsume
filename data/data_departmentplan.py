# 新增请领单参数
class DataDepartmentplan:
    # 物品名称或编号（selenium输入时不知为什么最后一个字符不能正常识别，所以我在物品编码后面加了一个空格）
    wpmc1 = 'H00003 '
    wpmc2 = 'H00004 '
    # 请领数量
    jhsl = '5'
    # 进货价
    jhj = '1.0000'
    # 成功截图名称
    successname = '06_departmentplan_success'
    # 失败截图名称
    errorname = '06_departmentplan_Fail'