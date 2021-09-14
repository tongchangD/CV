# import cv2

import os
import cv2
import numpy as np
import PIL.Image as Image
from PIL import ImageDraw,ImageFont
from glob import glob


# source =['0', '1_00', '1_01', '1_02', '1_03', '1_04', '1_10', '1_11', '1_12', '1_13', '1_14', '1', '2', '3', '4', '5', '6', '7', '8']
# filename=[
# "_原图.jpg",
# "_上色.png",
# "_修复.png",
# "_上色-修复.png",
# "_修复-上色.png",
# "_上色-修复-超分(BSRGAN).png",
# "_上色-修复-超分(RealSR).png",
# "_上色-超分(BSRGAN).png",
# "_上色-超分RealSR.png",
# "_修复-上色-超分(BSRGANSR).png",
# "_修复-上色-超分(RealSR).png",]
#
# pic_path = "/media/tcd/data/work/Shanghai_Archives_Bureau/data/total/"
#
# for bef_file_name in source:
#     # print(source)
#     new_image = Image.new('RGB', (7714, 1200), (255, 255, 255))
#     print(bef_file_name)
#     H=0
#     W=0
#     setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 40)
#     fillColor = "#ff0000"
#     for aft_file_name in filename:
#         imgname=pic_path+bef_file_name+aft_file_name
#         images = Image.open(imgname)
#         if "超分" in imgname:
#             draw = ImageDraw.Draw(new_image)
#             new_image.paste(images, (W,0))
#             draw.text((W,1025), aft_file_name[:-4], font=setFont, fill=fillColor)
#             W += (256*4 + 10)
#         else:
#             draw = ImageDraw.Draw(new_image)
#             new_image.paste(images, (W, 0))
#             draw.text((W,260), aft_file_name[:-4], font=setFont, fill=fillColor)
#             W += (256 + 10)
#     print("file",pic_path+bef_file_name+"_total.png")
#     new_image.save(pic_path+bef_file_name+"_total.png")
#
# print("done")


# source =['0', '1_00', '1_01', '1_02', '1_03', '1_04', '1_10', '1_11', '1_12', '1_13', '1_14', '1', '2', '3', '4', '5', '6', '7', '8','b']
#
# pic_path = "/media/tcd/data/work/Shanghai_Archives_Bureau/data/修复"
# new_image = Image.new('RGB', (len(source)*266, 300), (255, 255, 255))
# H=0
# W=0
# setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 40)
# fillColor = "#ff0000"
# for aft_file_name in source:
#     imgname=os.path.join(pic_path,aft_file_name+".png")
#     images = Image.open(imgname)
#     draw = ImageDraw.Draw(new_image)
#     new_image.paste(images, (W, 0))
#     draw.text((W,260), aft_file_name+".png", font=setFont, fill=fillColor)
#     W += (256 + 10)
# print("/home/tcd/Desktop/新建文件夹/color_restore_SR.media/"+os.path.split(pic_path)[-1]+"_total.jpg")
# new_image.save("/home/tcd/Desktop/新建文件夹/color_restore_SR.media/"+os.path.split(pic_path)[-1]+"_total.jpg")


files=["/home/tcd/Desktop/新建文件夹/color_restore_SR.media/原图_total.jpg",
"/home/tcd/Desktop/新建文件夹/color_restore_SR.media/上色_total.jpg",
"/home/tcd/Desktop/新建文件夹/color_restore_SR.media/修复_total.jpg",]

new_image = Image.new('RGB', (len(source)*266, 300*3), (255, 255, 255))
setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 40)
fillColor = "#ff0000"
for i,aft_file_name in enumerate(files):
    images = Image.open(aft_file_name)
    draw = ImageDraw.Draw(new_image)
    new_image.paste(images, (0, i*300))
print("/home/tcd/Desktop/新建文件夹/color_restore_SR.media/_total.jpg")
new_image.save("/home/tcd/Desktop/新建文件夹/color_restore_SR.media/_total.jpg")


# source =['b']
#
# pic_path = "/media/tcd/data/work/Shanghai_Archives_Bureau/tcd/res/"
# filename=[
# "_原图.jpg",
# "_上色.png",
# "_修复.png",
# "_上色-修复.png",
# "_修复-上色.png",
# "_上色-修复-超分(BSRGAN).png",
# "_上色-修复-超分(RealSR).png",
# "_上色-超分(BSRGAN).png",
# "_上色-超分RealSR.png",
# "_修复-上色-超分(BSRGANSR).png",
# "_修复-上色-超分(RealSR).png",]
#
# for bef_file_name in source:
#     # print(source)
#     new_image = Image.new('RGB', (7714, 1200), (255, 255, 255))
#     print(bef_file_name)
#     H=0
#     W=0
#     setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 40)
#     fillColor = "#ff0000"
#     for aft_file_name in filename:
#         imgname=pic_path+bef_file_name+aft_file_name
#         print("imgname",imgname)
#         images = Image.open(imgname)
#         if "超分" in imgname:
#             draw = ImageDraw.Draw(new_image)
#             new_image.paste(images, (W,0))
#             draw.text((W,1025), aft_file_name[:-4], font=setFont, fill=fillColor)
#             W += (256*4 + 10)
#         else:
#             draw = ImageDraw.Draw(new_image)
#             new_image.paste(images, (W, 0))
#             draw.text((W,260), aft_file_name[:-4], font=setFont, fill=fillColor)
#             W += (256 + 10)
#     print("file",pic_path+bef_file_name+"_total.png")
#     new_image.save(pic_path+bef_file_name+"_total.png")

print("done")



"_原图.jpg", "_上色.png", # 对比上色效果

"_原图.jpg", "_修复.png", # 对比修复效果

"_上色-修复.png", "_修复-上色.png", # 对比 上色 修复 流程
"_上色-修复-超分(BSRGAN).png", "_修复-上色-超分(BSRGANSR).png", # 对比 修复 上色 流程
"_上色-修复-超分(RealSR).png", "_修复-上色-超分(RealSR).png", # 对比 修复 上色 流程


"_上色-修复-超分(BSRGAN).png", "_上色-修复-超分(RealSR).png", # 对比 bsrgan 和realsr
"_上色-超分(BSRGAN).png", "_上色-超分RealSR.png",           # 对比 bsrgan 和realsr


"_上色-修复-超分(BSRGAN).png", "_上色-超分(BSRGAN).png", # 对比 加不加 修复
"_上色-修复-超分(RealSR).png", "_上色-超分RealSR.png",  # 对比加不加 修复




source =['0', '1_00', '1_01', '1_02', '1_03', '1_04', '1_10', '1_11', '1_12', '1_13', '1_14', '1', '2', '3', '4', '5', '6', '7', '8']
filename=[
"_原图.jpg",
"_上色.png",
"_修复.png",
"_上色-修复.png",
"_修复-上色.png",
"_上色-修复-超分(BSRGAN).png",
"_上色-修复-超分(RealSR).png",
"_上色-超分(BSRGAN).png",
"_上色-超分RealSR.png",
"_修复-上色-超分(BSRGANSR).png",
"_修复-上色-超分(RealSR).png",]

pic_path = "/media/tcd/data/work/Shanghai_Archives_Bureau/data/total/"
print(os.listdir(pic_path))
setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 40)
fillColor = "#ff0000"
for path in os.listdir(pic_path):
    for img in os.listdir(os.path.join(pic_path,path)):
        imgname=pic_path+path+"/"+img
        images = Image.open(imgname)
        if "超分" in imgname:
            setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 40)
            new_image= Image.new('RGB', (1024, 1124), (255, 255, 255))
            draw = ImageDraw.Draw(new_image)
            new_image.paste(images, (0, 0))
            draw.text((0, 1030), path+img[:-4], font=setFont, fill=fillColor)
            draw = ImageDraw.Draw(images)
            new_image.save(imgname)
        else:
            setFont = ImageFont.truetype('/home/tcd/Desktop/SimSun.ttf', 20)
            new_image = Image.new('RGB', (256, 300), (255, 255, 255))
            draw = ImageDraw.Draw(new_image)
            new_image.paste(images, (0, 0))
            draw.text((0,260), path+img[:-4], font=setFont, fill=fillColor)
            new_image.save(imgname)
print("done")