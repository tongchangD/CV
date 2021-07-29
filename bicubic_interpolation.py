import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import math

def double_linear(input_signal, zoom_multiples):
    '''
    双线性插值 
    :param input_signal: 输入图像
    :param zoom_multiples: 放大倍数
    :return: 双线性插值后的图像
    '''
    input_signal_cp = np.copy(input_signal)   # 输入图像的副本
    input_row, input_col = input_signal_cp.shape # 输入图像的尺寸（行、列）
    # 输出图像的尺寸
    output_row = int(input_row * zoom_multiples)
    output_col = int(input_col * zoom_multiples)
    output_signal = np.zeros((output_row, output_col)) # 输出图片
    for i in range(output_row):
        for j in range(output_col):
            # 输出图片中坐标 （i，j）对应至输入图片中的最近的四个点点（x1，y1）（x2, y2），（x3， y3），(x4，y4)的均值
            temp_x = i / output_row * input_row
            temp_y = j / output_col * input_col
            x1 = int(temp_x)
            y1 = int(temp_y)
            x2 = x1
            y2 = y1 + 1
            x3 = x1 + 1
            y3 = y1
            x4 = x1 + 1
            y4 = y1 + 1
            u = temp_x - x1
            v = temp_y - y1
            # 防止越界
            if x4 >= input_row:
                x4 = input_row - 1
                x2 = x4
                x1 = x4 - 1
                x3 = x4 - 1
            if y4 >= input_col:
                y4 = input_col - 1
                y3 = y4
                y1 = y4 - 1
                y2 = y4 - 1
            # 插值
            output_signal[i, j] = (1-u)*(1-v)*int(input_signal_cp[x1, y1]) + (1-u)*v*int(input_signal_cp[x2, y2]) + u*(1-v)*int(input_signal_cp[x3, y3]) + u*v*int(input_signal_cp[x4, y4])
    return output_signal
    

def BiLinear_interpolation(img,dstH,dstW):
    scrH,scrW,_=img.shape
    img=np.pad(img,((0,1),(0,1),(0,0)),'constant')
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx=(i+1)*(scrH/dstH)-1
            scry=(j+1)*(scrW/dstW)-1
            x=math.floor(scrx)
            y=math.floor(scry)
            u=scrx-x
            v=scry-y
            retimg[i,j]=(1-u)*(1-v)*img[x,y]+u*(1-v)*img[x+1,y]+(1-u)*v*img[x,y+1]+u*v*img[x+1,y+1]
    return retimg

img = cv2.imread("../paojie_g.jpg",0).astype(np.float)
out = double_linear(img,2).astype(np.uint8)
cv2.imwrite("out.jpg", out)

im_path='../paojie.jpg'
image=np.array(Image.open(im_path))
image2=BiLinear_interpolation(image,image.shape[0]*2,image.shape[1]*2)
image2=Image.fromarray(image2.astype('uint8')).convert('RGB')
image2.save('out.png')
