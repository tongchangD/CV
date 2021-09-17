"""
去除水印 失败的代码
"""

import  cv2
import numpy as  np
from PIL import Image
import os
from itertools import product


def def1():
    test_dir = 'xxx'
    mask_dir = 'xxx'
    save_dir ='xxx'
    src = cv2.imread(test_dir)
    mask = cv2.imread(mask_dir)
    save = np.zeros(src.shape, np.uint8)
    for row in range(src.shape[0]):
        for col in range(src.shape[1]):
            for channel in range(src.shape[2]):
                if mask[row, col, channel] == 0:
                    val = 0
                else:
                    reverse_val = 255 - src[row, col, channel]
                    val = 255 - reverse_val * 256 / mask[row, col, channel]
                    if val < 0:
                        val = 0
                save[row, col, channel] = val
    cv2.imwrite(save_dir, save)

def def2():
    img = Image.open('./322.jpg')
    width, height = img.size
    for pos in product(range(width), range(height)):
        if sum(img.getpixel(pos)[:3]) > 600:
            img.putpixel(pos, (255, 255, 255))
    img.save('removed_1.png')

def drop_wartermark(path, newpath):
    img = cv2.imread(path, 1)
    # img.shape[:3] 则取彩色图片的高、宽、通道。
    hight, width, depth = img.shape[0:3]
    print(hight)
    print(width)
    # 裁剪水印坐标为[y0:y,x0:x1]
    cropped = img[int(hight * 0.9):hight, int(width * 0.7):width]
    # cropped = img[hight-49:hight, width-180:width]
    cv2.imwrite(newpath, cropped)
    # 将图片加载为内存对象 参一：完整路径；参二：flag：-1彩色，0灰色，1原有
    imgsy = cv2.imread(newpath, 1)

    # 图片二值化处理，把[200,200,200]~[255, 255, 255]以外的颜色变成0
    # 这个颜色区间就是水印周边的背景颜色
    thresh = cv2.inRange(imgsy, np.array([28, 28, 28]), np.array([54, 54, 54]))
    # #创建形状和尺寸的结构元素 创建水印蒙层
    kernel = np.ones((3, 3), np.uint8)
    # 对水印蒙层进行膨胀操作
    hi_mask = cv2.dilate(thresh, kernel, iterations=10)
    specular = cv2.inpaint(imgsy, hi_mask, 5, flags=cv2.INPAINT_TELEA)
    cv2.imwrite(newpath, specular)

    # 覆盖图片
    imgsy = Image.open(newpath)
    img = Image.open(path)
    img.paste(imgsy, (int(width * 0.7), int(hight * 0.9), width, hight))
    img.save(newpath)

def def3(path):
    # coding=utf-8
    # 图片修复

    img = cv2.imread(path)
    hight, width, depth = img.shape[0:3]

    # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
    thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))

    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)

    # 扩张待修复区域
    hi_mask = cv2.dilate(thresh, kernel, iterations=1)
    specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

    cv2.namedWindow("Image", 0)
    cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
    cv2.imshow("Image", img)

    cv2.namedWindow("newImage", 0)
    cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
    cv2.imshow("newImage", specular)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def def4(path,newPath):
    img = cv2.imread(path, 1)
    hight, width, depth = img.shape[0:3]
    # 截取
    cropped = img[int(hight * 0.8):hight, int(width * 0.7):width]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(newPath, cropped)
    imgSY = cv2.imread(newPath, 1)
    # 图片二值化处理，把[200,200,200]-[250,250,250]以外的颜色变成0
    thresh = cv2.inRange(imgSY, np.array([200, 200, 200]), np.array([250, 250, 250]))
    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)
    # 扩展待修复区域
    hi_mask = cv2.dilate(thresh, kernel, iterations=10)
    specular = cv2.inpaint(imgSY, hi_mask, 5, flags=cv2.INPAINT_TELEA)
    cv2.imwrite(newPath, specular)
    # 覆盖图片
    imgSY = Image.open(newPath)
    img = Image.open(path)
    img.paste(imgSY, (int(width * 0.7), int(hight * 0.8), width, hight))
    img.save(newPath)

if __name__ == '__main__':
    path="./322_1.jpg"
    newpath="./322_2.jpg"
    ######### 失败的  #############
    # def1()
    # def2()
    # drop_wartermark(path, newpath)
    # def3(path)
    # def4(path,newpath) # 稍微还行 其实也不行
    ######### 失败的  #############
