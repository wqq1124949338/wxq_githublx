import sys
import os
from HTMLTestRunnerNew import HTMLTestRunner
curPath = os.path.abspath(os.path.dirname(r'D:\Users\Administrator\PycharmProjects\Test_myfirst\Runn\runcase.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import time
def run01():
   reportpath = "../report"
   test_dir = '../'
   suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
   now = time.strftime('%Y-%m-%d_%H_%M_%S')
   reportname = reportpath + '\\' + 'TestResult' + now + '.html'
   with open(reportname, 'wb') as f:
      runner =HTMLTestRunner(
         stream=f,
         title='测试报告',
         verbosity = 2,
         tester = "仵向前",
         description='Test the import testcase'
      )
      runner.run(suite)

run01()