import unittest
from Testcase_me.test_lcjl01 import *
from public.readfile_01 import *
from ddt import ddt,data,unpack
@ddt()
class mainfunaction_01(unittest.TestCase):
    def setUp(self):
        self.q = cpgl()

    def tearDown(self):
        self.q.wxq.quit()

    sss = exsj()
    lis = sss.tz(r'D:\Users\Administrator\PycharmProjects\Test_myfirst\information\addlb.xlsx', 'name1')
    @data(*lis)
    @unpack
    # @unittest.skip('跳过')
    def test_01(self,a,b):
        leibie=a
        xuhao=b
        self.q.addlb_01(leibie,xuhao)
        # a=self.q.wxq.find_element_by_css_selector('.layui-layer-content')
        # self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_02(self):
        self.q.addlb_02()

    # @unittest.skip('跳过')
    def test_03(self):
        self.q.addlb_03()
        # 断言无法定位
        # a=self.q.wxq.find_element_by_link_text('更新成功！').text()
        # self.assertTrue(a)
    # @unittest.skip('跳过')
    def test_04(self):
        self.q.addlb_04()

    # @unittest.skip('跳过')
    def test_05(self):
        self.q.addlb_05()

    # @unittest.skip('跳过')
    def test_06(self):
        self.q.addlb_06()


    # @unittest.skip('跳过')
    def test_07(self):
        self.q.addlb_07()

    # @unittest.skip('跳过')
    def test_08(self):
        self.q.addlb_08()

    # @unittest.skip('跳过')
    def test_09(self):
        self.q.addlb_09()

    # @unittest.skip('跳过')
    def test_10(self):
        self.q.addlb_10()

    # @unittest.skip('跳过')
    def test_11(self):
        self.q.addlb_11()

    # @unittest.skip('跳过')
    def test_12(self):
        self.q.addlb_12()

    # @unittest.skip('跳过')
    def test_13(self):
        s=self.q.addlb_13()
        self.assertTrue(s)

    # @unittest.skip('跳过')
    def test_14(self):
        a=self.q.addlb_14()
        self.assertTrue(a)

    # @unittest.skip('跳过')
    def test_15(self):
        self.q.addlb_15()

    # @unittest.skip('跳过')
    def test_16(self):
        self.q.addlb_16()

if __name__ == '__main__':
    unittest.main()
