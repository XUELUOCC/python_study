# -*- encoding: utf-8 -*-
'''
@File    :   index.py
@Time    :   2021/04/15 14:46:50
@Author  :   cc 
@Version :   3.9.4
'''
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
# import xlwt
import sqlite3

def main():
    # print('hello')
    baseUrl='https://movie.douban.com/top250?start='
    #爬取网页
    getData(baseUrl)
    #保存数据
    # savePath='.\\豆瓣电影Top250.xls'
    # saveData(savePath)

    # askURL(baseUrl)

#爬取网页
def getData(baseUrl):
    dataList=[]
    for i in range(0,10):    #调用它给获取页面的数据10次
        url=baseUrl+str(i*25)
        html=askURL(url)   #爬取网页
    return dataList

#保存数据
def saveData(savePath):
    pass

#得到指定一个url的网页内容
def askURL(url):
    head={
        "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    req=urllib.request.Request(url=url,headers=head)
    html=""
    try:
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        print(html)
    except urllib.error.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"error"):
            print(e.reason)
    return html



#可通过main()函数测试程序，定义程序的入口位置，即程序的开始的点
if __name__=="__main__":   #当程序执行时
    main()