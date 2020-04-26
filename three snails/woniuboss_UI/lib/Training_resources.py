#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import time
from selenium.webdriver.support.select import Select
from woniuboss_UI.tools.utility import Utility
from woniuboss_UI.tools.service import Service
from woniuboss_UI.lib.login import Login

class Training_Resources:
    def __init__(self, driver):
        self.driver = driver
    #培训资源
    def tranin(self,driver):
    #点击资源管理，进入资源管理界面
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[4]/div[1]/a').click()
    #点击资源管理内的培训资源
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[4]/div[2]/div/ul/li[1]/a').click()

    # 进行解密
    def click_psd(self,driver,passwd):
        self.driver.find_element_by_id('btn-decrypt').click()
        sepass = self.driver.find_element_by_name('secondPass')
        Service.send_input(sepass, passwd)
        time.sleep(5)
        self.driver.find_elements_by_class_name('btn.btn-info')[0].click()
    #选择资源库的下拉框
    def resource_store(self,driver,value):
        Resource_bank= driver.find_element_by_id('poolSelect')
        selects = Select(Resource_bank)
        selects.select_by_visible_text(value)
    #选择状态的下拉框
    def select_status(self,driver,value):
        state = driver.find_element_by_id('empNameSelect')
        select = Select(state)
        select.select_by_visible_text(value)

    #选择来源下拉框
    def select_source(self,driver,value):
        source = driver.find_element_by_id('sourceSelect')
        select = Select(source)
        select.select_by_visible_text(value)

    # 选择区域下拉框
    def select_region(self,driver,value):
        area = driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(1)')
        select = Select(area)
        select.select_by_visible_text(value)
    def select_department(self,driver,value):
        # #选择部门下拉框
        department = driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(2)')
        select = Select(department)
        select.select_by_visible_text(value)
    def select_consultant(self,driver,value):
        # #选择咨询师下拉框
        counselor = driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(3)')
        select = Select(counselor)
        select.select_by_visible_text(value)
    def select_begin(self,driver,value):
        # #选择开始时间
        begin_time = driver.find_element_by_id('date1')
        begin_time.click()
        begin_time.clear()
        begin_time.send_keys(value)
    def select_end(self,driver,value):
        # #选择结束时间
        end_time = driver.find_element_by_id('date2')
        end_time.click()
        end_time.clear()
        end_time.send_keys(value)
    def select_name(self,driver,value):
        # #选择姓名输入框
        input_name = driver.find_element_by_css_selector('div.col-lg-12:nth-child(1) > input:nth-child(6)')
        input_name.click()
        input_name.clear()
        input_name.send_keys(value)
    def select_search(self,driver):
        # #点击搜索按钮
        seek = driver.find_element_by_css_selector('button.btn:nth-child(7)')
        seek.click()
    #新增按钮
    def new_button(self,driver,value):
        driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()
        driver.find_element_by_css_selector('div.has-feedback:nth-child(2) > input:nth-child(2)').send_keys(value)
        driver.find_element_by_css_selector('#addCus > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)').send_keys(value)
    def select_new_status(self,driver,value):
        #选择最新状态下拉框
        status = driver.find_element_by_css_selector('#addCus > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > select:nth-child(2)')
        selectss = Select(status)
        selectss.select_by_visible_text(value)
    def select_channel(self,driver,value):
        #选择渠道来源下拉框
        ditch = driver.find_element_by_css_selector('#addCus > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > select:nth-child(2)')
        selectsss = Select(ditch)
        selectsss.select_by_visible_text(value)
    def select_save(self,driver):
        # 点击保存
        driver.find_element_by_css_selector('#addCusBtn').click()
        #点击弹窗确定
        driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()
    #点击废弃
    def out_student_msg(self,driver):
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_css_selector('th.bs-checkbox > div:nth-child(1) > input:nth-child(1)').click()
        driver.find_element_by_css_selector('#abandon').click()
        driver.find_element_by_css_selector('button.btn-primary:nth-child(2)').click()
    #data = {'资源库':'临时池'}
    #data = {'资源库':'临时池','状态':'新认领'}
    #对excle中获取的用例进行选择方法
    def all_opration(self,driver,data):
        options = {'资源库': self.resource_store,'状态': self.select_status,'区域':self.select_region,'来源':self.select_source,
                   '部门':self.select_department,'咨询师':self.select_consultant,'开始时间':self.select_begin,
                   '结束时间':self.select_end,'姓名':self.select_name,'最新状态':self.select_new_status,'渠道':self.select_channel
                   }
        #excel内容的键值
        test_data_key = data.keys()
        #options的键值
        key_list = options.keys()
        #进行循环，判断键值是否对应
        for i in test_data_key :
            if i in key_list :
                #如果对应，传参，并且执行键所对应的值
                options[i](driver,data[i])

# if __name__ == '__main__':
#     Training_Resources.tranin()





