import time
import unittest
import HTMLTestRunnerNew
import sys
import os
curPath = os.path.abspath(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\common\majorfunctionfwm.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def run_sc():
   reportlj="../report"
   test_dir="./"
   zx=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
   now=time.strftime('%Y-%m-%d_%H_%M_%S')
   reportname=reportlj+'\\'+'Test_result'+now+'.html'
   with open(reportname,'wb') as f:
       runner=HTMLTestRunnerNew.HTMLTestRunner(title='溯源测试报告',
                                               stream=f,
                                               description='wxq')
       runner.run(zx)



if __name__ == '__main__':
    run_sc()