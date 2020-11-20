import unittest
import sys
import os
curPath = os.path.abspath(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\common\majorfunctionfwm.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


if __name__ == "__main__":
    # 测试用例目录
    test_dir = r"../Runn"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, 'test*.py')
    # 测试报告路径
    report_path = r"./"
    with open(report_path,"a") as report:
        runner = unittest.TextTestRunner(stream=report,verbosity=2)
        runner.run(discover)