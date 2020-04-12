from woniuboss2.lib.student import Student
from woniuboss2.tools.utility import Utility
import unittest
from parameterized import parameterized

data_config_info=Utility.get_json('..\\config\\testdata.conf')
test_queryStudentInfo_info=Utility.get_excel_to_tuple(data_config_info[1])
test_selectInfo_info=Utility.get_excel_to_tuple(data_config_info[2])
test_saveNewInfo_info=Utility.get_excel_to_tuple(data_config_info[3])
test_saveLeave_info=Utility.get_excel_to_tuple(data_config_info[4])
test_saveModLeave_info=Utility.get_excel_to_tuple(data_config_info[5])
test_terminateLeave_info=Utility.get_excel_to_tuple(data_config_info[6])
test_queryLeave_info=Utility.get_excel_to_tuple(data_config_info[7])
test_saveUpLeave_info=Utility.get_excel_to_tuple(data_config_info[8])
test_quertAtteResult_info=Utility.get_excel_to_tuple(data_config_info[9])
# test_queryPhaseExam_info=Utility.get_excel_to_tuple(data_config_info[10])
test_saveScore_info=Utility.get_excel_to_tuple(data_config_info[11])
test_updateRepeat_info=Utility.get_excel_to_tuple(data_config_info[12])
test_showPhaseExam_info=Utility.get_excel_to_tuple(data_config_info[13])
test_queryStuOfClass_info=Utility.get_excel_to_tuple(data_config_info[14])
test_allocate_info=Utility.get_excel_to_tuple(data_config_info[15])
# test_saveCourse_info=Utility.get_excel_to_tuple(data_config_info[16])
test_saveModifyCourse_info=Utility.get_excel_to_tuple(data_config_info[17])
class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student=Student()
        print('test start')

    def tearDown(self) -> None:
        print('test end')
    #基本信息-查询
    @parameterized.expand(test_queryStudentInfo_info)
    def test_queryStudentInfo(self,queryStudentInfo_url,post,queryStudentInfo_data,status_code,content):
        queryStudentInfo_resp=self.student.queryStudentInfo(queryStudentInfo_url,queryStudentInfo_data)
        sql_all = 'select count(student_id) from student'
        all_student_number = Utility.query_one('..\\config\\base.conf', sql_all)[0]
        sql_part = 'select count(student_id) from student where student_class_id=59'
        part_student_number = Utility.query_one('..\\config\\base.conf', sql_part)[0]
        if queryStudentInfo_resp.json()['totalRow']== 0:
            actual = 'query zero'
        elif queryStudentInfo_resp.json()['totalRow'] == 1:
            actual = 'query one'
        elif queryStudentInfo_resp.json()['totalRow'] == all_student_number:
            actual = 'query all'
        elif queryStudentInfo_resp.json()['totalRow'] == part_student_number:
            actual = 'query part'
        else:
            actual = 'query error'

        self.assertEqual(actual,content)
    #基本信息-查看
    @parameterized.expand(test_selectInfo_info)
    def test_selectInfo(self,select_url,post,select_data,status_code,content):
        select_resp=self.student.selectInfo(select_url,select_data)
        actual=select_resp.text
        #断言
        self.assertEqual(actual,content)

    #基本信息-修改
    @parameterized.expand(test_saveNewInfo_info)
    def test_saveNewInfo(self,save_url,post,save_data,status_code,content):
        save_resp=self.student.saveNewInfo(save_url,save_data)
        actual=save_resp.text
        #断言
        self.assertEqual(actual,content)

    #学员请假-新增请假
    @parameterized.expand(test_saveLeave_info)
    def test_saveLeave(self,leave_url,post,leave_data,status_code,content):
        leave_resp=self.student.saveLeave(leave_url,leave_data)
        actual=leave_resp.text
        #断言
        self.assertEqual(actual,content)

    #学员请假-修改请假
    @parameterized.expand(test_saveModLeave_info)
    def test_saveModLeave(self,mod_url,post,mod_data,status_code,content):
        mod_resp=self.student.saveModLeave(mod_url,mod_data)
        actual=mod_resp.text
        #断言
        self.assertEqual(actual,content)

    #学员请假-销假
    @parameterized.expand(test_terminateLeave_info)
    def test_terminateLeave(self,terminate_url,post,terminate_data,status_code,content):
        terminate_resp=self.student.terminateLeave(terminate_url,terminate_data)
        actual=terminate_resp.text
        #断言
        self.assertEqual(actual,content)

    #学员请假-查询
    @parameterized.expand(test_queryLeave_info)
    def test_queryLeave(self,queryLeave_url,post,queryLeave_data,status_code,content):
        queryLeave_resp=self.student.queryLeave(queryLeave_url,queryLeave_data)
        actual=queryLeave_resp.text
        #断言
        self.assertEqual(actual,content)

    #学员请假-假条
    @parameterized.expand(test_saveUpLeave_info)
    def test_saveUpLeave(self,saveUpLeave_url,post,saveUpLeave_data,status_code,content):
        saveUpLeave_resp = self.student.saveUpLeave(saveUpLeave_url, saveUpLeave_data)
        actual = saveUpLeave_resp.text
        # 断言
        self.assertEqual(actual, content)

    #晨考记录-查询
    @parameterized.expand(test_quertAtteResult_info)
    def test_quertAtteResult(self,quertAtteResult_url,post,quertAtteResult_data,status_code,content):
        quertAtteResult_resp = self.student.saveUpLeave(quertAtteResult_url,quertAtteResult_data)
        actual = quertAtteResult_resp.text
        # 断言
        self.assertEqual(actual, content)

    # #阶段测评-查询
    # @parameterized.expand(test_queryPhaseExam_info)
    # def test_queryPhaseExam(self,queryPhaseExam_url,post,queryPhaseExam_data,status_code,content):
    #     queryPhaseExam_resp = self.student.queryPhaseExam(queryPhaseExam_url, queryPhaseExam_data)
    #     actual = queryPhaseExam_resp.text
    #     # 断言
    #     self.assertEqual(actual, content)

    #阶段测评-测评
    @parameterized.expand(test_saveScore_info)
    def test_saveScore(self,saveScore_url,post,saveScore_data,status_code,content):
        saveScore_resp = self.student.saveScore(saveScore_url, saveScore_data)
        actual = saveScore_resp.text
        # 断言
        self.assertEqual(actual, content)

    # 阶段测评-降级
    @parameterized.expand(test_updateRepeat_info)
    def test_updateRepeat(self,updateRepeat_url,post,updateRepeat_data,status_code,content):
        updateRepeat_resp = self.student.updateRepeat(updateRepeat_url,updateRepeat_data)
        actual = updateRepeat_resp.text
        # 断言
        self.assertEqual(actual, content)

    #测评记录-查询
    @parameterized.expand(test_showPhaseExam_info)
    def test_showPhaseExam(self,showPhaseExam_url,post,showPhaseExam_data,status_code,content):
        showPhaseExam_resp = self.student.showPhaseExam(showPhaseExam_url, showPhaseExam_data)
        actual = showPhaseExam_resp.text
        # 断言
        self.assertEqual(actual, content)

    #班级管理-查询
    @parameterized.expand(test_queryStuOfClass_info)
    def test_queryStuOfClass(self,queryStuOfClass_url,post,queryStuOfClass_data,status_code,content):
        queryStuOfClass_resp = self.student.queryStuOfClass(queryStuOfClass_url, queryStuOfClass_data)
        actual = queryStuOfClass_resp.text
        # 断言
        self.assertEqual(actual, content)

    #班级管理-确认分班
    @parameterized.expand(test_allocate_info)
    def test_allocate(self, allocate_url, post, allocate_data, status_code, content):
        allocate_resp = self.student.allocate(allocate_url,allocate_data)
        actual = allocate_resp.text
        # 断言
        self.assertEqual(actual, content)

    # #课程安排-新增排课
    # @parameterized.expand(test_saveCourse_info)
    # def test_saveCourse(self,saveCourse_url,post,saveCourse_data,status_code, content):
    #     saveCourse_resp=self.student.saveCourse(saveCourse_url,saveCourse_data)
    #     actual=saveCourse_resp.text
    #     #断言
    #     self.assertEqual(actual,content)

    #课程安排-修改
    @parameterized.expand(test_saveModifyCourse_info)
    def test_saveModifyCourse(self,saveModifyCourse_url,post,saveModifyCourse_data,status_code, content):
        saveModifyCourse_resp=self.student.saveModifyCourse(saveModifyCourse_url,saveModifyCourse_data)
        actual=saveModifyCourse_resp.text
        #断言
        self.assertEqual(actual,content)




if __name__ == '__main__':
    unittest.main(verbosity=2)
