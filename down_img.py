# -*- coding:utf-8 -*-
import os
import sys
import re
from bs4 import BeautifulSoup
import datetime
import requests


def dowmloadPic(html, index):
    # pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    pic_url = re.findall(' <a href="/(.*?)"><img src ="/', html, re.S)

    for each in pic_url:
        each=("http://data.zjda.gov.cn/"+each)
        print('正在下载第' + str(index) + '张图片，图片地址:' + each)
        try:
            pic = requests.get("http://data.zjda.gov.cn/old/dadb/lstk/qdrw/201411/W020160512379849236067.jpg", timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        dir = './'+ str(index) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        index += 1

        requests1=requests.get(url=each).content
        print("requests1",requests1)
        with open("dada"+str(index)+".jpg","wb") as f:
            f.write(requests1)

        each = ("http://kr.shanghai-jiuxin.com/file/2021/0429/11a56f6cbc984b11c49c6cfe3f755adc.jpg")
        pic = requests.get(each, timeout=10)
        print("pic.content",pic.content)
        print(da)



    return index


def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


def method_two():
    start = datetime.datetime.now()
    count=0
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    html_frist = "http://data.zjda.gov.cn/col/col14/index.html"
    try:
        html = requests.get(html_frist,headers=headers)
    except:
        print ("垃圾")
    html.encoding="utf-8"
    # title = re.findall("target=\"_blank\" href=\"(.*)\" style",html.text)
    title = re.findall("(.*).html",html.text)
    print("html.text",html.text)
    print("title",title)
    print(da)
    for each in title:
        count+=1
        html_url = "http://www.customs.gov.cn"+each
        print ("\t",html_url)
        html1 = requests.get(html_url)
        html1.encoding = "utf-8"
        sensece = html1.text
        soup = BeautifulSoup(html1.text, 'html.parser')  # 文档对象
        str1=""
        for k in soup.findAll("div",class_="easysite-info-con"):
            str1 += str(k).replace("<div class=\"easysite-info-con\">","").replace("</div>","").replace("<p>","").replace("</p>","").replace("\n","").strip()+"@#$^@"
        #print str1[:-5]
        q = str1.split("@#$^@")[0]
        a = str1.split("@#$^@")[1]
    end =  datetime.datetime.now()
    print ("耗时:%s S"%((end-start).seconds))

if __name__ == '__main__':
    word = "旧照片"
    mkDir(word)
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    index=0
    urls =[]
    # for i in range(14,33):  # 好多张 从 7 开始 7 重定向
    #     urls.append("http://data.zjda.gov.cn/col/col"+str(i)+"/index.html")
    for i in range(1,10):
        urls.append("http://data.zjda.gov.cn/art/2014/11/1/art_14_"+str(i)+".html")
    print("urls",urls)
    for i,url in enumerate(urls):
        htmls = requests.get(url, headers=headers)
        index=dowmloadPic(htmls.text,index)
        print("已下载 %s 张" % index)

