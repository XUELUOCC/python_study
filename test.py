# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2021/04/13 15:26:24
@Author  :   cc 
@Version :   3.9.4
'''

'''
string='aaa'
string1='bbb'
# print('字符串是%s'%(string))
print('字符串1是%s,字符串2是%s'%(string,string1))
print('hhh\n')
print('aaaa')
'''

# password=input('请输入密码')
# print('密码是',password)

# a=90
# b='aaa'
# if a==12 and b=='aaa':
#     print('true')
# else:
#     print('false')
# if a>=90 :
#     print('A')
#     if (b=='aa'):
#         print('插入b')
#     else:
#         print('没有b')
# elif (a>=60) :
#     print('B')
# elif (a>=30):
#     print('C')
# else:
#     print('不合格') 

# print(type(a))

# a=12
# b=str(a)
# print(type(b))

# a='1'
# b=ord(a)
# print(b)

# a='qqq'
# b='wwww'
# print(a+'11')

# arr=[1,2,3]
# b=(1,2,3)
# newArr=arr.insert(1,2)
# print(arr)
# print(len(arr))
# print(type(b))

# def test(a,b):
#     return a+b

# print(test(1,2))

import urllib.request,urllib.error,urllib.parse

# response=urllib.request.urlopen('http://python.org/')
# print(response.read().decode('utf-8'))

#将信息转化成form表单提交数据
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))
url='https://www.douban.com'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

