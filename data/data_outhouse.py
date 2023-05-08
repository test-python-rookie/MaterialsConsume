# 修改出库单参数
class DataOuthouse:
    # 物品名称或编号（selenium输入时不知为什么最后一个字符不能正常识别，所以我在物品编码后面加了一个空格）
    wpmc1 = 'H00003 '
    wpmc2 = 'H00004 '
    # 出库数量
    cksl = '5'
    # 成功截图名称
    successname = '05_outhouse_success'
    # 失败截图名称
    errorname = '05_outhouse_Fail'