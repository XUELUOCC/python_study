# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2021/05/11 11:36:50
@Author  :   cc 
@Version :   3.9.4
'''

#模拟登录 
# "https://passport.mafengwo.cn/login/"

import requests
from bs4 import BeautifulSoup

def main():
    url='"https://passport.mafengwo.cn/login/"'
    getLogin(url)

def getLogin(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Referer": "https://passport.mafengwo.cn/"
    }
    FormData={
        'LoginForm':{
            'username':'雪落cc',
            'password':'CC135790'
        } 
    } 
    res=requests.post(url=url,data=FormData,headers=headers)
    print("%d%s"%(res.status_code,'aa'))
    print(res)
    res.encoding='utf-8'
    html=res.text

    soup=BeautifulSoup(html,'html.parser')
    account=soup.find_all('div',id='wrapper')
    # print(soup)

#可通过main()函数测试程序，定义程序的入口位置，即程序的开始的点
if __name__=="__main__":   #当程序执行时
    main()