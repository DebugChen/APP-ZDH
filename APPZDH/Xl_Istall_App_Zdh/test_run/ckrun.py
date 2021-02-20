# coding=utf-8
import sys
import time
from test_run.BSTestRunner import BSTestRunner
import unittest

# 指定项目路径
path='E:\APPZDH\Xl_Istall_App_Zdh'
sys.path.append(path)
# 指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../reports'
# 匹配测试多条用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

# if __name__=='__main__':
#     # 组装测试套件
#     testunit=unittest.TestSuite()
#     # 添加测试用例
#     testunit.addTest(test_case.test_login.Testlogin('test_login_1'))
#     # testunit.addTest(test_case.test_Hd.TestHd('test_Hd'))

# runner = BeautifulReport(testunit)
# runner.report(filename='星联APP用户版-自动化测试报告8',
#                   description='星联APP用户版-测试用例执行情况',
#                   report_dir='report',
#                   theme='theme_default')

# 定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' test_report.html'
# 运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="星联APP安装版-自动化测试报告", description="星联APP安装版-测试用例执行情况")
    runner.run(discover)