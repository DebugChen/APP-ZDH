# coding=utf-8
import time
import unittest
import os
from BeautifulReport import BeautifulReport
from appium import webdriver


class MyTestCase_Xl_User_Login(unittest.TestCase):

    # # 自定义截图方法
    # def save_img(self, img_name):
    #     """
    #     传入一个img_name, 并存储到默认的文件路径下
    #     :param img_name:
    #     :return:
    #    """
    #     # os.path.abspath(r"E:\APPZDH\Xl_Istall_App_Zdh\img")截图存放路径
    #     self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
    #         r"E:\APPZDH\Xl_Istall_App_Zdh\img"), img_name))

    @classmethod
    def setUpClass(cls):
        print("开始测试")

    @classmethod
    def tearDownClass(cls):
        print("结束测试")

    # # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    # @BeautifulReport.add_test_img('test_Xl_Intall_Login')
    def test_Xl_User_Login(self):
        '''星联用户版登陆测试用例 '''
        desired_caps = {}
        # 为字典增加键值对
        desired_caps["platformName"] = 'Android'
        desired_caps["platformVersion"] = '8.0.0'
        desired_caps["deviceName"] = 'V3HBB18727512494'
        # 增加配置====>一旦启动时  会自动安装 该app文件
        # 自动化安装星联安装版app
        # desired_caps["app"]='E:\starlink_install_v4.2.7_2020-08-26-16-15-19.apk'
        # 使用aapt工具得到
        desired_caps["appPackage"] = 'org.xc.peoplelive'
        desired_caps["appActivity"] = 'org.xc.peoplelive.activity.StartActivity'
        # 注意在界面元素处理中文输入 =====一定要加入这两句
        desired_caps['unicodeKeyboard'] = "True"  # 中文支持unicode字符
        desired_caps['resetKeyboard'] = "True"  # 隐藏键盘
        # app---被测试项目每次都是以全新方式打开
        desired_caps["noReset"] = "False"
        self.dr = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 对查找元素 -----进行隐式等待工作
        # implicitly_wait(5)  ====>寻找页面元素时 最多找5秒 超过5秒 未找到报错
        self.dr.implicitly_wait(2)

        # #开始登陆
        # 判断是否有欢迎提示
        try:
            skipBtn = self.dr.find_element_by_id('org.xc.peoplelive:id/btnJump')
        except:
            print("无点击跳过欢迎按钮")
        else:
            skipBtn.click()

        # 点击获取位置权限
        self.dr.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()
        # 点击获取相机权限
        self.dr.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()
        # 点击获取存储权限
        self.dr.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()
        # 输入账户
        self.dr.find_element_by_xpath('//android.widget.EditText[@text="请输入手机号"]').send_keys('13200000000')
        # 输入密码
        self.dr.find_element_by_id('org.xc.peoplelive:id/etCode').send_keys('123456')
        # 点击屏幕键盘的搜索键，收起输入法
        # dr.press_keycode(66)
        # 点击登录
        self.dr.find_element_by_id('org.xc.peoplelive:id/btnLogin').click()
        # 等待登录完成
        time.sleep(3)

        # 根据 个人---元素是否存在---判断是否登录成功
        try:
            self.dr.find_element_by_id('org.xc.peoplelive:id/smallLabel')
        except:
            print("登录失败")
        else:
            print("登录成功")

    def test_Xl_User_BJLB(self):
        self.dr.find_element_by_id('org.xc.peoplelive:id/ibNotify').click()



if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_Xl_User_Login('test_Xl_User_Login'))
    testunit.addTest(MyTestCase_Xl_User_Login('test_Xl_User_BJLB'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='星联APP用户版-自动化测试报告',
                  description='星联APP用户版-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
