#!/usr/bin/env  python
#date 2020-12-08
#author:  james jia
#由于打开的是纯净的火狐浏览器，从已有火狐浏览器cookie文件中获取cookie记录
#
from selenium import webdriver

#本地火狐浏览器Cookie的文件目录
COOKIE_PATH = r'C:\Users\yanfa-jiajj\AppData\Roaming\Mozilla\Firefox\Profiles\gf5wwqww.default-release' 
#本地火狐浏览器驱动的位置
WEBDRIVER_PATH =r'C:\Windows\System32\wbem\geckodriver.exe'


# 实例化出一个Firefox浏览器 
#firefox_driver =webdriver.Firefox()

options = webdriver.FirefoxOptions()
options.add_argument(COOKIE_PATH)
#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])

driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH,options=options)
driver.maximize_window()
driver.get('http://10.10.22.200:3000/login"')
driver.find_element_by_name('user').clear()
driver.find_element_by_name('user').send_keys('admin')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('admin@123')
driver.find_element_by_class_name('css-6ntnx5-button').click()

cookies = driver.get_cookies()
#打印所有cookie显示
print(cookies)

#firefox_driver.quit()
