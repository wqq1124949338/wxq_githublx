from public.login import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class syslgl(dl):

    # 薪增溯源实例模块的正常新增测试
    def xzsy_01(self, a, b):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('新增溯源实例').click()
        self.wxq.find_element_by_css_selector('.form-control').send_keys(a)
        self.wxq.switch_to.frame(0)
        self.wxq.find_element_by_css_selector('body').send_keys(Keys.TAB)
        self.wxq.find_element_by_css_selector('body').send_keys(b)
        self.wxq.switch_to.default_content()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.btn')
        time.sleep(2)

    # 溯源实例管理模块的查看功能测试(溯源实例名称)
    def sygl_02(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/ul/li[2]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)').click()
        time.sleep(2)
        a = self.wxq.find_element_by_css_selector('.layui-layer-title').text
        return a

    # 溯源实例管理模块的刷新功能测试
    def sygl_03(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/ul/li[2]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.btn-default').click()
        time.sleep(3)

    # 溯源实例管理模块的开始搜索功能测试
    def sygl_04(self, a):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/ul/li[2]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('#key').send_keys(a)
        self.wxq.find_element_by_css_selector('button.btn:nth-child(2)').click()
        time.sleep(3)

    #  溯源实例管理模块的编辑功能测试
    def sygl_05(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/ul/li[2]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)').click()
        self.wxq.find_element_by_css_selector('.form-control').clear()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.form-control').send_keys('sadsdas')
        time.sleep(2)
        self.wxq.find_element_by_css_selector('.btn')


    # 溯源实例管理模块的删除功能测试
    def sygl_06(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/ul/li[2]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > span:nth-child(2)').click()
        time.sleep(2)
        self.wxq.find_element_by_css_selector('.layui-layer-btn0').click()
        time.sleep(1)
        s = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return s

    # 批量溯源操作模块中的按物流码批量操作正常修改测试
    def plcz_07(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('批量溯源操作').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('#txm').send_keys('53355')
        time.sleep(2)
        Select(self.wxq.find_element_by_css_selector('#s001')).select_by_index(0)
        self.wxq.find_element_by_css_selector('div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)').click()
        time.sleep(1)
        a=self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return a

    # 批量溯源操作模块中的按ID号段批量操作正常修改测试
    def plcz_08(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('批量溯源操作').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector("div.col-sm-2:nth-child(2) > input:nth-child(1)").send_keys('a')
        self.wxq.find_element_by_css_selector('div.col-sm-2:nth-child(3) > input:nth-child(1)').send_keys('a')
        time.sleep(3)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/span').click()
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[2]').click()
        self.wxq.find_element_by_css_selector('div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)').click()
        time.sleep(1)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return a


    # 批量溯源操作模块中的按防伪码批量操作正常修改测试
    def plcz_09(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('批量溯源操作').click()
        time.sleep(1)
        mb=self.wxq.find_element_by_xpath('/html/body/section/section/section/div[3]/div/section/header/h3')
        time.sleep(2)
        self.wxq.execute_script("return arguments[0].scrollIntoView();",mb)
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[1]/div[1]/div/span").click()
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)").click()
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(1)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return a

    # 批量溯源操作模块中的按产品名称批量操作正常修改测试
    def plcz_10(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('批量溯源操作').click()
        time.sleep(1)
        mb=self.wxq.find_element_by_xpath('/html/body/section/section/section/div[4]/div/section/header/h3')
        time.sleep(2)
        self.wxq.execute_script("return arguments[0].scrollIntoView();",mb)
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/span").click()
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(2)
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div[1]/div/span").click()
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[6]").click()
        time.sleep(2)
        self.wxq.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[3]/div/button").click()
        time.sleep(2)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return a

    # 批量溯源操作模块中的按生成日期批量操作正常修改测试
    def plcz_11(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('批量溯源操作').click()
        time.sleep(1)
        mb=self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/header/h3')
        self.wxq.execute_script("return arguments[0].scrollIntoView();",mb)
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/span').click()
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div[1]/div/span').click()
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[7]').click()
        time.sleep(2)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/div/form/div[3]/div/button').click()
        time.sleep(2)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return a

    #溯源操作记录模块的刷新功能测试
    def plcz_12(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('溯源操作记录').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.btn-default').click()
        time.sleep(3)

    # 溯源操作记录模块的开始搜索功能测试
    def plcz_13(self, a):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('溯源操作记录').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('#key').send_keys(a)
        self.wxq.find_element_by_css_selector('button.btn:nth-child(2)').click()
        time.sleep(3)

    # 溯源操作记录模块的单个删除功能
    def plcz_14(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('溯源操作记录').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.layui-layer-btn0').click()
        time.sleep(1)
        a=self.wxq.find_element_by_css_selector('.layui-layer-ico')
        return a

    # 溯源操作记录模块的批量删除功能以及一键选择所有功能测试
    def plcz_15(self):
        self.wxq.find_element_by_link_text('溯源实例管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('溯源操作记录').click()
        time.sleep(1)
        # self.wxq.find_element_by_css_selector('#chkAll').click()
        # time.sleep(2)
        self.wxq.find_element_by_xpath('//*[@id="chk[]"]').click()
        mb = self.wxq.find_element_by_xpath('//*[@id="del"]')
        self.wxq.execute_script("return arguments[0].scrollIntoView();", mb)
        self.wxq.find_element_by_css_selector('#del').click()
        time.sleep(1)
        self.wxq.switch_to.alert.accept()
        time.sleep(1)
        self.wxq.switch_to.alert.accept()
        time.sleep(1)


