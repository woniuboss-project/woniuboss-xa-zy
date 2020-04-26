#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#综合成绩
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
import time

class Finally_test:


    # 进入综合成绩页面
    def open_finally(self,driver):
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div[2]/div/ul/li[5]/a").click()
        time.sleep(2)

    # 区域 下拉选择框
    def choice_region(self,driver,value):
        # random_index = random.randint(0,6)
        cr = Select(driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/select[1]"))
        cr.select_by_index(value)

    # 方向 下拉选择框
    def choice_orientation(self,driver,value):
        # random_index = random.randint(0,4)
        co = Select(driver.find_element_by_css_selector("select.sel-text:nth-child(1)"))
        co.select_by_visible_text(value)

    # 班级 下拉选择框
    def choice_class(self,driver,value):
        # random_index = random.randint(0,7)
        cc = Select(driver.find_element_by_css_selector(".col-lg-12 > select:nth-child(2)"))
        cc.select_by_visible_text(value)

    # 阶段 下拉选择框
    def choice_phase(self,driver,value):
        # random_index = random.randint(0,5)
        cp = Select(driver.find_element_by_css_selector("select.sel-text:nth-child(4)"))
        cp.select_by_visible_text(value)

    # 点击查询按钮
    def click_query(self,driver):
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/button").click()




