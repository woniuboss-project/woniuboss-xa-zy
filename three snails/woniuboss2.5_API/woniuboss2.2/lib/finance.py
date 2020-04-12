#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss2.tools.service import Service

class Finance:
    def __init__(self):
        self.session = Service.get_session()

    #新增流水
    def addFinancial(self,addFinancial_url,addFinancial_data):
        return self.session.post(addFinancial_url,addFinancial_data)

    #学员缴费
    def payment(self,payment_url,payment_data):
        return self.session.post(payment_url,payment_data)

    #上月查询
    def Query_lastmonth(self,Query_lastmonth_url,Query_lastmonth_data):
        return self.session.post(Query_lastmonth_url,Query_lastmonth_data)

    #本月查询
    def Query_thismonth(self,Query_thismonth_url,Query_thismonth_data):
        return self.session.post(Query_thismonth_url,Query_thismonth_data)