import numpy as np  
import tensorflow as tf
from captcha.image import ImageCaptcha
import numpy as np  
import matplotlib.pyplot as plt  
from PIL import Image  
import random   

number = ['0','1','2','3','4','5','6','7','8','9']  
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  

def random_captcha_text(char_set=number+alphabet+ALPHABET, captcha_size=4):  
    captcha_text = []  
    for i in range(captcha_size):  
        c = random.choice(char_set)  
        captcha_text.append(c)  
    return captcha_text  
   

def gen_captcha_text_and_image():  
    image = ImageCaptcha()  
   
    captcha_text = random_captcha_text()  
    captcha_text = ''.join(captcha_text)  
   
    captcha = image.generate(captcha_text)  
    #image.write(captcha_text, captcha_text + '.jpg')   
   
    captcha_image = Image.open(captcha)  
    captcha_image = np.array(captcha_image)  
    return captcha_text, captcha_image  

def convert2gray(img):  
    if len(img.shape) > 2:  
        gray = np.mean(img, -1)  
        # 上面的转法较快，正规转法如下  
        # r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]  
        # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b  
        return gray  
    else:  
        return img  
   
  
def text2vec(text):  
    text_len = len(text)  
    if text_len > MAX_CAPTCHA:  
        raise ValueError('验证码最长4个字符')  
   
    vector = np.zeros(MAX_CAPTCHA*CHAR_SET_LEN)  
    def char2pos(c):  
        if c =='_':  
            k = 62  
            return k  
        k = ord(c)-48  
        if k > 9:  
            k = ord(c) - 55  
            if k > 35:  
                k = ord(c) - 61  
                if k > 61:  
                    raise ValueError('No Map')   
        return k  
    for i, c in enumerate(text):  
        idx = i * CHAR_SET_LEN + char2pos(c)  
        vector[idx] = 1  
    return vector  
# 向量转回文本  
def vec2text(vec):  
    char_pos = vec.nonzero()[0]  
    text=[]  
    for i, c in enumerate(char_pos):  
        char_at_pos = i #c/63  
        char_idx = c % CHAR_SET_LEN  
        if char_idx < 10:  
            char_code = char_idx + ord('0')  
        elif char_idx <36:  
            char_code = char_idx - 10 + ord('A')  
        elif char_idx < 62:  
            char_code = char_idx-  36 + ord('a')  
        elif char_idx == 62:  
            char_code = ord('_')  
        else:  
            raise ValueError('error')  
        text.append(chr(char_code))  
    return "".join(text)  
   
""" 
#向量（大小MAX_CAPTCHA*CHAR_SET_LEN）用0,1编码 每63个编码一个字符，这样顺利有，字符也有 
vec = text2vec("F5Sd") 
text = vec2text(vec) 
print(text)  # F5Sd 
vec = text2vec("SFd5") 
text = vec2text(vec) 
print(text)  # SFd5 
"""  
  
 
   
if __name__ == '__main__':


    text, image = gen_captcha_text_and_image()
    print("验证码图像channel:", image.shape)  # (60, 160, 3)  
    
