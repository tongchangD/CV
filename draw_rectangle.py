#encoding=utf-8
import cv2
import os
import shutil
import numpy as np
import time
import copy
from glob import glob
#创建回调函数
def draw_(event,x,y,flags,param):
    global ix,iy,drawing,mode,respath,filename
    #当按下左键是返回起始位置坐标

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing =True
        ix,iy=x,y

    #当鼠标左键按下并移动时绘制图形,event 可以看成移动,flag 查看是否按下
    elif event ==cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        pass
        # if mode == True:
        #     cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),thickness=2)
        # else:
        #     #绘制圆圈,小圆点连在一起就成了线,3 代表了笔画的粗细
        #     cv2.circle(img,(x,y),3,(0,0,120),-1)
            #起始点为圆心,起点到终点为半径的
            #r = int(np.sqrt((x-ix)**2+(y-iy)**2))
            #cv2.circle(img,(x,y),r(0,0,255),-1)
    #当鼠标松开,停止绘制
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),thickness=2)
        # print(dada)
        global h,w,ih,iw
        h = x
        w = y
        ih = ix
        iw = iy
        # imgdada=img_new[iy:y,ix:x]
        # cv2.imwrite(os.path.join(respath,filename.split(".")[0]+time.strftime('_%H_%M_%S')+"."+filename.split(".")[1]), imgdada)
    drawing ==False

if __name__ == "__main__":
    h = 0
    w = 0
    ih = 0
    iw = 0
    path = glob("/home/tcd/Desktop/image_down/上海旧照片/*")
    respath = "/media/tcd/data/github/CV/code/CV_project/res"
    if not os.path.exists(respath):
        os.makedirs(respath)
    i = 0
    # cv2.namedWindow('image',0)
    # cv2.resizeWindow('image', 600, 600)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow('image', 0, 0)
    cv2.setMouseCallback('image', draw_, param=("da"))
    while (1):
        drawing = False #鼠标按下时变为True
        mode = True #mode 为true 绘制矩形,按"m"变成绘制曲线
        global x,y
        ix,iy = -1,-1
        if i >=len(path):
            break
        else:
            img=cv2.imread(path[i])
            filename=os.path.split(path[i])[-1]
            img_new=copy.deepcopy(img)
            while(1):
                cv2.imshow('image',img)
                k=cv2.waitKey(1)&0xFF
                if k==ord('m'): # 按"m"变成绘制曲线
                    mode = not mode
                # 96 49 50
                elif k == 49: # 直接保存
                    print(k,"直接保存，下一张")
                    i += 1
                    shutil.copy(path[1],os.path.join(respath,filename))
                    break
                elif k == 50: # 剪切 下一张
                    print(k,"剪切，下一张")
                    imgdada=img_new[iw:w,ih:h]
                    cv2.imwrite(os.path.join(respath,filename.split(".")[0]+time.strftime('_%H_%M_%S')+"."+filename.split(".")[1]), imgdada)
                    i += 1
                    break
                elif k == 96:   # 删除 既是 不 copy
                    print(k,"不做操作，下一张")
                    i += 1
                    break
                elif k==27:
                    exit(0)
            cv2.destroyAllWindows()


