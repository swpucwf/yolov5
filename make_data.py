# 添加背景图片到训练集
import os
import shutil

bg_img_path = '/Users/chenweifeng/Desktop/captcha_click/backgrounds/images'
train_img_path = 'datasets/train/images'
count = 0
for item in os.listdir(bg_img_path):
    if '.jpg' in item:
        img_path = os.path.join(bg_img_path, item)
        shutil.copy(img_path, os.path.join(train_img_path, item))
        count += 1
print(f'add {count} images')

# 背景图片不添加空标签也可以
# bg_label_path = 'data/backgrounds/labels'
# train_label_path = 'datasets/train/labels'
# count = 0
# for item in os.listdir(bg_label_path):
#     if '.txt' in item:
#         img_path = os.path.join(bg_label_path, item)
#         shutil.copy(img_path, os.path.join(train_label_path, item))
#         count += 1
# print(f'add {count} labels')