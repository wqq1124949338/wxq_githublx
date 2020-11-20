from selenium.webdriver.support.select import Select
from public.login import *
# import pyautogui
# 防伪码管理模块测试类
class fwmgl(dl):

    # 批量生成防伪码模块正常新增，默认字段不修改
    def fwmsc_01(self):

       self.wxq.find_element_by_link_text('批量生成防伪码').click()
       time.sleep(2)
       self.wxq.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('wee')
       self.wxq.find_element_by_css_selector('div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)').send_keys('100')
       self.wxq.execute_script('document.getElementById("s1").style.display="block";')
       Select(self.wxq.find_element_by_id('s1')).select_by_visible_text('ASD')
       time.sleep(3)
       self.wxq.execute_script('document.getElementById("s2").style.display="block";')
       Select(self.wxq.find_element_by_id('s2')).select_by_visible_text('枇杷露')
       time.sleep(3)
       self.wxq.find_element_by_css_selector('#tj').click()
       time.sleep(1)
       a=self.wxq.find_element_by_css_selector('.layui-layer-ico')
       time.sleep(3)
       return a

    # 批量生成防伪码模块修改生成批次为已存在的内容('202011100955477')，其他字段正常输入
    def fwmsc_02(self):
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').clear()
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('202011100955477')
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('wee')
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)').send_keys('100')
        self.wxq.execute_script('document.getElementById("s1").style.display="block";')
        Select(self.wxq.find_element_by_id('s1')).select_by_visible_text('134sw')
        time.sleep(3)
        self.wxq.execute_script('document.getElementById("s2").style.display="block";')
        Select(self.wxq.find_element_by_id('s2')).select_by_visible_text('扩扩扩')
        time.sleep(3)
        self.wxq.find_element_by_css_selector('#tj').click()
        time.sleep(1)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        time.sleep(3)
        return a


    # 批量生成防伪码模块修改防伪码长度不符合建议长度8-18位，反案例
    def fwmsc_03(self):
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('6')
        time.sleep(3)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('ABC')
        time.sleep(3)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)').send_keys('10')
        self.wxq.execute_script('document.getElementById("s1").style.display="block";')
        Select(self.wxq.find_element_by_id('s1')).select_by_visible_text('ASD')
        time.sleep(3)
        self.wxq.execute_script('document.getElementById("s2").style.display="block";')
        Select(self.wxq.find_element_by_id('s2')).select_by_visible_text('枇杷露')
        time.sleep(3)
        self.wxq.find_element_by_css_selector('#tj').click()
        time.sleep(1)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        time.sleep(3)
        return a

    # 批量生成防伪码模块修改防伪码长度不符合建议前缀前度2-4位，反案例

    def fwmsc_04(self):
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('10')
        time.sleep(3)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('asdasdad')
        time.sleep(3)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)').send_keys('10')
        self.wxq.execute_script('document.getElementById("s1").style.display="block";')
        Select(self.wxq.find_element_by_id('s1')).select_by_visible_text('西安')
        time.sleep(3)
        self.wxq.execute_script('document.getElementById("s2").style.display="block";')
        Select(self.wxq.find_element_by_id('s2')).select_by_visible_text('枇杷露')
        time.sleep(3)
        self.wxq.find_element_by_css_selector('#tj').click()
        time.sleep(1)
        a = self.wxq.find_element_by_css_selector('.layui-layer-ico')
        time.sleep(3)
        return a

    # 单个生成防伪码模块的正常输入，默认生成字段不修改
    def dgsc_05(self):
        self.wxq.find_element_by_link_text('单个生成防伪码').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(4) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.has-next > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4)').click()
        self.wxq.find_element_by_css_selector('.btn').click()
        a=self.wxq.find_element_by_css_selector('.layui-layer-content').text
        return a

    #单个生成防伪码模块的正常输入，修改默认字段生成批次的修改
    def dgsc_06(self):
        self.wxq.find_element_by_link_text('单个生成防伪码').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.col-sm-3 > input:nth-child(1)').clear()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.col-sm-3 > input:nth-child(1)').send_keys('20112036543')
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(4) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.has-next > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector('.btn').click()
        a = self.wxq.find_element_by_css_selector('.layui-layer-content').text
        return a

    #单个生成防伪码模块的正常输入，修改默认字段防伪码的修改
    def dgsc_07(self):

        self.wxq.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('asd45ad4aqwe45')
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(4) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.has-next > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector('.btn').click()
        a = self.wxq.find_element_by_css_selector('.layui-layer-content').text
        return a

    # 单个生成防伪码模块的正常输入，修改默认字段物流码的修改
    def dgsc_08(self):
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('786613156123')
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(4) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.has-next > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5)').click()
        self.wxq.find_element_by_css_selector('.btn').click()
        a = self.wxq.find_element_by_css_selector('.layui-layer-content').text
        return a

    # 批量删除防伪码，按批次删除
    def plsc_09(self):
        self.wxq.find_element_by_link_text('批量删除防伪码').click()
        time.sleep(3)
        self.wxq.find_element_by_css_selector('div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)').click()
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div/button').click()
        time.sleep(3)

    # 批量删除防伪码，按产品删除
    def plsc_10(self):
        self.wxq.find_element_by_css_selector(
            'div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            '.has-next > div:nth-child(2) > div:nth-child(4)').click()
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div/button').click()
        time.sleep(3)


    # 批量删除防伪码，按生成日期删除
    def plsc_11(self):
        a=self.wxq.find_element_by_css_selector('div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
        self.wxq.execute_script('return arguments[0].scrollIntoView();',a)
        self.wxq.find_element_by_css_selector(
            'div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            'div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)').click()
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div[3]/div/section/div/form/div[2]/div/button').click()
        time.sleep(3)

        # 批量删除防伪码，按查询次数删除
    def plsc_12(self):
        a = self.wxq.find_element_by_css_selector(
            'div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > label:nth-child(1)')
        self.wxq.execute_script('return arguments[0].scrollIntoView();', a)
        self.wxq.find_element_by_css_selector(
            '.form-control').clear()
        self.wxq.find_element_by_css_selector(
            '.form-control').send_keys('10')
        time.sleep(1)

        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div/button').click()
        time.sleep(3)

    # 批量删除防伪码，全部删除
    def plsc_13(self):
        a = self.wxq.find_element_by_css_selector(
            'div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > label:nth-child(1)')
        self.wxq.execute_script('return arguments[0].scrollIntoView();', a)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div/button').click()

