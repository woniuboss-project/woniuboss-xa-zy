#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss2.tools.service import Service

class Employment:
    def __init__(self):
        self.session = Service.get_session()

    #技术面试
    def Interview(self,Interview_url,Interview_data):
        return self.session.post(Interview_url,Interview_data)

    #就业管理
    def obtainEmployment(self,obtainEmployment_url,obtainEmployment_data):
        return self.session.post(obtainEmployment_url,obtainEmployment_data)

