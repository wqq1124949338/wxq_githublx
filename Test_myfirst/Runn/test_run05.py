import unittest
# from ddt import ddt,data,unpack
from Testcase_me.test_syslgl import *

class mainfunicton_02(unittest.TestCase):
    #系统登录
    def setUp(self):
        self.q = syslgl()

    # @unittest.skip('跳过')
    def test_01(self):
        a='苹果'
        b='无描述'
        self.q.xzsy_01(a,b)

    # @unittest.skip('跳过')
    def test_02(self):
        s=self.q.sygl_02()
        self.assertEqual(s,'预览')


    # @unittest.skip('跳过')
    def test_03(self):
        self.q.sygl_03()


    # @unittest.skip('跳过')
    def test_04(self):
        a='sa'
        self.q.sygl_04(a)

    # @unittest.skip('跳过')
    def test_05(self):
        self.q.sygl_05()

    # @unittest.skip('跳过')
    def test_06(self):
        a=self.q.sygl_06()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_07(self):
        a=self.q.plcz_07()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_08(self):
        a=self.q.plcz_08()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_09(self):
        a=self.q.plcz_09()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_10(self):
        a = self.q.plcz_10()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_11(self):
        a = self.q.plcz_11()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_12(self):
        a = self.q.plcz_12()

    # @unittest.skip('跳过')
    def test_13(self):
        a='品质'
        self.q.plcz_13(a)

    @unittest.skip('跳过')
    def test_14(self):
        a = self.q.plcz_14()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_15(self):
        a = self.q.plcz_15()
        # self.assertTrue(a)

    # 系统关闭
    def tearDown(self):
        self.q.wxq.quit()

if __name__ == '__main__':
    unittest.main()