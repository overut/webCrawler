#!-*- coding:utf-8 -*-
#FileName : appleCrawler.py
 
import re 
import requests #python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import random 
 
#定义函数方法
def spiderPic(html,keyword):
    print('正在查找 ' + keyword +' 对应的图片,下载中，请稍后......')
    for addr in re.findall('"objURL":"(.*?)"',html,re.S):     #查找URL
        print('正在爬取URL地址：'+str(addr)[0:30]+'...') 
        try:
            pics = requests.get(addr,timeout=3)  
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误')
            continue
 
        fq = open('D:\\img\\' + (keyword+'_'+str(random.randrange(0,1000,4))+'.jpg'),'wb')     
        fq.write(pics.content)
        fq.close()
 
if __name__ == '__main__':
    word = input('请输入你要搜索的图片关键字：')
    result = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word)
 

spiderPic(result.text,word)