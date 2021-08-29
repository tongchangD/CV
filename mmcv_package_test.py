mmcv 是一个基础库，主要分为两个部分，  
一部分是和 deep learning framework 无关的一些工具函数，比如 IO/Image/Video 相关的一些操作，  
另一部分是为 PyTorch 写的一套训练工具，可以大大减少用户需要写的代码量，同时让整个流程的定制变得容易。  

https://github.com/open-mmlab/mmcv  
mmcv在安装过程中需要VC++支持，安装过程中出现error：Microsoft Visual C++ 14.0 is required 参照这篇文章解决  

## File IO  
模块提供两个通用的接口用于加载和转储不同形式的文件

### Load and dump data  
```
import mmcv  
#直接从文件加载
#可以加载json,yaml,pkl文件
data = mmcv.load('test.json')
data = mmcv.load('test.yaml')
data = mmcv.load('test.pkl')
# 从一个文件类别加载
with open('test.json', 'r') as f:
    data = mmcv.load(f)
# 将文件转储为字符串
json_str = mmcv.dump(data, file_format='json')
# 将数据转储为文件
mmcv.dump(data, 'out.pkl')
with open('test.yaml', 'w') as f:
    data = mmcv.dump(data, f, file_format='yaml')
```

扩充接口以支持更多的文件形式，需要写一个文件句柄继承BaseFileHandler然后将其注册为其他的文件类型。
```
@mmcv.register_handler('txt')
class TxtHandler1(mmcv.BaseFileHandler):
    def load_from_fileobj(self, file):
        return file.read()
    def dump_to_fileobj(self, obj, file):
        file.write(str(obj))
    def dump_to_str(self, obj, **kwargs):
        return str(obj)
```  
### Load a text file as a list or dict  
使用list_from_file加载文件成list  
使用dict_from_file加载文件成dict
```
mmcv.list_from_file('a.txt')
mmcv.dict_from_file('b.txt')
```
## Image
采用opencv的方式实现，在使用的过程中需要保证opencv已经安装
### Read/Write/Show
```
mmcv.imread()
mmcv.imwrite()
mmcv.imshow()
```
### Color space conversion
```
mmcv.bgr2gray()
mmcv.gray2bgr()
mmcv.bgr2rgb()
mmcv.rgb2bgr()
mmcv.bgr2hsv()
mmcv.hsv2bgr()
```
### Resize（图像尺寸变换）
#调整为指定大小的尺寸、按照尺度变换率调整大小
```
mmcv.imresize()
```
#按照目标图片大小尺寸调整大小
```
mmcv.imresize_like()
```
### Rotate（图像旋转）
#可以指定旋转中心（默认为图像中心点），旋转角度，尺度变换率
```
mmcv.imrotate()
```
### Flip（图像反转）
```
mmcv.imflip(img，direction='vertical')
```
### Crop（图像裁切）
#裁切范围表示为（x1, y1, x2, y2），且必须为list类型
```
mmcv.imcrop(img，bbox)
```
### Padding（填充）
#将图片用指定的值去填充到指定大小
```
mmcv.impad(img,(w,h),pad_val = [r,g,b])
```
#填充图像以确保每个边缘成倍增加到一定数量
```
mmcv.impad_to_multiple(img, divisor=,pad_val = )
```
## video
该模块包含视频读取和转换的接口，视频编辑的一些方法以及光流的读取/写/弯曲
VideoReader
视频序列的处理需要正确安装ffmpeg，Windows环境下详细安装及配置参照如下教程
Windows安装配置ffmpeg_运维_chasiny的博客-CSDN博客
​blog.csdn.net/chy466071353/article/details/54949221

#视频读取
```
mmcv.VideoReader( )将视频读取成frame序列
```
#视频转换
```
cvt2frames(路径)将视频转化为图像帧序列
frames2video(‘路径’,’文件名’)Windows安装配置ffmpeg_运维_chasiny的博客-CSDN博客#视频读取
mmcv.VideoReader( )将视频读取成frame序列
```
#视频转换
```
cvt2frames(路径)将视频转化为图像帧序列
frames2video(‘路径’,’文件名’)
Editing utils

#裁切视频序列
mmcv.cut_video(‘源文件’，’目标文件’，start = ,end = ,vcodec = )
#加入一段视频
mmcv.concat_video([‘源文件’，’添加的文件’]，’目标文件’)
#修改视频的尺寸
mmcv.resize_video(‘源文件’，’目标文件’,（xx,xx），ration=)
visualization
mmcv.imshow()
mmcv.imshow_bboxes(img,boxes)    #在图像上画框
mmcv.imshow_det_bboxes()         #在一幅图上画出检测框
utils
config
Config类用于处理config和config文件。 它支持从多种文件格式（包括python，json和yaml）加载配置。它提供类似dict的api来获取和设置值。

test.py
#########################
a = 1
b = {'b1': [0, 1, 2], 'b2': None}
c = (1, 2)
d = 'string'
##########################

#测试案例
```
cfg = Config.fromfile('test.py')
assert cfg.a == 1
assert cfg.b.b1 == [0, 1, 2]
cfg.c = None
assert cfg.c == None
```
## ProgressBar
#对一系列项目和任务跟踪进度，进度条原位置刷新的方式
```
mmcv.track_progress(func,tasks)
```
#并行任务的跟踪进度
```
mmcv.track_parallel_progress(func,tasks,nproc)
```
#刷新位置的进度条方式
```
mmcv.track_iter_progress(tasks)
```
Timer
基于time来实现
```
timer = mmcv.Timer()
timer.since_start()
timer.since_last_check
```
以上列举了一些常用的mmcv的功能和函数，简单记录，代码自己测试了一部分，比较乱，就不分享了，
可以基于我给的代码去尝试一下，其中多任务Processbar和视频处理由于自己ffmpeg安装不成功所以实验不成功，其他的部分可以参照mmcv文档学习（不是很全面，最好看源码）
