# -*- encoding: utf-8 -*-
'''
@File    :   rotate_test.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/3/10 21:50
@Desciption  :   None
'''

import numpy as np
import cv2

######图像和bbox任意角度旋转函数#######
def image_rotate(image, theta):
    rows, cols = image.shape[0:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), theta, 1)
    print("M:", M)
    print("M[0, 0]:", M[0, 0])
    print("M[0, 1]", M[0, 1])

    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((rows * sin) + (cols * cos))
    nH = int((rows * cos) + (cols * sin))
    M[0, 2] += (nW / 2) - cols / 2
    M[1, 2] += (nH / 2) - rows / 2
    if len(image.shape) == 3:
        dst = cv2.warpAffine(image, M, (nW, nH),borderValue=(255,255,255))
    elif len(image.shape) == 2:
        dst = cv2.warpAffine(image, M, (nW, nH),borderValue=(255,255))
    return dst

######bbox任意角度旋转函数#######
def bbox_rotate(image, xs, ys, theta):
    rows, cols = image.shape[0:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), theta, 1)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((rows * sin) + (cols * cos))
    nH = int((rows * cos) + (cols * sin))
    M[0, 2] += (nW / 2) - cols / 2
    M[1, 2] += (nH / 2) - rows / 2

    nxs = []
    nys = []
    for i in range(len(xs)):
        x1 = int(xs[i] * M[0, 0] + ys[i] * M[0, 1] + M[0, 2])
        y1 = int(xs[i] * M[1, 0] + ys[i] * M[1, 1] + M[1, 2])
        nxs.append(x1)
        nys.append(y1)

    return nxs, nys

if __name__ == '__main__':
    img = cv2.imread(r'C:\Users\lenovo\Desktop\000023.jpg')
    angle = 3
    rotate_img = image_rotate(img, angle)