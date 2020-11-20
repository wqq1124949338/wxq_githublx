from public.login import *
from selenium.webdriver.support.select import Select
class cpgl(dl):

    # 新增流程类别的正反用例 ddt导入数据
    def addlb_01(self,a,b):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('新增流程类别').click()
        self.wxq.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys(a)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys(b)
        self.wxq.find_element_by_css_selector(
            'html body.has-js section#container section#main-content section.wrapper div.row div.col-lg-12 section.panel div.panel-body form.form-horizontal.tasi-form div.form-group div.col-lg-offset-2.col-lg-10 button.btn.btn-danger').click()
        time.sleep(2)

    # 新增流程类别，其中流程状态为
    def addlb_02(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(2)
        self.wxq.find_element_by_link_text('新增流程类别').click()
        self.wxq.find_element_by_css_selector('.col-sm-4 > input:nth-child(1)').send_keys('加工处理')
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('122315')
        x=self.wxq.find_element_by_name('zt')
        Select(x).select_by_visible_text('禁用')
        self.wxq.find_element_by_css_selector(
            'html body.has-js section#container section#main-content section.wrapper div.row div.col-lg-12 section.panel div.panel-body form.form-horizontal.tasi-form div.form-group div.col-lg-offset-2.col-lg-10 button.btn.btn-danger').click()
        time.sleep(4)

    # 流程分类管理模块的编辑功能测试
    def addlb_03(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('流程类别管理').click()
        self.wxq.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(23) > td:nth-child(7) > a:nth-child(1)').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('7563324')
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        time.sleep(3)

    #     流程类别模块的批量删除功能测试
    def addlb_04(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('流程类别管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('//*[@id="chkAll"]').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('//*[@id="del"]').click()
        time.sleep(2)
        self.wxq.switch_to.alert.accept()

    # 流程类别管理模块单条删除流程类别名称测试
    def addlb_05(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('流程类别管理').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > span:nth-child(2)').click()
        time.sleep(2)
        self.wxq.find_element_by_css_selector('.layui-layer-btn0').click()
        time.sleep(2)

    #   流程类别管理模块搜索功能测试
    def addlb_06(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('流程类别管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div/input').send_keys('取消')
        time.sleep(1)
        self.wxq.find_element_by_css_selector('button.btn:nth-child(2)').click()
        time.sleep(2)

    # 流程类别管理模块刷新功能测试
    def addlb_07(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('流程类别管理').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.btn-default').click()
        time.sleep(3)

    # 录入流程记录模块的正常输入值
    def addlb_08(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('录入流程记录').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/textarea').send_keys('12347856')
        self.wxq.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('无记录')
        self.wxq.find_element_by_css_selector('.btn').click()


    # 录入流程记录模块的输入时选择不同的流程类别下拉框中的值
    def addlb_09(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('录入流程记录').click()
        time.sleep(1)
        # 下拉框处理方法一
        # self.wxq.execute_script('document.getElementById("s001").style.display="block";')
        # Select(self.wxq.find_element_by_id('s001')).select_by_visible_text('搞活动他不会让他')
        # time.sleep(3)
        # 下拉框处理处理方法二
        self.wxq.find_element_by_css_selector('.searchable-select-caret').click()
        self.wxq.find_element_by_css_selector('div.searchable-select-item:nth-child(4)').click()
        time.sleep(3)
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/textarea').send_keys('12347856')
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('无记录')
        time.sleep(4)
        self.wxq.find_element_by_css_selector('.btn').click()

    #  录入流程记录模块的责任人或工号默认字段的修改
    def addlb_10(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('录入流程记录').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/textarea').send_keys(
            '465461321')
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('无记录')
        self.wxq.find_element_by_css_selector('div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)').clear()
        self.wxq.find_element_by_css_selector(
            'div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)').send_keys('我的滑板鞋')
        self.wxq.find_element_by_css_selector('.btn').click()

    # 录入流程记录模块的操作时间反案例
    def addlb_11(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_link_text('录入流程记录').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/textarea').send_keys(
            '465461321')
        self.wxq.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('无记录')
        self.wxq.find_element_by_css_selector(
            '#czdate').clear()
        self.wxq.find_element_by_css_selector(
            '#czdate').send_keys('0112314564')
        self.wxq.find_element_by_css_selector('.btn').click()
        time.sleep(3)

    # 流程记录管理模块的刷新功能
    def addlb_12(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.btn-default').click()
        time.sleep(1)

    # 子级流程记录管理模块的编辑功能测试
    def addlb_13(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)').click()
        self.wxq.find_element_by_css_selector('div.col-sm-6:nth-child(2) > input:nth-child(1)').send_keys('无说明')
        self.wxq.find_element_by_css_selector('.btn').click()
        time.sleep(0.5)
        # 断言时无法定位元素
        a=self.wxq.find_element_by_css_selector('[class="layui-layer-ico layui-layer-ico1"]')
        return a

    # 子级流程记录管理模块的单个删除功能测试
    def addlb_14(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > span:nth-child(2)').click()
        self.wxq.find_element_by_css_selector('.layui-layer-btn0').click()
        a=self.wxq.find_element_by_css_selector('.layui-layer-content').text
        return a

    # 子级流程记录管理模块的批量删除功能测试
    def addlb_15(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('#chkAll').click()
        self.wxq.find_element_by_css_selector('#del').click()
        time.sleep(1)
        self.wxq.switch_to.alert.accept()

    # 子级流程记录管理模块的搜索功能测试
    def addlb_16(self):
        self.wxq.find_element_by_link_text('流程记录管理').click()
        time.sleep(1)
        self.wxq.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        time.sleep(1)
        self.wxq.find_element_by_css_selector('input.form-control').send_keys('4562')
        self.wxq.find_element_by_css_selector('.btn-success').click()
        time.sleep(3)

