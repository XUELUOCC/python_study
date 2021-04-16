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
import xlwt
import sqlite3

def main():
    baseUrl='https://movie.douban.com/top250?start='
    #爬取网页
    dataList=getData(baseUrl)
    #保存数据
    savePath='豆瓣电影Top250.xls'
    saveData(dataList,savePath)

#设置电影的正则表达式  全局变量
findLink=re.compile(r'<a href="(.*?)">')   #href="中间的字符0个或者1个，且这种情况只有一次或者0次"
#设置电影的图片正则
findImgLink=re.compile(r'<img .*src="(.*?)"',re.S)  #re.S 忽略所有的换行符
#设置影片的片名
findTile=re.compile(r'<span class="title">(.*)</span>')
#设置影片的评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#影片的概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getData(baseUrl):
    dataList=[]
    for i in range(0,10):    #调用它给获取页面的数据10次
        url=baseUrl+str(i*25)
        html=askURL(url)   #爬取网页
        soup=BeautifulSoup(html,'html.parser')
        # print(soup.find_all('div',class_="item"))
        for item in soup.find_all('div',class_="item"): #查找div，且class=item的div
            # print(item)
            data=[]   #保存电影所有的信息
            item=str(item)
            try:
                link=re.findall(findLink,item)[0]   #获取影片的详情链接
                data.append(link)

                imgSrc=re.findall(findImgLink,item)[0]
                data.append(imgSrc)

                titles=re.findall(findTile,item)
                if(len(titles)==2):
                    cTitle=titles[0]
                    oTitle=titles[1].replace('/',"") #去掉/
                    data.append(cTitle)
                    data.append(oTitle)
                else:
                    data.append(titles[0])
                    data.append(' ')

                rating=re.findall(findRating,item)[0]
                data.append(rating)

                judgeNum=re.findall(findJudge,item)[0]
                data.append(judgeNum)

                inq=re.findall(findInq,item)
                if len(inq)!=0:
                    inq=inq[0].replace('。',"")
                    print(inq)
                    data.append(inq)
                else:
                    data.append(inq)

                bd=re.findall(findBd,item)[0]
                bd=re.sub('<br(\S+)?/>(\S+)?'," ",bd)  #去掉其中的<br/>
                bd=re.sub('/'," ",bd)   #去掉替换掉/
                bd=bd.replace(" ","")   #去掉字符串中间的空格
                data.append(bd.strip()) #去掉字符串前后的空格

                dataList.append(data)   #将信息添加到dataList
            except IndexError:
                pass
    # print(dataList)
    return dataList

#保存数据
def saveData(dataList,savePath):
    pass
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)  #创建workbook对象
    sheet=book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  #创建工作表格,cell_overwrite_ok=True表示每个单元格覆盖以前的内容
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价人数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])  #将表头写入
    for i in range(0,250):
        print('第%d条'%i)
        try:
            data=dataList[i]
            for j in range(0,8):
                sheet.write(i+1,j,data[j])
        except IndexError:
            pass
    book.save(savePath)

#得到指定一个url的网页内容
def askURL(url):
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Cookie":'bid=L6oUOU9G3YQ; douban-fav-remind=1; __gads=ID=9334ab52387a9ffb-2213c7fa6cc6007f:T=1615792523:RT=1615792523:S=ALNI_MZKzCpIaoM2jrDmL2w_qW6u6HmhLQ; __utmz=30149280.1615792526.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108288"; __utmc=30149280; __utmc=223695111; __utmz=223695111.1618457794.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=0JICxqvldCeQuYAjSxqjp1lmXH0tyAOD; _vwo_uuid_v2=DB8DF4BF8F039A4464EDD7718B1D35195|af1b322060a36eb3a3bf1d1f12611e43; ap_v=0,6.0; _pk_ses.100001.4cf6=*; __utma=30149280.1226424107.1615792526.1618555154.1618562973.5; __utmb=30149280.0.10.1618562973; __utma=223695111.453458065.1618457794.1618555154.1618562973.4; __utmb=223695111.0.10.1618562973; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=b6dfc7e0e9189e18.1618457790.4.1618563174.1618555191.; dbcl2="224211431:mRuwfd1DJlA"'
    }
    req=urllib.request.Request(url=url,headers=head)
    html=""
    try:
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        # print(html)
    except urllib.error.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"error"):
            print(e.reason)
    return html



#可通过main()函数测试程序，定义程序的入口位置，即程序的开始的点
if __name__=="__main__":   #当程序执行时
    main()