from appium import webdriver
import yaml
import os

#文件  =====》封装读取yaml文件方式----了解
def appium_desired():
    # 获取当前路径---就算被别的文件调用 获取当前位置
    base_dir = os.path.dirname(__file__)
    yaml_path = os.path.join(base_dir, 'ck_kyb_caps.yaml')
    print(yaml_path)
    ckfile=open(yaml_path,'r',encoding='utf-8')
    # 加载yaml文件
    data=yaml.load(ckfile)
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    # os.path.dirname代表获取当前路径  比如  c：/a/b/c.txt ====>c：/a/b/
    # 两层的话再获取上一层路径
    base_dir = os.path.dirname(os.path.dirname(__file__))
    print("项目路径",base_dir)
    # 获取项目路径下 app路径下的 apk文件
    app_path = os.path.join(base_dir,'app', data['appname'])
    desired_caps['app']=app_path
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']
    # appium服务的端口
    dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    dr.implicitly_wait(4)
    return dr

# 单元测试
if __name__ == '__main__':
    appium_desired()
