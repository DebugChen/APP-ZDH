# coding=utf-8
# 进行登录业务=====》依赖数据  用户名和密码 ====》形参
from time import sleep
from config.desired_caps import appium_desired


def XL_Install_login(username, password):
    # 后获取封装好的驱动
    dr = appium_desired()
    # # 判断是否有更新提示
    # try:# 尝试运行
    #     # 代表传递一个可变参数====》待会传递进来的是一个元组
    #     cancelBtn = dr.find_element_by_id('android:id/button2')
    # except: # 找不到按钮执行的代码
    #     print("无取消更新按钮")
    # else:# 找到按钮执行的代码
    #     cancelBtn.click()

    # 判断是否有欢迎提示
    try:
        skipBtn = dr.find_element_by_id('org.xc.starlinkother:id/btnJump')
    except:
        print("无点击跳过欢迎按钮")
    else:
        skipBtn.click()
    sleep(1)
    # #开始登陆
    # 点击获取位置权限
    dr.find_element_by_id(
        'android:id/button1').click()
    sleep(1)
    # 点击获取相机权限
    dr.find_element_by_id(
        'android:id/button1').click()
    sleep(1)
    # 点击获取存储权限
    dr.find_element_by_id(
        'android:id/button1').click()
    # 输入账户
    dr.find_element_by_id('org.xc.starlinkother:id/etTel').send_keys(username)
    # dr.find_element_by_xpath('//android.widget.EditText[@text="请输入手机号"]').send_keys(username)
    # 输入密码
    dr.find_element_by_id('org.xc.starlinkother:id/etCode').send_keys(password)
    # 点击屏幕键盘的搜索键，收起输入法
    # dr.press_keycode(66)
    # 点击登录
    dr.find_element_by_id('org.xc.starlinkother:id/btnLogin').click()
    # 等待登录完成
    sleep(3)

    # print("检测是否有那种弹出广告（比如信任有礼）")
    # try:
    #     #检测账户登录后是否有账户下线提示
    #     element1 = dr.find_element_by_id("com.tal.kaoyan:id/tip_commit")
    # except:
    #     print("没有账号提示下线提示")
    # else:
    #     element1.click()

    # # 检测是否有我知道了按钮
    # try:
    #     element2 = dr.find_element_by_id("com.tal.kaoyan:id/task_no_task")
    # except:
    #     print("没有弹出广告提示")
    # else:
    #     element2.click()

    # 根据 个人---元素是否存在---判断是否登录成功
    try:
        dr.find_element_by_id("org.xc.peoplelive:id/smallLabel")
    except: # 捕获异常----》 代表没有找到首页 这个标签
        print("登录失败")
        return  False
    else: # 找到的内容
        print("登录成功")
        return True

    # # 点击首页设备切换
    # dr.find_element_by_id('org.xc.peoplelive:id/btnLogin').click()

    # # 获取屏幕坐标
    # def get_size():
    #     # 字典===》键值对组成
    #     # 屏幕的宽
    #     x = dr.find_element_by_id('find_element_by_id')['width']
    #     # 屏幕的高
    #     y = dr.find_element_by_id('find_element_by_id')['height']
    #     return x, y
    #
    # # 函数 向左滑动
    # def swipe_left():
    #     # 注意 这是英文字母l 变量===>元组
    #     ll = get_size()
    #     print("屏幕尺寸", ll)
    #     # 起始点 ll[0]===》576
    #     x1 = int(ll[0] * 0.9)
    #     # 结束点   保证起始点》结束点
    #     x2 = int(ll[0] * 0.1)
    #     # y轴不变ll[0]====》1024  y1==y2
    #     y1 = int(ll[1] * 0.5)
    #     # swipe函数5个参数
    #     # 参数1和参数2
    #     # 起始点x1，y1
    #     # 参数3和参数4
    #     # 结束点x2，y2
    #     # 参数5是完成滑动所需要时间
    #     dr.swipe(x1, y1, x2, y1, 1000)


# def TestHd(self, element):
#     """
#     IOS专用 在元素内部滑动
#     """
#     scrolldict = {'direction': 'left', 'org.xc.peoplelive:id/civ': element.id}
#     self.driver.execute_script('mobile: swipe', scrolldict)

# # 调用函数滑动两次次
# for i in range(2):  # 0,1 ===>代表循环两次
#     TestHd()
#     sleep(1)  # 休眠1秒

if __name__=='__main__':
    XL_Install_login("7888", "douniu2918")
