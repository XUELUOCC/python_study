#-*- codeing = utf-8 -*-     //添加注释，说明任何编译器都是输出utf-8格式
#@Time: ${DATA} ${TIME}      //添加注释，说明此程序生成的时间
#@Author:cc                  //添加注释，说明此程序的作者
#@File: ${NAME}.py           //添加注释，说明文件的拓展名和后缀

f=open("./test.txt","r",encoding="utf-8")
# print(f.read())
print(f.readline(1))   #读取第一行的第一个字符
f.close()

