import unittest
from Testcase_me.test_fwmgl import *
class mainfunicton_03(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.q=fwmgl()

    # @unittest.skip("跳过")
    def test_01(self):

        s=self.q.fwmsc_01()
        # self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_02(self):

        s=self.q.fwmsc_02()
        self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_03(self):

        s=self.q.fwmsc_03()
        self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_04(self):
        s=self.q.fwmsc_04()
        self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_05(self):
        s = self.q.dgsc_05()
        self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_06(self):
        s = self.q.dgsc_06()
        self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_07(self):
        s = self.q.dgsc_07()
        self.assertTrue(s)

    # @unittest.skip("跳过")
    def test_08(self):
        s = self.q.dgsc_08()
        self.assertTrue(s)

    @unittest.skip("跳过")
    def test_09(self):
        s = self.q.plsc_09()
   # self.assertTrue(s)
    @unittest.skip("跳过")
    def test_10(self):
        self.q.plsc_10()

    @unittest.skip("跳过")
    def test_11(self):
        self.q.plsc_11()

    @unittest.skip("跳过")
    def test_12(self):
        self.q.plsc_12()

    @unittest.skip("跳过")
    def test_13(self):
        self.q.plsc_13()

    @classmethod
    def tearDownClass(self):

        self.q.wxq.quit()


if __name__ == '__main__':
    unittest.main()
