import os
import glob
import data
import unittest


if __name__ == '__main__':
    for file_name in glob.glob('{}/*'.format(data.join_path)):
        os.remove(file_name)
        # print(file_name)
    case_login = unittest.defaultTestLoader.discover('./scripts', pattern="test_login.py")
    case_inhouse = unittest.defaultTestLoader.discover('./scripts', pattern="test_inhouse.py")
    # 创建套件
    suit = unittest.TestSuite()
    # 添加套件用例
    suit.addTest(case_login)
    # suit.addTest(case_inhouse)
    run = unittest.TextTestRunner()
    run.run(suit)



