#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss2.tools.service import Service


class EtprsManage:
    def __init__(self):
        self.session = Service.get_session()

    # 新增企业
    def add_company(self,add_company_url, add_company_data,):
        return self.session.post(add_company_url,add_company_data,)
    # 查询企业
    def query_etprs(self, query_etprs_url, query_etprs_data):
        return self.session.post(query_etprs_url, query_etprs_data)



