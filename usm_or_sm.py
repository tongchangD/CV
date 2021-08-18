
# ##  锐化掩模
def sharp(img):
    dst1 = cv2.GaussianBlur(img, (101, 101), 100) 
    img_enhance = cv2.addWeighted(img, 2, dst1, -1, 0);
    return img_enhance

# ## 非锐化掩膜
def usm_sharp(img, weight=0.5, radius=50, threshold=10):
    if radius % 2 == 0:
        radius += 1
    blur = cv2.GaussianBlur(img, (radius, radius), 0)
    residual = img - blur
    mask = np.abs(residual) * 255 > threshold
    mask = mask.astype('float32')
    soft_mask = cv2.GaussianBlur(mask, (radius, radius), 0)
    K = img + weight * residual
    K = np.clip(K, 0, 1)
    return soft_mask * K + (1 - soft_mask) * img
   
