from appium import webdriver
#创建Capability 对话
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='V3HBB18727512494'
desired_caps['platforVersion']='8.0.0'
# 增加配置====>一旦启动时会自动安装 该app文件
# 2.1自动化安装星联app
desired_caps["app"]='F:\starlink_user_v4.1.18_2020-07-06-10-14-48.apk'

# 定义被测app aapt dump badging F:\starlink_user_v4.1.18_2020-07-06-10-14-48.apk
#使用aapt工具查看 包名
desired_caps['appPackage']='org.xc.peoplelive'
desired_caps['appActivity']='org.xc.peoplelive.activity.StartActivity'
# 重点 每次打开 appium 都是以重置（全新）方式打开 ===》noReset设置为false
# 打开 appium 都是以打开过的 方式打开 ===》设置为true
desired_caps['noReset']="false"
#注意处理中文 =====一定要加入这两句
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"
#desired_caps['automationName']='uiautomator2'
# appium访问地址
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# 这里面的等待时间是指每次查找元素时都会发生等待
# 比如查看两次元素就会等待两个3秒
dr.implicitly_wait(3)

# # 点击  取消按钮
# def check_cancelBtn():
#     print("check_cancelBtn")
#
#     try:
#         cancelBtn = driver.find_element_by_id('android:id/button2')
#     except :
#         print('no CancelBtn')
#     else:
#         cancelBtn.click()

# 点击跳过按钮
def check_skipBtn():
    print("check_skipBtn")
    try:
        skipBtn = dr.find_element_by_id('org.xc.peoplelive:id/btnJump')
    except:
        print('no skipBtn')
    else:
        skipBtn.click()

