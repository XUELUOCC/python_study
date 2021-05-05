# -*- encoding: utf-8 -*-
'''
@File    :   chrome.rq
@Time    :   2021/05/05 11:19:36
@Author  :   CC 
@Version :   3.9.4
'''
from selenium import webdriver

browser=webdriver.Chrome()

browser.get('https://www.zdaye.com/FreeIPlist.html')

container=browser.find_element_by_id('ipc')
tbody=container.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
print(type(tr))

list=[]
for i in tr:
    # print(i.text)
    arr=[]
    arr.append(i.text)
    list.append(arr)
print(list)

