# 新增入库单参数
class DataInhouse:
    # 物品名称或编号（selenium输入时不知为什么最后一个字符不能正常识别，所以我在物品编码后面加了一个空格）
    wpmc1 = 'H00003 '
    wpmc2 = 'H00004 '
    # 入库数量
    rksl = '10'
    # 成功截图名称
    successname = '02_inhouse_success'
    # 失败截图名称
    errorname = '02_inhouse_Fail'