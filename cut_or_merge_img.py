def cut_big_pic(img_path, source_min_img_path, height_cut, width_cut,lenth):
    if lenth!=0:
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
        height, width, depth = img.shape
        height_cut = height // lenth
        width_cut = width // lenth
        pattern_height = lenth
        pattern_width = lenth
        for j in range(height_cut):
            for i in range(width_cut):
                #  切割的时候如果是靠边的最后一个就将图片加宽，保持原本的尺寸
                left_h = j * pattern_height
                left_w = i * pattern_width
                right_h = left_h + pattern_height
                right_w = left_w + pattern_width
                if i == width_cut - 1 or j == height_cut - 1:
                    if i == width_cut - 1:
                        right_w = width if width >= width_cut * lenth else (left_w + pattern_width)
                    if j == height_cut - 1:
                        right_h = height if height >= height_cut * lenth else (left_h + pattern_height)
                sub_img = img[left_h: right_h, left_w: right_w]
                cv2.imencode('.jpg', sub_img)[1].tofile(
                    os.path.join(source_min_img_path, os.path.split(img_path)[1][:-4] + '_{}{}'.format(j, i) + '.jpg'))
    else:
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
        height, width, depth = img.shape
        min_height = height // height_cut
        min_width = width // width_cut
        diff_width = min_width if width == width_cut * min_width else width - width_cut * min_width + min_width
        diff_height = min_height if height == height_cut * min_height else height - height_cut * min_height + min_height
        for j in range(height_cut):
            for i in range(width_cut):
                #  切割的时候如果是靠边的最后一个就将图片加宽，以便保持原本的尺寸
                left_h = j * min_height
                left_w = i * min_width
                right_h = left_h + min_height
                right_w = left_w + min_width
                if i == width_cut - 1 or j == height_cut - 1:
                    if i == width_cut - 1:
                        right_w = width if width >= width_cut * min_width else (left_w + diff_width)
                    if j == height_cut - 1:
                        right_h = height if height >= height_cut * min_height else (left_h + diff_height)
                sub_img = img[left_h: right_h, left_w: right_w]
                cv2.imencode('.jpg', sub_img)[1].tofile(
                    os.path.join(source_min_img_path, os.path.split(img_path)[1][:-4] + '_{}{}'.format(j, i) + '.jpg'))


def image_compose2(source_img_path, source_min_img_path, res_pic_path):
    # 获取 文件夹 中 的图片 数量及其 尺寸
    min_pic_file = os.listdir(source_min_img_path)
    img1 = cv2.imdecode(np.fromfile(os.path.join(source_min_img_path, min_pic_file[0]), dtype=np.uint8), -1)
    min_height, min_width, depth = img1.shape
    diff_width = 0
    diff_height = 0
    height_cut = 0
    width_cut = 0
    for file in min_pic_file:
        img1 = cv2.imdecode(np.fromfile(os.path.join(source_min_img_path, file), dtype=np.uint8), -1)
        height, width, depth = img1.shape
        if height != min_height:
            diff_height = height
        if width != min_width:
            diff_width = width
        nums = file[:-4].split("_")[1]
        if int(nums[0]) >= height_cut:
            height_cut = int(nums[0])
        if int(nums[1]) >= width_cut:
            width_cut = int(nums[1])
    height_cut += 1
    width_cut += 1

    diff_width = min_width if diff_width == 0 else diff_width
    diff_height = min_height if diff_height == 0 else diff_height

    print(diff_width, diff_height)
    new_image = Image.new('RGB',
                          (min_width * (width_cut - 1) + diff_width, min_height * (height_cut - 1) + diff_height))

    for j in range(height_cut):
        for i in range(width_cut):
            print(os.path.join(source_min_img_path,
                               os.path.split(source_img_path)[1][:-4] + '_{}{}'.format(j, i) + '.png'))
            temp_images = Image.open(os.path.join(source_min_img_path,
                                                  os.path.split(source_img_path)[1][:-4] + '_{}{}'.format(j,
                                                                                                          i) + '.png'))
            new_image.paste(temp_images, (i * min_width, j * min_height))
    return new_image.save(res_pic_path)

# cut_big_pic(img_path, source_min_img_path, 4, 4,0)# 3和4位值表示行列各是多少，5位值 是切割的照片的尺寸 长宽相等
# image_compose2(source_img_path, source_min_img_path, res_pic_path)
