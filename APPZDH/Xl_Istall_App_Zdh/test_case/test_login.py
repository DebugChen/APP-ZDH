# coding=utf-8
import unittest
import warnings
from business.login_business import XL_Install_login
from data.cktestdata import get_csv_data


class Testlogin(unittest.TestCase):
    # 指定csv数据 文件所在的位置
    csv_file=r'E:\APPZDH\Xl_Istall_App_Zdh\data\ckaccount.csv'

    # # 截图方法
    # def save_img(self, img_name):
    #     """
    #         传入一个img_name, 并存储到默认的文件路径下
    #     :param img_name:
    #     :return:
    #    """
    #     # os.path.abspath(r"G:\Test_Project\img")截图存放路径
    #     self.dr.get_screenshot_as_file(
    #         '{}/{}.png'.format(os.path.abspath(r"E:\APPZDH\ckappiumframework\img"), img_name))

    #定义setup函数===》1条用例运行之前
    @classmethod
    def setUpClass(cls):
        print("开始测试")
        # 删除输出不需要的警告
        # 这句话的作用是用来忽略 ResourceWaring 异常警告的
        warnings.simplefilter("ignore", ResourceWarning)

    @classmethod
    # 1条用例运行之后
    def tearDownClass(cls):
        print("结束测试")

    # # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    # @BeautifulReport.add_test_img('test_login_1')
    # 组织1条用例函数运行---test开头
    def test_login_1(self):
        '''星联APP用户版-登录测试用例'''
        print("第一条用例测试~")
        # 得到csv文件数据的第一行=====》预期登录成功的
        data = get_csv_data(self.csv_file, 1)
        # 预期失败用例
        #data[0]代表第一行数据的第一个
        #data[1] 代表第一行数据的第二个
        # .assertTrue 断言  XL_login 如果函数结果为true 代表运行成功
        self.assertTrue(XL_Install_login(data[0], data[1]))

    # def test_login_2(self):
    #     print("第二条用例测试~")
    #     data = get_csv_data(self.csv_file, 2)
    #     # 预期失败用例
    #     # .assertFalse 断言  jw_login 如果函数结果为False 代表运行成功
    #     self.assertFalse(XL_login(data[0], data[1]))
    #
    # def test_login_3(self):
    #     print("第三条用例测试~")
    #     data = get_csv_data(self.csv_file, 3)
    #     # 预期失败用例
    #     # .assertFalse 断言  jw_login 如果函数结果为False 代表运行成功
    #     self.assertFalse(XL_login(data[0], data[1]))
