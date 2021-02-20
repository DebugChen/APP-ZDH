import time
from appium import webdriver

desired_caps={}
# 为字典增加键值对
desired_caps["platformName"]='Android'
desired_caps["platformVersion"]='8.0.0'
desired_caps["deviceName"]='V3HBB18727512494'
# 增加配置====>一旦启动时  会自动安装 该app文件
# 2.1自动化安装考研帮app
# desired_caps["app"]='C:\kaoyan3.1.0.apk'
# 使用aapt工具得到
desired_caps["appPackage"]='org.xc.peoplelive'
desired_caps["appActivity"]='org.xc.peoplelive.activity.StartActivity'
#注意在界面元素处理中文输入 =====一定要加入这两句
desired_caps['unicodeKeyboard']="True"  #中文支持unicode字符
desired_caps['resetKeyboard']="True"  # 重置按键
# app---被测试项目每次都是以全新方式打开
desired_caps["noReset"]=False
#通过该字典json信息===》创造驱动==》 驱动appium+手机上app的执行
# 注意 导包时候必须使用导入  appium的 webdriver
#from appium import webdriver
# 参数1：appium一个远程(localhost)访问的地址
# 参数2： desired_capabilities 信息
dr=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
# 对查找元素 -----进行隐式等待工作
#implicitly_wait(5)  ====>寻找页面元素时 最多找5秒 超过5秒 未找到报错
dr.implicitly_wait(5)

# 判断是否有欢迎提示
try:
    skipBtn = dr.find_element_by_id('org.xc.peoplelive:id/btnJump')
except:
    print("无点击跳过欢迎按钮")
else:
    skipBtn.click()

# #开始登陆
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
dr.find_element_by_id('org.xc.peoplelive:id/etTel').send_keys('13200000000')
# dr.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号")').send_keys(username)
# dr.find_element_by_class_name('android.widget.EditText').click()
# dr.find_element_by_class_name('android.widget.EditText').send_keys(username)
# 输入验证码
dr.find_element_by_id('org.xc.peoplelive:id/etCode').send_keys('123456')
# 点击屏幕键盘的搜索键，收起输入法
dr.press_keycode(66)
# 点击登录
dr.find_element_by_id('org.xc.peoplelive:id/btnLogin').click()
# 等待登录完成
time.sleep(3)
dr.find_element_by_class_name('android.view.ViewGroup').click()
time.sleep(1)
dr.find_element_by_id('org.xc.peoplelive:id/img_right').click()
time.sleep(2)
dr.find_element_by_id('org.xc.peoplelive:id/btnCancal').click()
time.sleep(2)
dr.find_element_by_id('org.xc.peoplelive:id/tv_left').click()
time.sleep(2)
