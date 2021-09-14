import os
import fitz
from glob import glob
import shutil

def check_image_file(filename: str):
    for extension in[".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".JPG", ".JPEG", ".PNG", ".BMP"]:
        if filename.endswith(extension):
            return True
    return False

def pdf_to_img(path,output_path):
    original_files = glob(path+"/*")
    for file in original_files:
        filename=os.path.split(file)[-1]
        if check_image_file(file):
            shutil.copy(os.path.join(path,filename),os.path.join(output_path,filename))
        elif file.endswith(".pdf"):
            doc = fitz.open(file)
            # pdf_name = os.path.splitext(pdf)[0]
            for pg in range(doc.pageCount):
                page = doc[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
                zoom_x = 2.0
                zoom_y = 2.0
                trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
                pm = page.getPixmap(matrix=trans, alpha=False)
                if doc.pageCount==1:
                    if not os.path.exists(os.path.join(output_path, filename.replace(".pdf", ".jpg"))):
                        pm.writePNG(os.path.join(output_path, filename.replace(".pdf", ".jpg")))
                    else:
                        pm.writePNG(os.path.join(output_path, filename.replace(".pdf", "_new.jpg")))
                else:
                    if not os.path.exists(os.path.join(output_path,filename.replace(".pdf","_"+str(pg)+".jpg"))):
                        pm.writePNG(os.path.join(output_path,filename.replace(".pdf","_"+str(pg)+".jpg")))
                    else:
                        pm.writePNG(os.path.join(output_path, filename.replace(".pdf", "_"+str(pg)+"_new.jpg")))
    print("done")

if __name__ == '__main__':
    path="/media/tcd/data/work/Shanghai_Archives_Bureau/new_data/原图"
    output_path="/media/tcd/data/work/Shanghai_Archives_Bureau/new_data/source_img"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    pdf_to_img(path,output_path)


    print("done")

