from selenium import webdriver
import time
class dl():
    def __init__(self):
        self.wxq = webdriver.Firefox()
        self.wxq.get(r"http://123.57.140.190/manage/")
        time.sleep(2)
        # self.wxq.implicitly_wait(5)
        self.wxq.find_element_by_css_selector('input.form-control:nth-child(1)').send_keys("admin")
        self.wxq.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys("admin999")
        self.wxq.find_element_by_css_selector('.btn').click()
        self.wxq.maximize_window()
        time.sleep(2)
        try:
            a = self.wxq.find_element_by_css_selector(
                '#top_menu > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
            if a == '前台浏览':
                print(a, '登录模块测试成功')
            else:
                print("登录模块测试有误")

        except Exception as e:
              print(e)

