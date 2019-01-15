#-*- coding: utf-8 -*-
import time
def outTxt(str,fileName='C:\SPIDER\out.txt'):
    with open(fileName, "a") as f:
        f.writelines(str)
        f.write("\n")

f=open('C:\SPIDER\out.txt', "w+")
f.write("爬虫test 知乎话题热门数据---by zw \n")
time=time.localtime(time.time())
f.write(str(time))
f.close()