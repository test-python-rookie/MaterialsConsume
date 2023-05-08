import os
import time
import glob
import data
import unittest
import HTMLTestRunner


if __name__ == '__main__':
    for file_name in glob.glob('{}/*'.format(data.join_path)):
        os.remove(file_name)
        # print(file_name)
    case_login = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_login.py")
    case_inhouse = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_inhouse.py")
    case_request = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_request.py")
    case_agree = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_agree.py")
    case_outhouse = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_outhouse.py")
    case_departmentplan = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_departmentplan.py")
    case_planaudit = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_planaudit.py")
    # # 创建套件
    # suit = unittest.TestSuite()
    # # 添加套件用例
    # suit.addTest(case_login)
    # suit.addTest(case_inhouse)
    # suit.addTest(case_request)
    # suit.addTest(case_agree)
    # suit.addTest(case_outhouse)
    # run = unittest.TextTestRunner()
    # run.run(suit)
    # 生成测试报告
    report_file_path = data.report_path + '/test_report_{}.html'.format(time.strftime('%Y%m%d%H%M%S'))
    with open(report_file_path,'wb') as f:
        print(report_file_path)
        # 创建套件
        suit = unittest.TestSuite()
        # 添加套件用例
        suit.addTest(case_login)
        suit.addTest(case_inhouse)
        suit.addTest(case_request)
        suit.addTest(case_agree)
        suit.addTest(case_outhouse)
        suit.addTest(case_departmentplan)
        suit.addTest(case_planaudit)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='',description='',verbosity=2)
        runner.run(suit)



