# coding=utf-8
import time
import unittest
import os
from BeautifulReport import BeautifulReport
from appium import webdriver


class MyTestCase_Xl_Intall_Login(unittest.TestCase):

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
        print("开始测试")

    # # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    # @BeautifulReport.add_test_img('test_Xl_Intall_Login')
    def test_Xl_Intall_Login(self):
        '''星联安装流程测试方法 '''
        desired_caps = {}
        # 为字典增加键值对
        desired_caps["platformName"] = 'Android'
        desired_caps["platformVersion"] = '8.0.0'
        desired_caps["deviceName"] = 'V3HBB18727512494'
        # 增加配置====>一旦启动时  会自动安装 该app文件
        # 自动化安装星联安装版app
        # desired_caps["app"]='E:\starlink_install_v4.2.7_2020-08-26-16-15-19.apk'
        # 使用aapt工具得到
        desired_caps["appPackage"] = 'org.xc.starlinkother'
        desired_caps["appActivity"] = 'org.xc.starlinkother.activity.StartActivity'
        # 注意在界面元素处理中文输入 =====一定要加入这两句
        desired_caps['unicodeKeyboard'] = "True"  # 中文支持unicode字符
        desired_caps['resetKeyboard'] = "True"  # 隐藏键盘
        # app---被测试项目每次都是以全新方式打开
        desired_caps["noReset"] = "False"
        # 通过该字典json信息===》创造驱动==》驱动appium+手机上app的执行
        # 注意 导包时候必须使用导入 appium的 webdriver
        # from appium import webdriver
        # 参数1：appium一个远程(localhost)访问的地址
        # 参数2：desired_capabilities 信息
        dr = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 对查找元素 -----进行隐式等待工作
        # implicitly_wait(5)  ====>寻找页面元素时 最多找5秒 超过5秒 未找到报错
        dr.implicitly_wait(2)

        # #开始登陆
        # 判断是否有欢迎提示
        try:
            skipBtn = dr.find_element_by_id('org.xc.starlinkother:id/btnJump')
        except:
            print("无点击跳过欢迎按钮")
        else:
            skipBtn.click()

        # 点击获取位置权限
        dr.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()
        # 点击获取相机权限
        dr.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()
        # 点击获取存储权限
        dr.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()
        # 输入账户
        dr.find_element_by_id('org.xc.starlinkother:id/etTel').send_keys('陈凯')
        # 输入密码
        dr.find_element_by_id('org.xc.starlinkother:id/etCode').send_keys('douniu2918')
        # 点击屏幕键盘的搜索键，收起输入法
        # dr.press_keycode(66)
        # 点击登录
        dr.find_element_by_id('org.xc.starlinkother:id/btnLogin').click()
        # 等待登录完成
        time.sleep(3)

        # 根据 个人---元素是否存在---判断是否登录成功
        try:
            dr.find_element_by_id("org.xc.starlinkother:id/smallLabel")
        except: # 捕获异常----》 代表没有找到首页 这个标签
            print("登录失败，没有找到  个人---标签")
        else: # 找到的内容
            print("登录成功，找到  个人---标签")

        # 点击设备安装
        dr.find_element_by_xpath('//android.widget.TextView[@text="设备安装"]').click()
        time.sleep(2)
        # 点击添加设备
        dr.find_element_by_id('org.xc.starlinkother:id/img_right').click()
        # 输入IMEI号
        dr.find_element_by_id('org.xc.starlinkother:id/etImei').send_keys('861097040098216')
        # 输入姓名
        dr.find_element_by_id('org.xc.starlinkother:id/etName').send_keys('张三')
        # 输入身份证
        dr.find_element_by_id('org.xc.starlinkother:id/etIdCard').send_keys('420902199805026541')
        # 输入地址
        dr.find_element_by_id('org.xc.starlinkother:id/etAddr').send_keys('武汉市硚口区')
        # 输入车牌
        dr.find_element_by_id('org.xc.starlinkother:id/etCarTag').send_keys('鄂A6666')
        # 输入手机号
        dr.find_element_by_id('org.xc.starlinkother:id/etTel').send_keys('15545265354')
        time.sleep(2)
        # 点击上线状态
        dr.find_element_by_id('org.xc.starlinkother:id/btnOnline').click()
        time.sleep(1)
        # 点击提交
        dr.find_element_by_xpath('//*[@class="android.widget.Button"and@index="2"]').click()
        time.sleep(3)

        # 上传车牌照片
        dr.find_element_by_xpath('//*[@class="android.widget.ImageView"and@instance="1"]').click()
        time.sleep(2)
        dr.find_element_by_id('com.huawei.camera:id/shutter_button').click()
        time.sleep(2)
        dr.find_element_by_id('com.huawei.camera:id/done_button').click()
        time.sleep(2)

        # 上传设备安装位置照片
        dr.find_element_by_xpath('//*[@class="android.widget.ImageView"and@instance="4"]').click()
        time.sleep(2)
        dr.find_element_by_id('com.huawei.camera:id/shutter_button').click()
        time.sleep(2)
        dr.find_element_by_id('com.huawei.camera:id/done_button').click()
        time.sleep(2)

        # 上传车辆行驶证照片
        dr.find_element_by_xpath('//*[@class="android.widget.ImageView"and@instance="7"]').click()
        time.sleep(2)
        dr.find_element_by_id('com.huawei.camera:id/shutter_button').click()
        time.sleep(2)
        dr.find_element_by_id('com.huawei.camera:id/done_button').click()
        time.sleep(2)

        # 点击确认提交
        dr.find_element_by_id('org.xc.starlinkother:id/btn_submit').click()
        time.sleep(3)

if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_Xl_Intall_Login('test_Xl_Intall_Login'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='星联APP安装版-自动化测试报告',
                  description='星联APP安装版-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
