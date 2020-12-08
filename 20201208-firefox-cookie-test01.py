#!/usr/bin/env  python
#date 2020-12-08
#author:  james jia
#由于打开的是纯净的火狐浏览器，测试带定制功能的火狐浏览器，主要测试FirefoxBinary，FirefoxProfile
#
from selenium import webdriver

	
#本地火狐浏览器Cookie的文件目录
COOKIE_PATH = r'C:\Users\yanfa-jiajj\AppData\Roaming\Mozilla\Firefox\Profiles\gf5wwqww.default-release' 

#webdriver 目录使用的火狐浏览器配置文件
PROFILE_PATH = r'C:\Users\yanfa-jiajj\AppData\Roaming\Mozilla\Firefox\Profiles\dbbmatqc.webdriver'
#本地火狐浏览器驱动的位置
WEBDRIVER_PATH =r'C:\Windows\System32\wbem\geckodriver.exe'
#本地火狐浏览器exe的路径位置
FIREFOX_BINARY_PATH = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'


# 实例化出一个Firefox浏览器 
#firefox_driver =webdriver.Firefox()
#options = webdriver.FirefoxOptions()
#options.add_argument(COOKIE_PATH)
#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
#print(help(webdriver)) 

binary   =  webdriver.FirefoxBinary(firefox_path=FIREFOX_BINARY_PATH)
profile  =  webdriver.FirefoxProfile(profile_directory=PROFILE_PATH)

driver   =  webdriver.Firefox(executable_path=WEBDRIVER_PATH,firefox_binary=binary,firefox_profile=profile)
driver.maximize_window()
driver.get('http://10.10.22.200:3000/login"')
driver.find_element_by_name('user').clear()
driver.find_element_by_name('user').send_keys('admin')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('admin@123')
driver.find_element_by_class_name('css-6ntnx5-button').click()

#cookies = driver.get_cookies()


#firefox_driver.quit()
