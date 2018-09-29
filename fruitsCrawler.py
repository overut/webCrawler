import urllib.request
import re
import requests
import json
 
def getDatas(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1538139567093': ''
                  })
    url = 'https://image.baidu.com/search/index'
    urls = []
    for i in params:
        try:
            response = requests.get(url,params=i,timeout=5)
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误')
            continue
        try:
            jsonData = response.json()
        except json.decoder.JSONDecodeError:
            print("json decode error")    
            continue       
        if jsonData != None :
            #data = requests.get(url,params=i).json().get('data')
            data = jsonData.get('data')
        if data != None:
            urls.append(data)
        #urls.append(requests.get(url,params=i).json().get('data'))
 
    return urls
 
def getImg(datalist,path,dstname):
    for list in datalist:
        for i in list:
            if i.get('thumbURL') != None:
                print('正在下载：%s' % i.get('thumbURL'))
                urllib.request.urlretrieve(i.get('thumbURL'), path+'%d.jpg'%dstname)
                dstname += 1
            else:
                print('图片链接不存在')
 
 
if __name__ == '__main__':
    fruits = ["草莓","蓝莓","葡萄","橘子","柚子","桃子","李子","香蕉","杨梅","荔枝","龙眼","梨子","西瓜","火龙果","哈密瓜","香瓜","菠萝","芒果","榴莲"]
    dstname = 300
    for name in fruits:
        datalist=getDatas(name,10)
        getImg(datalist,'D:/fruits/',dstname)
        dstname += 300

