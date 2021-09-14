# -*- coding:utf-8 -*-
import re
import requests
import itertools
import urllib
import os
import sys


def dowmloadPic(html, keyword,index):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    for each in pic_url:
        print('正在下载第' + str(index) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        dir = './'+keyword+'/' + str(index) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        index += 1
    return index

# 生成网址列表
def buildUrls(word,page_nums):
    word = urllib.parse.quote(word)
    urls=[]
    for pn in range(0,page_nums):
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='+str(pn*20)+'&gsm=0&ct=&ic=0&lm=-1&width=0&height=0'
        urls.append(url)
    return urls

def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


if __name__ == '__main__':
    word = "美女"
    mkDir(word)
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    urls=buildUrls(word,5)
    index=0
    for page,url in enumerate(urls):
        result = requests.get(url, headers=headers)
        index=dowmloadPic(result.text, word,index)
        print("已下载 %s 张" % index)

