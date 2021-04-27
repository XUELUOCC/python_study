# -*- encoding: utf-8 -*-
'''
@File    :   index.py
@Time    :   2021/04/27 10:00:37
@Author  :   cc 
@Version :   3.9.4
'''

import urllib.request,urllib.error,urllib.parse
import random
import time
import urllib3
from io import BytesIO   #进行解码
import gzip #进行解码

#可通过main()函数测试程序，定义程序的入口位置，即程序的开始的点
# if __name__=="__main__":   #当程序执行时
#     main()

# def main():
#     pass
    

url="http://www.xbiquge.la/56/56564/"
#http://www.xbiquge.la/56/56564/23611363.html
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

#代理ip
proxy_list=[
    {"http" : "61.135.217.7:80"},
    {"http" : "111.155.116.245:8123"},
    {"http" : "122.114.31.177:808"},
]

#随机抽取ip
proxy=random.choice(proxy_list)


#封装请求header
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
htmls=response.read()

#解码（UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte）
buff = BytesIO(htmls)
f = gzip.GzipFile(fileobj=buff)

print(f.read().decode('utf-8'))


