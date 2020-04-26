#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author:
# CreatDate:
# Version:
# ====#====#====#====
# 阶段考评
import os
from time import sleep
from woniuboss_UI.tools.service import Service


class Month_test:
    # 选择区域
    def select_area(self, driver, value):
        area = driver.find_element_by_css_selector('select.sel-text:nth-child(1)')
        Service.select_value(area, value)

    # 选择班级
    def select_class(self, driver, value):
        cclass = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/select[2]')
        Service.select_value(cclass, value)

    # 输入姓名
    def input_name(self, driver, value):
        name = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/input')
        Service.input_ele(name, value)

    # 点击查询按钮
    def query(self, driver):
        query_button = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/button')

    # 查看模板
    def check_from(self, driver):
        menu = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/div/button[1]')
        menu.click()

    # 阶段导入按钮
    def phase(self, driver):
        phase = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[1]/div/button[2]')
        phase.click()
        # 选择班级

    def upload_class(self, driver, value):
        class1 = driver.find_element_by_xpath('//*[@id="import_cl"]')
        Service.select_value(class1, value)
        # 选择阶段

    def upload_stage(self, driver, value):
        stage1 = driver.find_element_by_xpath('//*[@id="import_ph"]')
        Service.select_value(stage1, value)
        # 上传文件

    def upload_file(self, driver, value):
        file = driver.find_element_by_xpath('//*[@id="files"]')
        filepath = os.path.join(os.getcwd(), 'stage_grade.xlsx')
        file.send_keys(filepath)

    # 阶段导入提交按钮
    def commit_button(self, driver):
        commit = driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/button')
        commit.click()

    # 数据导出
    def date_export(self, driver):
        data = driver.find_element_by_id('btn_download')

    # 上传返回的确定按钮
    def upload_resp_button(self, driver):
        driver.find_element_by_css_selector(
            ".bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()

    # 上传返回的确定文本
    def upload_resp(self, driver):
        upload_resp = driver.find_element_by_css_selector(".bootbox-body").text
        return upload_resp

    # 阶段考评记录录入
    def entering(self, driver):
        type_in = driver.find_element_by_css_selector('#pe-result > tbody:nth-child(2) > tr:nth-child(3) > '
                                                      'td:nth-child(9) > button:nth-child(1)')
        type_in.click()

    # 录入班级
    def select_class2(self, driver, value):
        class2 = driver.find_element_by_id('ph_cl')
        Service.select_value(class2, value)

    # 录入成绩
    def input_grade(self, driver, value):
        grade = driver.find_element_by_css_selector(
            '#phaseExam-form > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        grade.click()
        grade.clear()
        grade.send_keys(grade, value)

    # 录入阶段
    def select_stage(self, driver, value):
        stage2 = driver.find_element_by_xpath('//*[@id="ph_phase"]')
        Service.select_value(stage2, value)

    # 录入评语
    def input_comment(self, driver, value):
        comment = driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/form/div[3]/div[3]/textarea')
        comment.click()
        comment.clear()
        comment.send_keys(comment, value)

    # 点击保存
    def save_button(self, driver):
        save = driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button')
        save.click()

    # +按钮
    def add(self, driver):
        add = driver.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/a/i')
        add.click()

    # 修改阶段成绩
    def edit_grade(self, driver, value):
        edit_grade = driver.find_element_by_css_selector(
            '#phaseExam-form > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        Service.input_ele(edit_grade, value)

    # 修改阶段成绩保存按钮
    def edit_save_grade(self, driver):
        edit_save_grade = driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button')
        edit_save_grade.click()

    # 数据导出按钮

    def data_export_button(self, driver):
        driver.find_element_by_id("btn_download").click()

    # 阶段考评查询整合
    def stage_grade_query(self, driver, stage_query_data):
        self.select_area(driver, stage_query_data[0])
        sleep(2)
        self.select_class(driver, stage_query_data[1])
        sleep(2)
        self.input_name(driver, stage_query_data[2])
        sleep(2)
        self.query(driver)

    # 阶段考评录入
    def stage_grade_upload(self, driver, stage_upload_data):
        self.phase(driver)
        self.upload_class(driver, stage_upload_data[0])
        sleep(2)
        self.upload_stage(driver, stage_upload_data[1])
        sleep(2)
        self.upload_file(driver, stage_upload_data[2])
        self.commit_button(driver)







