# -*- encoding: utf-8 -*-
'''
@File    :   draw_bbox_on_image.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/3/18 11:12
@Desciption  :   None
'''

# import tensorflow as tf
import matplotlib.pyplot as plt
import random
import os
import time
import cv2
import numpy as np



# 显示图片
def plt_bboxes(img, ratio, bboxes, figsize=(10, 10), linewidth=2.5):
    """Visualize bounding boxes. Largely inspired by SSD-MXNET!
    """
    fig = plt.figure(figsize=figsize)
    plt.imshow(img)
    height = img.shape[0]
    width = img.shape[1]
    colors = dict()
    cls_id = 0
    if cls_id not in colors:
        colors[cls_id] = (random.random(), random.random(), random.random())
        print(colors)

    # ###bbox缩放前给左右边界扩充5个像素，上下扩充3个像素###
    # bboxes[0][0][0] -= 0
    # bboxes[0][0][1] -= 1
    # bboxes[0][0][2] += 3
    # bboxes[0][0][3] += 3

    ###回缩比例,边界处理###
    ymin1 = int(bboxes[0] / ratio[0])
    ymin = max(ymin1, 0)
    xmin = max(int(bboxes[1] / ratio[1]), 0)
    ymax = min(int(bboxes[2] / ratio[0]), height)
    xmax = min(int(bboxes[3] / ratio[1]), width)

    print("ymin1:", ymin1)
    rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                         ymax - ymin, fill=False,
                         edgecolor=colors[cls_id],
                         linewidth=linewidth)
    plt.gca().add_patch(rect)
    # plt.gca().text(xmin, ymin - 2,
    #                  '{:s} | {:.3f}'.format(class_name, score),
    #                   bbox=dict(facecolor=colors[cls_id], alpha=0.5),
    #                  fontsize=12, color='white')
    plt.show()


if __name__ == '__main__':
    imgpath = r'D:\liuan58\ocrdata\zc_fz_10000_opt\org_train_jpg_and_xml_from_55\zc_fz_jpg_2230'
    img = cv2.imread(imgpath + '/'+ '12_3140_zc' + '.jpg')
    ratio = [1, 1]
    bbox = [ 16, 23, 59, 218]
    plt_bboxes(img, ratio, bbox)

