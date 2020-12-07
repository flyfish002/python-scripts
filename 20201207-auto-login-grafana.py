#-*- coding:utf8 -*-
#!/usr/bin/env  python
#date 2020-12-06
#author:  james jia
#
#
from selenium import webdriver

# 实例化出一个Firefox浏览器 
driver =webdriver.Firefox()

# 设置浏览器窗口的位置和大小
driver.set_window_position(20,40)
driver.set_window_size(1100,700)

# 打开一个页面（grafana登录页）
driver.get("http://10.10.22.200:3000/login")

# 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
driver.find_element_by_name('user').clear()
driver.find_element_by_name('user').send_keys('admin')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('admin@123')
driver.find_element_by_class_name('css-6ntnx5-button').click()

# do something
driver.get("http://10.10.22.200:3000/d/omSUlOcMk/19-3lian-xiang-fu-wu-qi-server01?orgId=1&var-group=19-3%E8%81%94%E6%83%B3%E6%9C%8D%E5%8A%A1%E5%99%A8server1&var-host=%E8%81%94%E6%83%B3%E6%9C%8D%E5%8A%A1%E5%99%A8-10.196.1.120")


# 退出窗口
#driver.quit()
