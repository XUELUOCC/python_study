# -*- encoding: utf-8 -*-
'''
@File    :   sqlite.py
@Time    :   2021/04/17 16:20:34
@Author  :   CC 
@Version :   3.9.4
'''

import sqlite3
import pymysql


conn=sqlite3.connect("test.db")  #打开或创建数据库文件
c=conn.cursor()    #获取游标

sql='''
    create table company
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50)
    );
'''
c.execute(sql)  #执行数据库操作
# cursor=c.execute(sql)  #查询时可获取数据库数据

sql1='''
    INSERT INTO company VALUES
    (1,'名字',39,'北京'),
    (2,'名字2',392,'北京2')
    '''

c.execute(sql1)

conn.commit()  #提交数据库操作
conn.close()   #关闭数据库连接

print('successful')

