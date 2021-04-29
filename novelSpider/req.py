# -*- encoding: utf-8 -*-
'''
@File    :   requests.python
@Time    :   2021/04/27 14:45:37
@Author  :   cc 
@Version :   3.9.4
'''

import requests
from bs4 import BeautifulSoup
import re
# import xlwt
import xlsxwriter

def main():
    url="http://www.xbiquge.la/66/66995/"
    ipUrl=" https://www.zdaye.com/FreeIPlist.html"
    savePath='高人竟在我身边小说章节.xlsx'

    dataList=getNovel(url)  #获取小说章节和链接

    # getIpList(ipUrl)---未完成，爬取代理ip

    getNovelContent(dataList)  #获取小说内容  

    setExcel(dataList,savePath)  #将信息保存到excel中

    # list=[1,2,3,4,5,6,7,8,67,76,78]
    # getMaxWidth(list)  #测试最大表格单元格宽度
    # test('http://www.xbiquge.la/66/66995/27578826.html')  #测试函数

def test(url):
    content=''
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    html=response.text
    # print(html)

    soup=BeautifulSoup(html,'html.parser')
    #正文保存标题
    title=soup.find_all('div',class_='bookname')[0]
    title=str(title)

    titleContent=re.findall(r'<h1>(.*?)</h1>',title,re.S)[0]
    strTitle=re.sub('\（.*?\）','','(aaa)（bbb）cc')
    strTitle=re.sub('\(.*?\)','',strTitle)
    print(strTitle)

    path='F://cc文件//python_study//novelSpider//novelData/'  #保存路径

    #内容
    content=re.findall(r'<div id="content">(.*?)</div>',html,re.S)[0]
    content=content.replace('<br />','\n')  #替换<br />
    content=content.replace('&nbsp;','\t')  #替换&nbsp;

    #保存文件
    # f=open(path+'/'+strTitle+'.txt','w',encoding="utf-8")
    # f.write(content)
    # f.close()


#爬取小说章节
def getNovel(url):    
    novelList=[]  #章节链接，名称
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
    html=response.text 

    soup=BeautifulSoup(html,'html.parser')
    listNovel=soup.find_all('div',id='list')
    # print(listNovel)
    dls=listNovel[0].find_all('dl')
    dds=dls[0].find_all('dd')

    for item in dds:
        data=[]
        try:
            href='http://www.xbiquge.la'+ item.find_all('a')[0]['href']
            data.append(href)

            name=item.find_all('a')[0].string
            data.append(name)

            novelList.append(data)
        except IndexError:
            pass
    # print(novelList)
    return novelList

#爬取小说内容，并保存
def getNovelContent(dataList):
    pass
    for i in range(len(dataList)):
        content=''
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }
        try:
            url=dataList[i][0]
            response=requests.get(url=url,headers=headers)
            response.encoding='utf-8'
            html=response.text
            # print(html)

            soup=BeautifulSoup(html,'html.parser')
            #正文保存标题
            title=soup.find_all('div',class_='bookname')[0]
            title=str(title)

            titleContent=re.findall(r'<h1>(.*?)</h1>',title,re.S)[0]
            strTitle=re.sub('\（.*?\）','',titleContent)   #去掉中文括号以及括号内的内容
            strTitle=re.sub('\(.*?\)','',strTitle)  #去掉英文括号以及括号内的内容
            print(strTitle)

            path='F://cc文件//python_study//novelSpider//novelData/'  #保存路径

            #内容
            content=re.findall(r'<div id="content">(.*?)</div>',html,re.S)[0]
            content=content.replace('<br />','\n')  #替换<br />
            content=content.replace('&nbsp;','\t')  #替换&nbsp;

            #保存文件
            f=open(path+'/'+strTitle+'.txt','w',encoding="utf-8")
            f.write(content)
            f.close()

            if (i>=len(dataList)):
                print('爬取完成')
        except IndexError:
            pass

#将小说章节数据添加到表格中
def setExcel(dataList,savePath):
    book=xlsxwriter.Workbook(savePath)  #创建excel文件
    sheet=book.add_worksheet('test-sheet')   #创建工作表格对象
    col=('章节链接','章节名称')
    col_width=[]
    
    for i in range(0,2):
        sheet.write(0,i,col[i])   #写入表头 ，写入数据

    length=len(dataList)
    for i in range(0,length):
        try:
            data=dataList[i]
            for j in range(0,2):
                sheet.write(i+1,j,data[j])
                col_width.append(len(data[j].encode('gb18030')))

        except IndexError:
            pass
        maxwidth=getMaxWidth(col_width)  #拿到最大宽度
        sheet.set_column(0,1,maxwidth) # 设置列宽

    book.close()  #关闭excel文件

#获取存入excel中的数据的单元格最大宽度
def getMaxWidth(list):
    max=list[0]
    for i in range(len(list)):
        try:
            if(list[i]>max):
                max=list[i]
        except IndexError:
            pass
    # print(max)
    return max

#爬取代理网站中的代理ip---未完成，需要用到selenium获取浏览器动态加载的数据源码
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