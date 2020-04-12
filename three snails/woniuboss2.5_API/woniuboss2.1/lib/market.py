from woniuboss2.tools.service import Service

class Market:

    def __init__(self):
        self.session = Service.get_session()

    # 新增资源
    def addCus(self, addCus_url, addCus_data):
        return self.session.post(addCus_url, addCus_data)

    # 上传专属
    def validateUpload(self, validateUpload_url, validateUpload_data):
        return self.session.post(validateUpload_url, validateUpload_data)

    # 查询资源
    def qureyNetCus(self, qureyNetCus_url, qureyNetCus_data):
        return self.session.post(qureyNetCus_url, qureyNetCus_data)
