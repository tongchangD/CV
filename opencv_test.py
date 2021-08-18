import cv2
# 分别获取图像 的 RGB 三通道 上 的值
def acquire_RBG(path):
  img = cv2.imread(path)
  img1 = img[0:4, 0:4]
  B = img1[:, :, 0]
  G = img1[:, :, 1]
  R = img1[:, :, 2]
  print("B\n",B,"\nG\n",G,"\nR\n",R)

# BGR 图像转bcbcr 
def bgr_to_ycbcr(one):
    one = one.astype('float32')
    (B, G, R) = cv2.split(one)
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    Cr = (R - Y) * 0.713 + 0.5
    Cb = (B - Y) * 0.564 + 0.5
    return cv2.merge([Y, Cr, Cb])
# ycbcr图转bgr
def ycbcr_to_bgr(one):
    one = one.astype('float32')
    Y, Cr, Cb = cv2.split(one)

    B = (Cb - 0.5) * 1. / 0.564 + Y
    R = (Cr - 0.5) * 1. / 0.713 + Y
    G = 1. / 0.587 * (Y - 0.299 * R - 0.114 * B)

    return cv2.merge([B, G, R])

img=cv2.imread("/home/tcd/Desktop/image-20210816134543164.png")
cv2.imshow("source",img)
Y=bgr_to_ycbcr(img)
# BGR=ycrcb_to_bgr(img)
cv2.imshow("Y",Y)
cv2.imwrite("Y.jpg",Y)
# cv2.imshow("BGR",BGR)
cv2.waitKey(0)
print("done")

