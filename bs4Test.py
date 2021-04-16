# -*- encoding: utf-8 -*-
'''
@File    :   bs4-tag.py
@Time    :   2021/04/16 10:19:18
@Author  :   cc 
@Version :   3.9.4
'''
from bs4 import BeautifulSoup

file=open("./笔记.html","rb")
html=file.read()
bs= BeautifulSoup(html,"html.parser")
print(bs.a.string)
print(bs.head.contents[1])