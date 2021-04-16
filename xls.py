# -*- encoding: utf-8 -*-
'''
@File    :   xls.py
@Time    :   2021/04/16 15:48:39
@Author  :   cc 
@Version :   3.9.4
'''

import xlwt

wookbook=xlwt.Workbook(encoding='utf-8')  #创建workbook对象
wooksheet=wookbook.add_sheet('sheet1')  #创建工作表格
# wooksheet.write(0,0,'hello')  #写入数据，第一个参数“行”，第二个参数“列”，第三个参数“写入的内容”
for i in range(0,9):
    for j in range(0,i+1):
        wooksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
wookbook.save('study.xls') #保存数据表