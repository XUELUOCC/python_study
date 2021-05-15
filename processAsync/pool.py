# -*- encoding: utf-8 -*-
'''
@File    :   pool.py
@Time    :   2021/05/14 11:15:01
@Author  :   cc 
@Version :   3.9.4
'''

import time
from multiprocessing.dummy import Pool

startTime=time.time()
def test(str):
    print('正在下载',str)
    time.sleep(2)
    print('下载完成',str)

str_list=['aaa','bbb','ccc']

#创建线程池对象,参数：创建几个线程
pool=Pool(3)
pool.map(test,str_list)

endTime=time.time()
print('执行时间',endTime-startTime)