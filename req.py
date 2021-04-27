# -*- encoding: utf-8 -*-
'''
@File    :   requests.python
@Time    :   2021/04/27 14:45:37
@Author  :   cc 
@Version :   3.9.4
'''

import requests
from bs4 import BeautifulSoup

def main():
    url="http://www.xbiquge.la/56/56564/"
    ipUrl=" https://www.zdaye.com/FreeIPlist.html"
    # getNovel(url)
    getIpList(ipUrl)

def getNovel(url):    
    # url="http://www.xbiquge.la/56/56564/"
    #http://www.xbiquge.la/56/56564/23611363.html
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    #代理ip
    proxies={
        "https" : "https://111.23.16.250:3128"
    }
    #爬取
    response=requests.get(url=url,headers=headers,proxies=proxies)
    #请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。
    # 当你访问 r.text 之时，Requests 会使用其推测的文本编码。你可以找出 Requests 使用了什么编码，
    # 并且能够使用 r.encoding 属性来改变它
    response.encoding='utf-8'  
    print(response.text)
    return response.text

def getIpList(ipUrl):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive"
    }
    response=requests.get(url=ipUrl,headers=headers)
    response.encoding='utf-8'
    html=response.text
    # print(response.text)
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find_all('table',id='ipc')
    tbodys=table[0].find_all('tbody')
    trs=tbodys[0].find_all('tr')
    dataList=[]
    for item in trs:
        data=[]

        ip=item.find_all('td')[0].string
        data.append(ip)

        port=item.find_all('td')[1].string
        data.append(port)

        dataList.append(data)
    print(dataList)



#可通过main()函数测试程序，定义程序的入口位置，即程序的开始的点
if __name__=="__main__":   #当程序执行时
    main()