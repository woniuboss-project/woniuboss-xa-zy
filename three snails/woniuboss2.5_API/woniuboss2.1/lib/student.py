from woniuboss2.tools.service import Service

class Student:

    def __init__(self):
        self.session=Service.get_session()

    def queryStudentInfo(self,queryStudentInfo_url,queryStudentInfo_data):
        return self.session.post(queryStudentInfo_url, queryStudentInfo_data)

    def selectInfo(self,select_url,select_data):
        return self.session.post(select_url,select_data)

    def saveNewInfo(self,save_url,save_data):
        return self.session.post(save_url,save_data)

    def saveLeave(self,leave_url,leave_data):
        return self.session.post(leave_url,leave_data)

    def saveModLeave(self,mod_url,mod_data):
        return self.session.post(mod_url,mod_data)

    def terminateLeave(self,terminate_url,terminate_data):
        return self.session.post(terminate_url,terminate_data)

    def queryLeave(self,queryLeave_url,queryLeave_data):
        return self.session.post(queryLeave_url,queryLeave_data)

    def saveUpLeave(self,saveUpLeave_url,saveUpLeave_data):
        return self.session.post(saveUpLeave_url,saveUpLeave_data)

    def quertAtteResult(self,quertAtteResult_url,quertAtteResult_data):
        return self.session.post(quertAtteResult_url,quertAtteResult_data)

    def queryPhaseExam(self,queryPhaseExam_url,queryPhaseExam_data):
        return self.session.post(queryPhaseExam_url,queryPhaseExam_data)

    def saveScore(self,saveScore_url,saveScore_data):
        return self.session.post(saveScore_url,saveScore_data)

    def updateRepeat(self,updateRepeat_url,updateRepeat_data):
        return self.session.post(updateRepeat_url,updateRepeat_data)

    def showPhaseExam(self,showPhaseExam_url,showPhaseExam_data):
        return self.session.post(showPhaseExam_url,showPhaseExam_data)

    def queryStuOfClass(self,queryStuOfClass_url,queryStuOfClass_data):
        return self.session.post(queryStuOfClass_url,queryStuOfClass_data)

    def allocate(self,allocate_url,allocate_data):
        return self.session.post(allocate_url,allocate_data)

    def saveCourse(self,saveCourse_url,saveCourse_data):
        return self.session.post(saveCourse_url,saveCourse_data)

    def saveModifyCourse(self,saveModifyCourse_url,saveModifyCourse_data):
        return self.session.post(saveModifyCourse_url,saveModifyCourse_data)