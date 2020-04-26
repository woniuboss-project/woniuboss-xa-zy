#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#学员信息
from selenium import webdriver
import random
from selenium.webdriver.support.select import Select
import time

class Student_msg:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.1.113:8080/WoniuBoss4.0/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector('div.row:nth-child(1) > input:nth-child(1)').send_keys("wncd000")
        self.driver.find_element_by_css_selector('div.row:nth-child(2) > input:nth-child(1)').send_keys("woniu123")
        self.driver.find_element_by_css_selector('.btn').click()
        self.driver.find_element_by_partial_link_text("学员信息").click()

    # 选择随机区域
    def select_area(self):
        driver = self.driver
        ele = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/select[1]")
        length = len(Select(ele).options)
        random_index = random.randint(0, length - 1)
        Select(ele).select_by_index(random_index)
    # 选择随机方向
    def select_direction(self):
        driver = self.driver
        ele = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/select[2]")
        length = len(Select(ele).options)
        random_index = random.randint(0, length - 1)
        Select(ele).select_by_index(random_index)
    # 选择随机状态
    def select_status(self):
        driver = self.driver
        ele = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/select[4]")
        length = len(Select(ele).options)
        random_index = random.randint(0, length - 1)
        Select(ele).select_by_index(random_index)

    def query_info(self,data):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/input").click()
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/input").clear()
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/input").send_keys(data[0])
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/button").click()


    def amend_info(self,data):
        # 随机选择区域
        # self.select_area()
        driver = self.driver
        # 点击搜索
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/button").click()
        # 随机选择修改
        a = random.randint(0,2)
        driver.find_element_by_xpath('//table[@id="stuInfo_table"]/tbody/tr[2]/td[12]/button[2]').click()
        phone1 = driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div[1]/div[1]/div[4]/input")
        phone1.click()
        phone1.clear()
        phone1.send_keys(data[a][0])
        qq1 = driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div[1]/div[1]/div[8]/input")
        qq1.click()
        qq1.clear()
        qq1.send_keys(data[a][1])

        school1 = driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div[3]/div[1]/input")
        school1.click()
        school1.clear()
        school1.send_keys(data[a][2])
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/button").click()
        driver.find_element_by_xpath("/html/body/div[12]/div/div/div[3]/button").click()






