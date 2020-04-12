# 报表中心接口测试
from woniuboss2.tools.service import Service

class Report:

    def __init__(self):
        self.session = Service.get_session()

    # 咨询部
    def console(self, console_url, console_data):
        return self.session.post(console_url, console_data)

    # 电销部
    def sale(self, sale_url, sale_data):
        return self.session.post(sale_url, sale_data)

    # 市场部
    def mark(self, mark_url, mark_data):
        return self.session.post(mark_url, mark_data)

    # 就业部
    def job(self, job_url, job_data):
        return self.session.post(job_url, job_data)