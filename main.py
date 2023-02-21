import unittest
if __name__ == '__main__':
    case_path1 = unittest.defaultTestLoader.discover('./scripts', pattern="test_login.py")
    case_path2 = unittest.defaultTestLoader.discover('./scripts', pattern="test_inhouse.py")
    # 创建套件
    suit = unittest.TestSuite()
    # 添加套件用例
    suit.addTest(case_path1)
    suit.addTest(case_path2)
    run = unittest.TextTestRunner()
    run.run(suit)



