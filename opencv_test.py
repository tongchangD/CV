import cv2
# 分别获取图像 的 RGB 三通道 上 的值
def acquire_RBG(path):
  img = cv2.imread(path)
  img1 = img[0:4, 0:4]
  B = img1[:, :, 0]
  G = img1[:, :, 1]
  R = img1[:, :, 2]
  print("B\n",B,"\nG\n",G,"\nR\n",R)

