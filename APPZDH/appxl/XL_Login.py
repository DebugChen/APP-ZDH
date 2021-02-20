from Config.ConfigAPP import dr,check_skipBtn,desired_caps
import time

#点击取消欢迎界面
check_skipBtn()
##开始登陆
# 点击获取位置权限
dr.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
# 点击获取相机权限
dr.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
# 点击获取存储权限
dr.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
# 输入账户
dr.find_element_by_id('org.xc.peoplelive:id/etTel').send_keys('13200000000')
# 输入密码
dr.find_element_by_id('org.xc.peoplelive:id/etCode').send_keys('123456')
# 点击登录
dr.find_element_by_id('org.xc.peoplelive:id/btnLogin').click()
